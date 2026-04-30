from app.agents.base import Agent


def build_researcher(llm):
    return Agent(
        name="ResearchAgent",
        role="Market and audience researcher",
        llm=llm,
        system_prompt=(
            "You are a B2B market researcher. "
            "Summarize target audience, pain points, product angles, objections, and positioning opportunities. "
            "Do not fabricate exact external data. Mark assumptions clearly."
        ),
    )
