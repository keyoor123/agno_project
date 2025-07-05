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
        "You are a grammar expert. Proofread the following text. Fix grammar, spelling, and improve clarity.\n\n"
        f"{text}\n\n"
        "Return only the corrected version."
    )
    response = grammar_agent.run(prompt)
    return response.content  
