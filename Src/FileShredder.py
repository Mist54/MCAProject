import os
import sys
import time

from PySide6.QtCore import QThread, Signal, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLabel, \
    QProgressBar, QMessageBox


class ShredThread(QThread):
    progress_updated = Signal(int)
    shredding_complete = Signal(str)

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.is_canceled = False

    def run(self):
        time.sleep(5)  # Delay for 10 seconds

        if os.path.isfile(self.path):
            self.shred_file(self.path)
        elif os.path.isdir(self.path):
            self.shred_folder(self.path)

        if not self.is_canceled:
            self.shredding_complete.emit(self.path)

    def shred_file(self, file_path):
        file_size = os.path.getsize(file_path)
        passes = 3  # Number of passes for secure deletion

        with open(file_path, 'rb+') as file:
            for _ in range(passes):
                if self.is_canceled:
                    return

                file.seek(0)
                random_bytes = bytearray(os.urandom(file_size))
                file.write(random_bytes)
                file.flush()
                self.progress_updated.emit(33)

        if self.is_canceled:
            return

        os.remove(file_path)
        self.progress_updated.emit(100)

    def shred_folder(self, folder_path):
        total_files = 0
        for root, dirs, files in os.walk(folder_path):
            total_files += len(files)

        processed_files = 0
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.shred_file(file_path)
                processed_files += 1
                progress = int((processed_files / total_files) * 100)
                self.progress_updated.emit(progress)

        if self.is_canceled:
            return

        os.rmdir(folder_path)
        self.progress_updated.emit(100)


class FileShredderUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Shredder")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("Select a file or folder to shred.")
        self.layout.addWidget(self.label)

        self.select_button = QPushButton("Select File or Folder")
        self.select_button.clicked.connect(self.select_file_or_folder)
        self.layout.addWidget(self.select_button)

        self.shred_button = QPushButton("Shred")
        self.shred_button.clicked.connect(self.shred_selected)
        self.shred_button.setEnabled(False)
        self.layout.addWidget(self.shred_button)

        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(True)
        self.layout.addWidget(self.progress_bar)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.thread = None
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animate_progress_bar)

    def select_file_or_folder(self):
        file_dialog = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly

        if file_dialog.exec():
            self.selected_path = file_dialog.selectedFiles()[0]
            self.label.setText(f"Selected: {self.selected_path}")
            self.shred_button.setEnabled(True)

    def shred_selected(self):
        if hasattr(self, 'selected_path'):
            reply = QMessageBox.question(
                self, "Confirmation", "Are you sure you want to shred the selected file or folder?\nThis action is irreversible.",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                self.shred_button.setEnabled(False)
                self.progress_bar.setValue(0)
                self.animation_timer.start(50)  # Start animation timer

                self.thread = ShredThread(self.selected_path)
                self.thread.progress_updated.connect(self.update_progress)
                self.thread.shredding_complete.connect(self.shredding_complete)
                self.thread.start()

    def update_progress(self, progress):
        self.progress_bar.setValue(progress)
        self.progress_bar.setFormat(f"Shredding: {progress}%")

    def shredding_complete(self, path):
        self.label.setText(f"{path} has been shredded and permanently deleted.")
        self.shred_button.setEnabled(True)
        self.animation_timer.stop()
        self.progress_bar.setValue(0)
        self.thread = None

    def animate_progress_bar(self):
        value = self.progress_bar.value()
        value += 1
        if value > 100:
            value = 0
        self.progress_bar.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileShredderUI()
    window.show()
    sys.exit(app.exec())
