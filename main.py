from audio.recorder import record_audio
from stt.whisper_stt import transcribe
from llm.coach import generate_guidance
from detection.question import is_question
from ui.app import InterviewUI
from ui.web_app import WebUI
from utils.logger import log

import threading
import argparse

def process_loop(ui):
    while True:
        ui.update_status("🎤 Listening...")

        audio_array = record_audio()

        ui.update_status("🧠 Transcribing...")
        text = transcribe(audio_array)
        log(f"Heard: {text}")

        if is_question(text):
            ui.update_status("🤖 Generating guidance...")
            try:
                guidance = generate_guidance(text)
                ui.update_output(f"Question detected: {text}\n\n---\n{guidance}")
            except Exception as e:
                log(f"Error generating guidance: {e}")
                ui.update_output("Error communicating with AI services.")
        else:
            ui.update_output(f"No question detected. Heard: '{text.strip()}'\n(If you spoke the triggered word but it wasn't caught, try speaking louder!)")

def main():
    parser = argparse.ArgumentParser(description="AI Interview Coach")
    parser.add_argument("--mode", choices=["desktop", "web"], default="desktop", help="Run mode")
    args = parser.parse_args()

    if args.mode == "web":
        ui = WebUI()
    else:
        ui = InterviewUI()

    thread = threading.Thread(target=process_loop, args=(ui,), daemon=True)
    thread.start()

    ui.run()

if __name__ == "__main__":
    main()
