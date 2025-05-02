# Intune Assistant Chatbot

Currently going through the Microsoft AI Skills Fest.  One of my technical mentors pointed me in this direction in building a chatbot using RAG.  

I expect this to take my six weeks, so this is the breakdown of my plans:

Week 1 – Planning & Kickoff
- Define the chatbot's audience (Admin, Helpdesk, End User)
- Draft basic user flows and install paths (Windows, macOS, mobile)
- Choose bot tech: Azure Bot Service + Composer or Node.js

Week 2 – Bot Framework Setup
- Create the initial bot project
- Add Azure hosting (Bot Service or App Service)
- Deploy a "Hello World" version

Week 3 – Add Intune Dialog Logic
- Build Intune install flow (Windows) using PowerShell and Company Portal
- Add instructions for macOS, iOS, and Android
- Chatbot Intune Install Steps

Week 4 – Data Integration (Graph + CI/CD)
- Register Azure AD app for Microsoft Graph API access
- Connect bot to Graph to retrieve device and policy info
- Set up GitHub Actions to automate bot deployment

Week 5 – Secure & Monitor
- Add Azure Key Vault for storing secrets
- Configure Managed Identity or app registration for authentication
- Integrate Application Insights for logs and telemetry

Week 6 – Deploy & Recap
- Finalize production deployment
- Test chatbot with sample users

## Why Intune

I am going to be managing a project where we are standing up Intune so thought it would be good to create a chatbot that helps a team stand it up.  

## Resources 

(Tutorial: Part 1 - Set up project and development environment to build a custom knowledge retrieval (RAG) app with the Azure AI Foundry SDK) [ https://learn.microsoft.com/en-us/azure/ai-foundry/tutorials/copilot-sdk-create-resources?tabs=macos ]
