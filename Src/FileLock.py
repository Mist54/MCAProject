import os
import sys
import zipfile
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QLineEdit, QInputDialog
from cryptography.fernet import InvalidToken

from Designer.FileLock import Ui_Form


class FileLockDialog(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.BtnExtract = None
        self.setupUi(self)

        # Connect the BtnChooseFile clicked signal to the open_file method
        self.BtnChooseFile.clicked.connect(self.open_file)

        # Connect the BtnSubmit clicked signal to the lock_file method
        self.BtnSubmit.clicked.connect(self.lock_file)

        # Connect the BtnExtract clicked signal to the extract_file method
        self.BtnExtract.clicked.connect(self.extract_file)

        # Connect the BtnClose clicked signal to the clear_fields method
        self.BtnClose.clicked.connect(self.clear_fields)

    def open_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")
        self.TxtChooseFile.setText(file_path)

    def lock_file(self):
        password = self.TxtPassword.text()
        confirm_password = self.TxtConfirmPassword.text()

        if password == confirm_password:
            file_path = self.TxtChooseFile.text()
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
                password = prompt_password()
                extracted_file_path = extract_file(file_path, password)
                QMessageBox.information(self, "File Extracted",
                                        "File has been successfully extracted.\n")
            except InvalidToken:
                QMessageBox.warning(self, "Incorrect Password", "The provided password is incorrect.")
            except Exception as e:
                QMessageBox.warning(self, "Error", "Failed to extract the file: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Please select a protected file.")

    def clear_fields(self):
        self.TxtChooseFile.setText("")
        self.TxtPassword.setText("")
        self.TxtConfirmPassword.setText("")


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

    with zipfile.ZipFile(protected_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.setpassword(password.encode('utf-8'))
        zip_file.write(file_path, file_name)

    return protected_file_path


def extract_file(file_path, password):
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        zip_file.setpassword(password.encode('utf-8'))
        extracted_file_path = os.path.join(os.path.dirname(file_path), "Extracted_{os.path.basename(file_path)}")
        zip_file.extractall(os.path.dirname(file_path), pwd=password.encode('utf-8'))
    return extracted_file_path


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = FileLockDialog()
    dialog.show()
    sys.exit(app.exec())
