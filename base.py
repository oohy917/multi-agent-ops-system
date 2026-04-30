from dataclasses import dataclass
from app.llm import LLMProvider


@dataclass
class Agent:
    name: str
    role: str
    system_prompt: str
    llm: LLMProvider

    def run(self, user_prompt: str) -> str:
        return self.llm.generate(self.system_prompt, user_prompt)
