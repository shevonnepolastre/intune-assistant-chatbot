import os
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

# Load environment variables
load_dotenv()

# Create a credential
credential = DefaultAzureCredential()

# Connect to your Azure AI Foundry Project
project = AIProjectClient.from_connection_string(
    conn_str=os.environ["AIPROJECT_CONNECTION_STRING"],
    credential=credential,
)

# Correct client: get Azure OpenAI compatible client
openai_client = project.inference.get_azure_openai_client(api_version="2024-06-01")

# Prepare messages
messages = [
    {"role": "system", "content": "You are a Microsoft Intune expert helping users enroll their devices into Intune."},
    {"role": "user", "content": "How do I enroll a Windows 10 device into Intune?"},
]

# Call the OpenAI API properly
response = openai_client.chat.completions.create(
    model=os.environ["CHAT_MODEL"],  # e.g., "gpt-4o-mini"
    messages=messages,
)

# Output the response
print("Response from Azure OpenAI:")
print(response.choices[0].message.content)

# Show tracing URL
print("\nView traces at:")
print(f"https://ai.azure.com/tracing?wsid=/subscriptions/{project.scope['subscription_id']}/resourceGroups/{project.scope['resource_group_name']}/providers/Microsoft.MachineLearningServices/workspaces/{project.scope['project_name']}")
