import hashlib
import sys
import zlib

from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox

from Designer.FileHasher import Ui_Form


class FileHasherApp(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.BtnFile.clicked.connect(self.choose_file)
        self.ui.BtSubmit.clicked.connect(self.calculate_hashes)
        self.ui.BtnClear.clicked.connect(self.Clear_Text)

    # choosing file from GUI
    def choose_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Choose File")
        self.ui.File_Path.setText(file_path)

    def calculate_hashes(self):
        file_path = self.ui.File_Path.text()
        if not file_path:
            self.show_error_dialog("Please choose a file.")
            return

        try:
            with open(file_path, "rb") as file:
                data = file.read()
            # Different hash for calculation
            md5_hash = hashlib.md5(data).hexdigest()
            sha256_hash = hashlib.sha256(data).hexdigest()
            blake2_hash = hashlib.blake2b(data).hexdigest()
            sha3_hash = hashlib.sha3_256(data).hexdigest()
            sha512_hash = hashlib.sha512(data).hexdigest()
            sha1_hash = hashlib.sha1(data).hexdigest()
            crc32_checksum = zlib.crc32(data)  # Calculate CRC32 checksum using zlib
            crc32_hash = f"{crc32_checksum & 0xffffffff:08x}"  # Convert checksum to hexadecimal CRC32 hash

            self.ui.lineEdit_3.setText(md5_hash)
            self.ui.lineEdit_4.setText(sha256_hash)
            self.ui.lineEdit_5.setText(blake2_hash)
            self.ui.lineEdit_6.setText(sha3_hash)
            self.ui.lineEdit.setText(sha512_hash)
            self.ui.lineEdit_2.setText(crc32_hash)
            self.ui.lineEdit_7.setText(sha1_hash)
        except IOError:
            self.show_error_dialog("Error reading the file.")

    def show_error_dialog(self, message):
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.setStandardButtons(QMessageBox.Ok)
        error_dialog.exec()

    def Clear_Text(self):
        self.ui.File_Path.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileHasherApp()
    window.show()
    sys.exit(app.exec())
