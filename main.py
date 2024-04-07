# QR Code Generator
# Author: S. Chu
# Date: 2024-04-07
# Reference: https://pypi.org/project/qrcode/

import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog
import qrcode

class QRCodeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100, 100, 200, 200)

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.text_input = QLineEdit()
        self.generate_button = QPushButton("Generate QR Code")
        self.generate_button.clicked.connect(self.generate_qr_code)
        self.save_button = QPushButton("Save QR Code")
        self.save_button.clicked.connect(self.save_qr_code)
        self.qr_code_label = QLabel()

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Text:"))
        input_layout.addWidget(self.text_input)

        self.layout.addLayout(input_layout)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.qr_code_label)
        self.layout.addWidget(self.save_button)

    def generate_qr_code(self):
        text = self.text_input.text()
        if text:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)

            self.qr_pixmap = qr.make_image(fill_color="black", back_color="white").toqpixmap()
            self.qr_code_label.setPixmap(self.qr_pixmap.scaled(200, 200))

    def save_qr_code(self):
        if hasattr(self, 'qr_pixmap'):
            file_name, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "Images (*.png *.jpg)")
            if file_name:
                self.qr_pixmap.save(file_name, format='PNG')

def main():
    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
