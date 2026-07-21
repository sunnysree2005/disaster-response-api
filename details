# Local Disaster Response Bot 🚨



An AI-powered emergency coordination backend built with **FastAPI** and **OpenAI** to streamline disaster management and rescue operations in Bangladesh.

## 🚀 Features
* **Automated Data Extraction**: Parses unstructured emergency messages (SMS/Social Media) into clean, actionable JSON data.
* **Key Fields Extracted**:
  * `location`: Identifies the exact affected area (e.g., Sylhet).
  * `emergency_type`: Categorizes the crisis (e.g., Flood, Cyclone, Medical, Food Shortage, Rescue).
  * `urgency_level`: Evaluates priority (High, Medium, Low).
  * `summary`: Generates a concise English brief for rapid rescue dispatch.

## 🛠️ Tech Stack
* **Python**
* **FastAPI** / **Pydantic**
* **OpenAI API (GPT-4o-mini)**
* **Google Colab / TestClient** (for cloud execution and testing)

## 📌 API Endpoint
* **URL/Route**: `/process-emergency`
* **Method**: `POST`
* **Request Body Example**:
  ```json
  {
    "user_input": "Sylhet e banha porse, khabar ar pani lagbe."
  }
Response Example:

JSON
{
  "status": "success",
  "data": "{\n  \"location\": \"Sylhet\",\n  \"emergency_type\": \"Flood\",\n  \"urgency_level\": \"High\",\n  \"summary\": \"There is severe flooding in Sylhet and the user is in urgent need of food and drinking water.\"\n}"
}
