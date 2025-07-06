from agno.agent import Agent
from agno.models.mistral import MistralChat
import os
from dotenv import load_dotenv

load_dotenv()

model = MistralChat(id="mistral-small",api_key=os.getenv("MISTRAL_API_KEY"),temperature=0.3)

grammar_agent = Agent(model=model,
    description="Fix grammar, spelling, and improve writing style.")


def correct_text(text):
    prompt = (
    f"Please proofread the following text for grammar, spelling, and clarity. "
    f"Ensure the language sounds natural and professional. "
    f"Return only the corrected version: {text}")
    response = grammar_agent.run(prompt)
    return response.content  
