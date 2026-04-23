import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

DEFAULT_MODEL_ID = "Qwen/Qwen1.5-0.5B-Chat"


class LocalTransformersClient:
    """
    A lightweight local chat client built on top of Hugging Face Transformers.
    """

    def __init__(self, model_id: str = DEFAULT_MODEL_ID, device: str | None = None):
        self.model_id = model_id
        self.device = device or self._resolve_device()
        self.tokenizer = None
        self.model = None

    @staticmethod
    def _resolve_device() -> str:
        if torch.cuda.is_available():
            return "cuda"
        if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
            return "mps"
        return "cpu"

    def load(self) -> None:
        if self.tokenizer is not None and self.model is not None:
            return

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_id).to(self.device)
            self.model.eval()
        except Exception as exc:
            raise RuntimeError(f"加载本地模型失败: {exc}") from exc

    def generate(
        self,
        messages: list[dict[str, str]],
        max_new_tokens: int = 256,
        temperature: float = 0.7,
        top_p: float = 0.9,
    ) -> str:
        self.load()

        if self.tokenizer is None or self.model is None:
            raise RuntimeError("模型尚未完成初始化。")

        prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        model_inputs = self.tokenizer([prompt], return_tensors="pt").to(self.device)

        generation_kwargs = {
            "max_new_tokens": max_new_tokens,
            "top_p": top_p,
            "pad_token_id": self.tokenizer.eos_token_id,
        }

        if temperature > 0:
            generation_kwargs["do_sample"] = True
            generation_kwargs["temperature"] = temperature
        else:
            generation_kwargs["do_sample"] = False

        with torch.no_grad():
            generated_ids = self.model.generate(
                input_ids=model_inputs.input_ids,
                attention_mask=model_inputs.attention_mask,
                **generation_kwargs,
            )

        new_token_ids = generated_ids[:, model_inputs.input_ids.shape[1]:]
        return self.tokenizer.batch_decode(new_token_ids, skip_special_tokens=True)[0].strip()
