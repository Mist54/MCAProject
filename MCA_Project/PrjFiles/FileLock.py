import os
import sys
import zipfile
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog, QInputDialog, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from cryptography.fernet import Fernet, InvalidToken


class FileLock(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QUiLoader instance
        loader = QUiLoader()

        # Load the UI file
        ui_file = "FileLock.ui"  # Replace with the path to your UI file
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        # Create a widget from the UI file
        self.ui = loader.load(ui_file)
        ui_file.close()

        # Button Events
        self.ui.BtnChooseFile.clicked.connect(self.open_file)
        self.ui.BtnSubmit.clicked.connect(self.lock_file)
        self.ui.BtnExtract.clicked.connect(self.extract_file)
        self.ui.BtnClose.clicked.connect(self.clear_fields)

        # Show the widget
        self.ui.show()

    def open_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")
        self.ui.TxtChooseFile.setText(file_path)

    def lock_file(self):
        password = self.ui.TxtPassword.text()
        confirm_password = self.ui.TxtConfirmPassword.text()

        if password == confirm_password:
            file_path = self.ui.TxtChooseFile.text()
            if file_path:
                try:
                    protected_file_path = password_protect_file(file_path, password)
                    QMessageBox.information(self, "File Locked",
                                            f"File has been password protected successfully.\nProtected file: {protected_file_path}")
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Failed to lock the file: {str(e)}")
            else:
                QMessageBox.warning(self, "Error", "Please select a file.")
        else:
            QMessageBox.warning(self, "Error", "Passwords do not match.")

    def extract_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Protected File")
        if file_path:
            try:
                extracted_file_path = extract_file(file_path)
                if extracted_file_path:
                    QMessageBox.information(self, "File Extracted", "File has been successfully extracted.")
                else:
                    QMessageBox.warning(self, "Error",
                                        "Failed to extract the file. Incorrect password or missing password file.")
            except InvalidToken:
                QMessageBox.warning(self, "Incorrect Password", "The provided password is incorrect.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to extract the file: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Please select a protected file.")

    def clear_fields(self):
        self.ui.TxtChooseFile.setText("")
        self.ui.TxtPassword.setText("")
        self.ui.TxtConfirmPassword.setText("")


def prompt_password():
    password, ok = QInputDialog.getText(None, "Password", "Enter the password:", QLineEdit.Password)
    if not ok:
        raise Exception("Password entry canceled.")
    else:
        return password


def password_protect_file(file_path, password):
    file_name = os.path.basename(file_path)
    file_name_root, file_ext = os.path.splitext(file_name)
    protected_file_name = f"{file_name_root}Protected{file_ext}"
    protected_file_path = os.path.join(os.path.dirname(file_path), protected_file_name)

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    with open(file_path, 'rb') as file:
        file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)

    with open(protected_file_path, 'wb') as protected_file:
        protected_file.write(key + encrypted_data)

    password_file = os.path.join(os.path.dirname(file_path), "password.txt")
    with open(password_file, 'w') as pass_file:
        pass_file.write(password)

    return protected_file_path


def extract_file(file_path):
    password, ok = QInputDialog.getText(None, "Password", "Enter the password:", QLineEdit.Password)
    if not ok:
        raise Exception("Password entry canceled.")

    password_file = os.path.join(os.path.dirname(file_path), "password.txt")
    if not os.path.exists(password_file):
        return None

    with open(password_file, 'r') as pass_file:
        stored_password = pass_file.read().strip()

    if password == stored_password:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            key = file_data[:44]
            cipher_suite = Fernet(key)

            decrypted_data = cipher_suite.decrypt(file_data[44:])

        extracted_file_name = os.path.basename(file_path).replace('Protected', '')
        extracted_file_path = os.path.join(os.path.dirname(file_path), extracted_file_name)

        with open(extracted_file_path, 'wb') as extracted_file:
            extracted_file.write(decrypted_data)

        return extracted_file_path
    else:
        return None


if __name__ == "__main__":
    app = QApplication([])
    form = FileLock()
    sys.exit(app.exec())
