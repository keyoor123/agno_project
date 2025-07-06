from agno.agent import Agent
from agno.models.mistral import MistralChat
import os
from dotenv import load_dotenv

load_dotenv()

model = MistralChat(id="mistral-small",api_key=os.getenv("MISTRAL_API_KEY"),temperature=0.3)

summarizer_agent = Agent(model=model,
    description="Summarize long text into a concise 5-sentence summary.")



def summarize_text(text):
    prompt = (
    f"Please summarize the following text in 5–6 well-structured sentences. "
    f"Focus on the key ideas while maintaining clarity and original meaning:{text}")
    response = summarizer_agent.run(prompt)
    return response.content  
