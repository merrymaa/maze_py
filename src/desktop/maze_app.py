import sys

from PySide6.QtWidgets import QApplication

from desktop.mainWindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
