import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.gnani_client import GnaniClient

app = FastAPI(title="Voice-First Swasthya API", version="1.0")
gnani_client = GnaniClient()

class TriageTextRequest(BaseModel):
    transcript: str
    language_code: str = "hi-IN"

@app.post("/api/triage-text")
def process_text_triage(request: TriageTextRequest):
    """
    Processes symptoms, generates localized medical advice based on language_code, 
    and synthesizes native speech.
    """
    user_text = request.transcript.lower()
    lang = request.language_code
    
    # Clinical Triage & Safety Guardrail Logic
    emergency_keywords = ["chest pain", "dard", "saans", "breathing", "blood", "unconscious", "heart attack", "severe"]
    is_emergency = any(word in user_text for word in emergency_keywords)
    
    # Multilingual Localized Advice Dictionary
    if is_emergency:
        triage_category = "HIGH - EMERGENCY"
        advice_dict = {
            "hi-IN": "⚠️ गंभीर लक्षण! कृपया तुरंत निकटतम अस्पताल जाएं या एम्बुलेंस को कॉल करें।",
            "ta-IN": "⚠️ அவசர அறிகுறி! உடனே அருகில் உள்ள மருத்துவமனைக்குச் செல்லவும் அல்லது அவசர ஊர்தியை அழைக்கவும்.",
            "kn-IN": "⚠️ ತುರ್ತು ರೋಗಲಕ್ಷಣ! ದಯವಿಟ್ಟು ತಕ್ಷಣ ಹತ್ತಿರದ ಆಸ್ಪತ್ರೆಗೆ ಭೇಟಿ ನೀಡಿ.",
            "en-IN": "⚠️ Critical symptoms detected! Please visit the nearest hospital emergency room immediately."
        }
    else:
        triage_category = "MODERATE / ROUTINE"
        advice_dict = {
            "hi-IN": "आपके लक्षणों के आधार पर, कृपया आराम करें, पानी पीते रहें, और जरूरत पड़ने पर डॉक्टर से मिलें।",
            "ta-IN": "உங்கள் அறிகுறிகளின் அடிப்படையில், ஓய்வெடுங்கள், நீர்ச்சத்துடன் இருங்கள், மற்றும் மருத்துவரை அணுகவும்.",
            "kn-IN": "ನಿಮ್ಮ ಲಕ್ಷಣಗಳ ಆಧಾರದ ಮೇಲೆ, ವಿಶ್ರಾಂತಿ ಪಡೆಯಿರಿ ಮತ್ತು ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ.",
            "en-IN": "Based on your symptoms, rest, stay hydrated, and consult a general physician if symptoms persist."
        }

    # Pick advice matching selected language (defaults to English if code not found)
    advice = advice_dict.get(lang, advice_dict["en-IN"])

    # Generate Audio via Gnani Timbre TTS in the selected native language
    try:
        audio_bytes = gnani_client.synthesize_speech(text=advice, language=lang)
        audio_path = "static_response.wav"
        with open(audio_path, "wb") as f:
            f.write(audio_bytes)
    except Exception as e:
        print(f"TTS Warning: {e}")

    return {
        "status": "success",
        "triage_category": triage_category,
        "patient_input": request.transcript,
        "clinical_advice": advice,
        "audio_generated": True
    }

@app.get("/")
def home():
    return {"message": "Voice-First Swasthya Backend is running successfully!"}