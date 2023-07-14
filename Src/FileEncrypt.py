import os
import sys

from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from cryptography.fernet import Fernet

from Designer.FileEncrypt import Ui_Form


def generate_random_key():
    """Generates a random 32-byte key for encryption"""
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    return key


class FileEncryptApp(QDialog):
    def __init__(self):
        super(FileEncryptApp, self).__init__()

        # Set up the user interface from the Designer file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Connect the button click events to functions
        self.ui.BtnChooseFile.clicked.connect(self.choose_file)
        self.ui.BtnSaveFile.clicked.connect(self.choose_save_folder)
        self.ui.BtnEncrypt.clicked.connect(self.encrypt_file)
        self.ui.BtnDecrypt.clicked.connect(self.decrypt_file)
        self.ui.BtnClear.clicked.connect(self.clear_fields)

    def choose_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_paths, _ = file_dialog.getOpenFileNames(self, "Choose file(s)")

        if file_paths:
            # Update the QLineEdit with the selected file path
            self.ui.FileSelect.setText(file_paths[0])

    def choose_save_folder(self):
        save_folder = QFileDialog.getExistingDirectory(self, "Choose a folder to save the file")

        if save_folder:
            # Update the QLineEdit with the selected folder path
            self.ui.FileSave.setText(save_folder)

    def encrypt_file(self):
        file_path = self.ui.FileSelect.text()
        save_folder = self.ui.FileSave.text()

        if not file_path or not save_folder:
            QMessageBox.warning(self, "Encryption Error", "Please choose a file and a save folder.")
            return

        # Generate a random 32-byte key for encryption
        key = generate_random_key()
        self.ui.HashKey.setText(key.decode())
        fernet = Fernet(key)

        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()

            encrypted_data = fernet.encrypt(file_data)

            # Get the file name from the original file path
            file_name = os.path.basename(file_path)

            # Create the save file path using the selected folder and original file name
            save_path = os.path.join(save_folder, file_name + '.enc')

            with open(save_path, 'wb') as file:
                file.write(encrypted_data)

            QMessageBox.information(self, "Encryption Successful", "File encrypted and saved successfully.")
        except FileNotFoundError:
            QMessageBox.critical(self, "Encryption Error", "File not found.")
        except PermissionError:
            QMessageBox.critical(self, "Encryption Error", "Permission denied. Please check file access permissions.")
        except Exception as e:
            QMessageBox.critical(self, "Encryption Error", f"An error occurred while encrypting the file:\n{str(e)}")

    def decrypt_file(self):
        file_path = self.ui.FileSelect.text()
        save_folder = self.ui.FileSave.text()
        key = self.ui.HashKey.text().encode()

        if not file_path or not save_folder:
            QMessageBox.warning(self, "Decryption Error", "Please choose a file and a save folder.")
            return

        if not key:
            QMessageBox.warning(self, "Decryption Error", "Please enter a valid decryption key.")
            return

        try:
            fernet = Fernet(key)

            with open(file_path, 'rb') as file:
                file_data = file.read()

            decrypted_data = fernet.decrypt(file_data)

            # Get the original file name from the encrypted file path
            file_name = os.path.splitext(os.path.basename(file_path))[0]

            # Create the save file path using the selected folder and original file name
            save_path = os.path.join(save_folder, file_name)

            with open(save_path, 'wb') as file:
                file.write(decrypted_data)

            QMessageBox.information(self, "Decryption Successful", "File decrypted and saved successfully.")
        except FileNotFoundError:
            QMessageBox.critical(self, "Decryption Error", "File not found.")
        except PermissionError:
            QMessageBox.critical(self, "Decryption Error", "Permission denied. Please check file access permissions.")
        except Exception as e:
            QMessageBox.critical(self, "Decryption Error", f"An error occurred while decrypting the file:\n{str(e)}")

    def clear_fields(self):
        # Clear the file selection, save folder, and hash key fields
        self.ui.FileSelect.clear()
        self.ui.FileSave.clear()
        self.ui.HashKey.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = FileEncryptApp()
    window.show()

    sys.exit(app.exec())
