# AI Interview Coach

An AI-powered, real-time interview coach that secretly listens to your interviews, transcribes them using OpenAI's Whisper, and directly provides concise behavioral and technical guidance via GPT-4o.

## Two Modes
You can run the application either as a pure minimalist Desktop UI or as a stunning, modern Server Web App:

1. **Desktop Mode:** `python main.py --mode desktop`
2. **Web Mode:** `python main.py --mode web` (Then open http://127.0.0.1:5000)

## System Requirements
Because the system runs Whisper locally to bypass OS constraints, you only require standard Python.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running
Make sure your OpenAI API key is exported:
```bash
export OPENAI_API_KEY="sk-..."
python main.py
```
