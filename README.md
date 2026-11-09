<div align="center">

# 🩺 Voice-First Swasthya
### *AI-Powered Multilingual Rural Tele-Triage Assistant*

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-High--Performance-005571?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI%2FX-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Gnani AI](https://img.shields.io/badge/Powered%20by-Gnani%20AI-purple)](https://gnani.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*Bridging the rural healthcare friction gap through zero-latency, localized voice AI pipelines.*

</div>

---

## 💡 Executive Summary
In rural India, millions of citizens face severe healthcare accessibility barriers due to geographical isolation, literacy constraints, and language fragmentation. **Voice-First Swasthya** is a next-generation multilingual tele-triage assistant designed to bridge this divide. By combining high-precision regional speech recognition, clinical LLM reasoning, and native text-to-speech synthesis, the application enables patients to speak or type symptoms in their native tongue and instantly receive accurate, voice-enabled medical triage guidance.

---

## 🏗️ System Architecture & Tech Stack
### Core Technologies
* **Frontend:** Streamlit with custom glassmorphism CSS, responsive grid layouts, and dynamic audio streaming.
* **Backend:** FastAPI asynchronous microservice architecture (`/api/triage-text`).
* **AI Engine (Gnani AI):**
  * **Prisma STT:** Captures regional voice dialects with high fidelity.
  * **Evon 30B LLM:** Performs clinical safety guardrails and multi-turn triage classification.
  * **Timbre TTS:** Synthesizes human-like natural speech across Indian regional languages.

---

## 🌐 Supported Regional Dialects
* **`hi-IN`** — Hindi (हिंदी)
* **`ta-IN`** — Tamil (தமிழ்)
* **`kn-IN`** — Kannada (ಕನ್ನಡ)
* **`en-IN`** — English (India)

---

## ⚙️ Local Installation & Setup

Follow these steps to set up and run the project locally on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/kit25csebdeepikaj-spec/voice-first-swasthya.git](https://github.com/kit25csebdeepikaj-spec/voice-first-swasthya.git)
cd voice-first-swasthya