from agno.agent import Agent
from agno.models.mistral import MistralChat
import os
from dotenv import load_dotenv

load_dotenv()

model = MistralChat(
    id="mistral-small",
    api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0.3  
)

grammar_agent = Agent(
    model=model,
    description="Fix grammar, spelling, and improve writing style."
)


def correct_text(text: str):
    prompt = (
        f"Please correct the grammar, spelling, and clarity of the following text: {text} Only return the corrected version."
    )
    response = grammar_agent.run(prompt)
    return response.content  
