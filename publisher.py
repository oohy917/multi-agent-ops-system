from app.agents.base import Agent


def build_publisher(llm):
    return Agent(
        name="PublisherAgent",
        role="Publishing operations coordinator",
        llm=llm,
        system_prompt=(
            "You are a publishing operations coordinator. "
            "Create a practical publishing calendar, channel schedule, and asset checklist. "
            "This is a simulation; do not claim actual posting."
        ),
    )
