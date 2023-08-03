import sys
import os
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTextEdit,
    QSplitter,
)
from PySide6.QtCore import Qt
import importlib.util


class ScriptLoader(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Script Loader")
        self.setMinimumSize(800, 600)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        splitter = QSplitter(self)
        layout.addWidget(splitter)

        # Left side: Load .py script button
        load_button = QPushButton("Load Script", self)
        load_button.clicked.connect(self.load_script)
        load_button.setMaximumWidth(200)
        load_button.setMinimumHeight(40)
        splitter.addWidget(load_button)

        # Right side: Display loaded script output
        self.output_text_edit = QTextEdit(self)
        self.output_text_edit.setReadOnly(True)
        splitter.addWidget(self.output_text_edit)

    # ... (previous code)

    def load_script(self):
        script_file, _ = QFileDialog.getOpenFileName(
            self, "Load Script", "", "Python Files (*.py);;All Files (*)"
        )
        if script_file:
            try:
                # Clear previous output
                self.output_text_edit.clear()

                # Load and execute the script
                spec = importlib.util.spec_from_file_location("loaded_script", script_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Redirect stdout to the QTextEdit
                import sys

                sys.stdout = self.output_text_edit

                # Call the execute_script function from the loaded script
                if hasattr(module, "execute_script"):
                    module.execute_script()

                # Restore stdout
                sys.stdout = sys.__stdout__

            except Exception as e:
                self.output_text_edit.clear()
                self.output_text_edit.append(f"Error: {e}")

    # ... (rest of the code)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScriptLoader()
    window.show()
    sys.exit(app.exec())
