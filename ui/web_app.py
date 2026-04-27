from flask import Flask, render_template, jsonify
import sys
import logging

# Disable default flask logging to keep terminal clean
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class WebUI:
    def __init__(self):
        self.status_text = "Listening..."
        self.output_text = "Waiting for question..."
        self.app = Flask(__name__, template_folder='templates')
        
        @self.app.route('/')
        def index():
            return render_template('index.html')
            
        @self.app.route('/state')
        def state():
            return jsonify({
                "status": self.status_text,
                "output": self.output_text.replace('\n', '<br>')
            })

    def update_status(self, text):
        self.status_text = text

    def update_output(self, text):
        self.output_text = text

    def run(self):
        print("\n\n" + "="*50)
        print("🚀 WEB MODE ACTIVE 🚀")
        print("Navigate to http://127.0.0.1:5000 in your browser.")
        print("="*50 + "\n\n")
        self.app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
