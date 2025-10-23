from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from dataclasses import dataclass

@dataclass
class ModelLoader:
    model_name: str
    try:
        def load_model_and_tokenizer(self) -> pipeline:
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            model = AutoModelForCausalLM.from_pretrained(self.model_name)
            chat_bot_pipeline = pipeline("text-generation",model=model, tokenizer=tokenizer)
            return chat_bot_pipeline
    except Exception as e:
        raise RuntimeError(f"Failed to load model or tokenizer: {e}")