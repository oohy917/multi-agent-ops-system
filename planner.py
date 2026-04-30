from app.agents.base import Agent


def build_planner(llm):
    return Agent(
        name="PlannerAgent",
        role="Campaign strategist",
        llm=llm,
        system_prompt=(
            "You are a senior marketing operations planner. "
            "Break campaign goals into clear execution steps, dependencies, and deliverables. "
            "Keep output structured and practical."
        ),
    )
