import asyncio
import os
from google.antigravity import Agent, LocalAgentConfig, types

# Setup Google Antigravity Configuration
# Automatically checks for GEMINI_API_KEY from environment.
api_key = os.getenv("GEMINI_API_KEY", "MOCK_KEY_FOR_DESIGN_OR_SDK")

config = LocalAgentConfig(
    api_key=api_key,
    capabilities=types.CapabilitiesConfig(
        enable_subagents=True,
    )
)

async def main():
    print("Initializing Multi-Agent System...")

    # We instantiate the Master Agent to orchestrate the sub-tasks
    master_instruction = """
    You are the Agent Master. You coordinate three specialist sub-agents:
    1. Database & Schema Agent (Expert in PostgreSQL & schema optimization)
    2. Link Verification & Mirror Agent (Expert in mirror checks and fallback algorithms)
    3. Optimization & API Agent (Expert in FastAPI, performance, and search indexes)

    Your task is to orchestrate a detailed execution plan to verify database sanity, mirror ping logic, and API consistency.
    """

    async with Agent(config, system_instruction=master_instruction) as agent:
        # Requesting Database & Schema Agent task
        print("\n--- Delegating Database Schema Design ---")
        db_response = await agent.chat(
            "Spawn the Database & Schema Agent to analyze 'schema.sql' for index optimizations "
            "and suggest query-tuning strategies for User_Analytics tracking."
        )
        print(await db_response.text())

        # Requesting Link Verification & Mirror Agent task
        print("\n--- Delegating Mirror Health-check Logic ---")
        mirror_response = await agent.chat(
            "Spawn the Link Verification & Mirror Agent to design a Python-based periodic ping utility "
            "that verifies links and swaps inactive status in the database if a 404 is detected."
        )
        print(await mirror_response.text())

        # Requesting API & Indexing Agent task
        print("\n--- Delegating API Grid & Search Design ---")
        api_response = await agent.chat(
            "Spawn the Optimization & API Agent to verify 'api_routes.py' endpoints, ensure it handles "
            "fuzzy matches correctly, and propose Meilisearch integration steps."
        )
        print(await api_response.text())

if __name__ == "__main__":
    # To run the script: python agent_orchestrator.py
    asyncio.run(main())
