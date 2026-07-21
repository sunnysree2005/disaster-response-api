# Local Disaster Response Bot 🚨

## Overview
An AI-powered emergency communication assistant designed to process localized, unstructured distress messages (Bengali/Regional dialects/English) during natural disasters and instantly convert them into actionable data for rescue teams.

## How Codex & GPT-5.6 Were Used:
- **Codex:** Used to architect the backend FastAPI routes, setup data validation models (Pydantic), and structure the error-handling logic efficiently.
- **GPT-5.6:** Utilized for high-context natural language understanding to parse chaotic, multilingual crisis messages and extract precise location, urgency level, and emergency categories.

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set your OpenAI API key and run: `uvicorn main:app --reload`