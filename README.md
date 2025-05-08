# Intune Assistant Chatbot

I'm currently participating in the Microsoft AI Skills Fest. One of my technical mentors suggested building a chatbot using Retrieval-Augmented Generation (RAG) to deepen my AI learning.  

I'm learning Python and want to pivot toward DevOps and AI — this project combines both as a real-world practice project.

Therefore, I decided to build a chatbot that teaches users how to implement Microsoft Intune for a company.

---

## Why Intune?

I am about to manage a project that involves standing up Microsoft Intune for a client.  
Building this chatbot gives me a practical, hands-on way to explore device management concepts while advancing my Python, Azure, and AI development skills.

---

## Project Scenario

This project builds an intelligent chatbot to assist IT support teams and employees at **Skyline Dynamics** with Microsoft Intune device enrollment, compliance, and troubleshooting.

The chatbot uses Retrieval-Augmented Generation (RAG) to dynamically retrieve internal documentation and Intune policy information at runtime, ensuring accurate and contextually relevant responses.

---

## Architecture Overview

- **Frontend**: Copilot SDK chatbot interface
- **Backend**: Azure AI Foundry SDK and Python
- **Retrieval Strategy**: RAG — retrieves documents and data at runtime to ground LLM responses
- **Search Engine**: Azure Cognitive Search

<br>

<img src="https://github.com/shevonnepolastre/intune-assistant-chatbot/blob/main/images/azure_rag_chatbot_architecture.png" alt="Azure AI Foundry RAG Architecture" width="600">

---

## What I Learned

- How to create and configure an Azure AI Foundry project
- How to index internal documents into Azure AI Search
- How to create a custom intent mapping model using Azure Prompty files
- How to perform semantic search with vector embeddings
- How to add observability with Application Insights tracing
- How to debug common errors with Azure OpenAI deployments (e.g., invalid URL errors)
- How to build an end-to-end RAG solution grounded in a real-world business case

---

## Resources 

- [Tutorial: Part 1 - Set up project and development environment to build a custom knowledge retrieval (RAG) app with the Azure AI Foundry SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/tutorials/copilot-sdk-create-resources?tabs=macos)
- [Create AI Search Service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal)
- [How to trace your application with Azure AI Foundry project library (preview)](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/trace-local-sdk?tabs=python)
- [OpenAI GPT-3 API error: "Invalid URL (POST /v1/chat/completions)"](https://stackoverflow.com/questions/75882988/openai-gpt-3-api-error-invalid-url-post-v1-chat-completions)

---

## Technologies Used

- Python
- Azure AI Foundry SDK
- Azure Cognitive Search
- Azure OpenAI Service
- GitHub
- VS Code
- Retrieval-Augmented Generation (RAG)
- OpenTelemetry + Application Insights (for tracing)

