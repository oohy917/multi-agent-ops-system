from app.agents.base import Agent


def build_copywriter(llm):
    return Agent(
        name="CopywriterAgent",
        role="Channel copywriter",
        llm=llm,
        system_prompt=(
            "You are a concise B2B technology copywriter. "
            "Write benefit-led social and web copy. Avoid jargon unless necessary. "
            "Create different versions for different channels."
        ),
    )
