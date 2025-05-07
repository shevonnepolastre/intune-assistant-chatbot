import os
from pathlib import Path
from opentelemetry import trace
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from bot_src.config import ASSET_PATH, get_logger, enable_telemetry
from bot_src.get_intune_documents import get_intune_documents

from azure.ai.inference.tracing import AIInferenceInstrumentor 

# Instrument AI Inference API 

AIInferenceInstrumentor().instrument()

# initialize logging and tracing objects
logger = get_logger(__name__)
tracer = trace.get_tracer(__name__)

# create a project client using environment variables loaded from the .env file
project = AIProjectClient.from_connection_string(
    conn_str=os.environ["AIPROJECT_CONNECTION_STRING"], credential=DefaultAzureCredential()
)

# create a chat client we can use for testing
chat = project.inference.get_chat_completions_client()

from azure.ai.inference.prompts import PromptTemplate


@tracer.start_as_current_span(name="chat_with_intune")
def chat_with_intune(messages: list, context: dict = None) -> dict:
    if context is None:
        context = {}

    documents = get_intune_documents(messages, context)

    # do a grounded chat call using the search results
    grounded_chat_prompt = PromptTemplate.from_prompty(Path(ASSET_PATH) / "grounded_chat.prompty")

    system_message = grounded_chat_prompt.create_messages(documents=documents, context=context)
    response = chat.complete(
        model=os.environ["CHAT_MODEL"],
        messages=system_message + messages,
        **grounded_chat_prompt.parameters,
    )
    logger.info(f"💬 Response: {response.choices[0].message}")

    return {"message": response.choices[0].message, "context": context}


    if __name__ == "__main__":
        import argparse

    # load command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--query",
        type=str,
        help="Query to use to search product",
        default="I need a new tent for 4 people, what would you recommend?",
    )
    parser.add_argument(
        "--enable-telemetry",
        action="store_true",
        help="Enable sending telemetry back to the project",
    )
    args = parser.parse_args()
    if args.enable_telemetry:
        enable_telemetry(True)

    # run chat with intune
    response = chat_with_intune(messages=[{"role": "user", "content": args.query}])

    print(response)

