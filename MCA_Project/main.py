import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow, QVBoxLayout, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
import subprocess


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hashform Launcher")
        self.setGeometry(100, 100, 300, 100)

        layout = QVBoxLayout()
        button = QPushButton("Open Hashform.py")
        button.clicked.connect(self.open_hashform)

        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_hashform(self):
        # Provide the path to the Hashform.py file
        file_path = "MCA_Project/PrjFiles/HashForm.py"

        if os.path.exists(file_path):
            try:
                subprocess.Popen([sys.executable, file_path])
            except Exception as e:
                print(f"Error opening Hashform.py: {e}")
        else:
            print(f"Error: {file_path} not found!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
