from View.app import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()