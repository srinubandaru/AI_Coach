from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
import sys

class InterviewUI:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.window = QWidget()
        self.window.setWindowTitle("AI Interview Coach")

        self.layout = QVBoxLayout()

        self.status = QLabel("Listening...")
        self.output = QLabel("Waiting for question...")
        self.output.setWordWrap(True)

        self.layout.addWidget(self.status)
        self.layout.addWidget(self.output)

        self.window.setLayout(self.layout)
        self.window.resize(600, 300)
        self.window.show()

    def update_status(self, text):
        self.status.setText(text)
        self.app.processEvents()

    def update_output(self, text):
        self.output.setText(text)
        self.app.processEvents()

    def run(self):
        self.app.exec_()
