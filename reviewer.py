from app.agents.base import Agent


def build_reviewer(llm):
    return Agent(
        name="ReviewAgent",
        role="Brand, compliance and quality reviewer",
        llm=llm,
        system_prompt=(
            "You are a strict marketing reviewer. "
            "Check clarity, unsupported claims, tone, audience fit, CTA, and platform suitability. "
            "Return approval status and concrete edits."
        ),
    )
