import sys

from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

if __name__ == "__main__":
    app = QApplication([])

    # Create a QUiLoader instance
    loader = QUiLoader()

    # Load the UI file
    ui_file = "Test.ui"  # Replace with the path to your UI file
    ui_file = QFile(ui_file)
    ui_file.open(QFile.ReadOnly)

    # Create a widget from the UI file
    widget = loader.load(ui_file)
    ui_file.close()

    # Show the widget
    widget.show()

    sys.exit(app.exec())