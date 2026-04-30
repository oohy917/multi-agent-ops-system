from app.agents.base import Agent


def build_analyst(llm):
    return Agent(
        name="AnalystAgent",
        role="Performance analyst",
        llm=llm,
        system_prompt=(
            "You are a digital marketing analyst. "
            "Define KPIs, tracking plan, A/B tests, and optimization actions. "
            "Output should be actionable."
        ),
    )
