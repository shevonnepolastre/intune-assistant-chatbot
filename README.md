# Intune Assistant Chatbot

Currently going through the Microsoft AI Skills Fest.  One of my technical mentors pointed me in this direction in building a chatbot using Retrieval-Augmented Generation (RAG).  

Currently, I'm learning Python and want to focus on Devops and AI since that's where I want to go. 

Therefore, I decided to take do a chatbot that teaches you how to implement Intune for a company.  

## Why Intune

I am going to be managing a project where we are standing up Intune so thought it would be good to create a chatbot that helps a team stand it up.  

## Project Scenario
This project builds an intelligent chatbot that assists IT support and employees at Skyline Dynamics with Microsoft Intune device enrollment, compliance, and troubleshooting. The chatbot leverages Retrieval-Augmented Generation (RAG) to dynamically pull context from internal documentation and live Intune policy data.

## Architecture Overview
Frontend: Copilot SDK chatbot interface

Backend: Azure AI Foundry and Python 

Retrieval Strategy: RAG - retrieve documents and data at runtime to enrich LLM responses

<img src="https://github.com/shevonnepolastre/intune-assistant-chatbot/blob/main/images/azure_rag_chatbot_architecture.png">

## Resources 

[Tutorial: Part 1 - Set up project and development environment to build a custom knowledge retrieval (RAG) app with the Azure AI Foundry SDK] ( https://learn.microsoft.com/en-us/azure/ai-foundry/tutorials/copilot-sdk-create-resources?tabs=macos )
[Create AI Search Service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal)
[How to trace your application with Azure AI Foundry project library (preview)](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/trace-local-sdk?tabs=python)
[OpenAI GPT-3 API error: "Invalid URL (POST /v1/chat/completions)"](https://stackoverflow.com/questions/75882988/openai-gpt-3-api-error-invalid-url-post-v1-chat-completions)

## Technology Used 
- Python
- Azure AI
- GitHub 
- VS Code 
- Retrieval-Augmented Generation (RAG)