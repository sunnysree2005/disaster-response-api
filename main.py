import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="Local Disaster Response Bot")

# OpenAI ক্লায়েন্ট ইনিশিয়ালাইজ করা
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

class EmergencyRequest(BaseModel):
    user_input: str  # ইউজারের ভয়েস ট্রান্সক্রিপ্ট বা টেক্সট

@app.post("/process-emergency")
def process_emergency(data: EmergencyRequest):
    try:
        # GPT-5.6 প্রম্পটিং: অগোছালো তথ্য থেকে জরুরি ডেটা এক্সট্রাক্ট করা
        prompt = f"""
        You are an AI disaster response coordinator in Bangladesh. Analyze the following user message (which might be in Bengali, regional dialect, or English) and extract structured JSON data.
        
        Message: "{data.user_input}"
        
        Extract these fields:
        - location: (Where is the user?)
        - emergency_type: (e.g., Flood, Cyclone, Medical, Food Shortage, Rescue)
        - urgency_level: (High, Medium, Low)
        - summary: (A brief English summary for rescue teams)
        """
        
        response = client.chat.completions.create(
            model="gpt-5.6",  # হ্যাকাথনের রিকুইরমেন্ট অনুযায়ী মডেল
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        return {"status": "success", "data": response.choices[0].message.content}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))