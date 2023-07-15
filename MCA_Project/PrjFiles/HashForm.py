import hashlib
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class HashForm(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QUiLoader instance
        loader = QUiLoader()

        # Load the UI file
        ui_file = "HashForm.ui"  # Replace with the path to your UI file
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        # Create a widget from the UI file
        self.ui = loader.load(ui_file)
        ui_file.close()

        # Button Events
        self.ui.MD5_Encrypt.clicked.connect(self.encrypt_md5)
        self.ui.SHA_3.clicked.connect(self.sha3_encrypt)
        self.ui.Blake_2.clicked.connect(self.blake2_encrypt)
        self.ui.SHA_256.clicked.connect(self.sha256_encrypt)
        self.ui.Btn_Clear.clicked.connect(self.clear_text)

        # Show the widget
        self.ui.show()

    # Rest of the code...

    def encrypt_md5(self):
        text = self.ui.Encrypt_Text.toPlainText()
        if not text:
            self.show_error_dialog("Please enter text to encrypt.")
            return
        hashed_text = hashlib.md5(text.encode()).hexdigest()
        self.ui.Hash_Text.setPlainText(hashed_text)

    def sha3_encrypt(self):
        text = self.ui.Encrypt_Text.toPlainText()
        if not text:
            self.show_error_dialog("Please enter text to encrypt.")
            return
        hash_value = hashlib.sha3_256(text.encode()).hexdigest()
        self.ui.Hash_Text.setPlainText(hash_value)

    def blake2_encrypt(self):
        text = self.ui.Encrypt_Text.toPlainText()
        if not text:
            self.show_error_dialog("Please enter text to encrypt.")
            return
        hash_value = hashlib.blake2s(text.encode()).hexdigest()
        self.ui.Hash_Text.setPlainText(hash_value)

    def sha256_encrypt(self):
        text = self.ui.Encrypt_Text.toPlainText()
        if not text:
            self.show_error_dialog("Please enter text to encrypt.")
            return
        hash_value = hashlib.sha256(text.encode()).hexdigest()
        self.ui.Hash_Text.setPlainText(hash_value)

    def clear_text(self):
        self.ui.Encrypt_Text.clear()
        self.ui.Hash_Text.clear()

    def show_error_dialog(self, message):
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.setStandardButtons(QMessageBox.Ok)
        error_dialog.exec()


if __name__ == "__main__":
    app = QApplication([])
    form = HashForm()
    sys.exit(app.exec())
