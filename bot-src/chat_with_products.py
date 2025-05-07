import os
from pathlib import Path
from opentelemetry import trace
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from config import ASSET_PATH, get_logger, enable_telemetry
from get_product_documents import get_product_documents

# initialize logging and tracing objects
logger = get_logger(__name__)
tracer = trace.get_tracer(__name__)

# create a project client using environment variables loaded from the .env file
project = AIProjectClient.from_connection_string(
    conn_str=os.environ["AIPROJECT_CONNECTION_STRING"], credential=DefaultAzureCredential()
)

# no need for chat client if skipping chat.complete()

@tracer.start_as_current_span(name="chat_with_products")
def chat_with_products(messages: list, context: dict = None) -> dict:
    if context is None:
        context = {}

    documents = get_product_documents(messages, context)

    # Instead of calling chat.complete, just reply with a simple hardcoded response
    response_content = (
        "Here are some documents I found based on your question. "
        "Please review them to find your answer."
    )

    logger.info(f"✨ Assistant Response: {response_content}")

    # Return a mock chat protocol compliant response
    return {"message": {"content": response_content}, "context": context}

if __name__ == "__main__":
    import argparse

    # load command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--query",
        type=str,
        help="Query to use to search product",
        default="How do I setup co-management?",
    )
    parser.add_argument(
        "--enable-telemetry",
        action="store_true",
        help="Enable sending telemetry back to the project",
    )
    args = parser.parse_args()

    if args.enable_telemetry:
        enable_telemetry(True)

    # run chat with products
    result = chat_with_products(messages=[{"role": "user", "content": args.query}])

    print("\n📄 Search Results:")
    for idx, doc in enumerate(result["context"].get("grounding_data", [[]])[0], 1):
        print(f"Document {idx}: {doc['title']} ({doc['url']})")

    print("\n💬 Assistant Response:")
    print(result["message"]["content"])
