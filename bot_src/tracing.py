from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Foundry
project = AIProjectClient.from_connection_string(
    conn_str=os.environ["AIPROJECT_CONNECTION_STRING"],
    credential=DefaultAzureCredential()
)

openai_client = project.inference.get_azure_openai_client(api_version="2024-06-01")

messages = [
    {"role": "system", "content": "You are a Microsoft Intune expert."},
    {"role": "user", "content": "How do I enroll a Windows 10 device into Intune?"}
]

response = openai_client.chat.completions.create(
    model=os.environ["CHAT_MODEL"],  # gpt-4o-mini
    messages=messages,
)

print(response.choices[0].message.content)
