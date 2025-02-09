from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys
from Controller.inputValidator import validateInput
from Controller.suitProcess import repairSuit

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		#Create a window panel
		self.setWindowTitle("Hero Suit Health Check")
		self.setGeometry(200, 200, 600, 400)

		self.layout = QVBoxLayout()

		#Create labels for the input fields
		self.suitIdLabel = QLabel("Enter Suit ID:")
		self.suitIdInput = QLineEdit()
		self.confirmButton = QPushButton("Confirm")
		self.confirmButton.clicked.connect(self.confirmButtonClicked)


		#Apply styling to the labels
		self.suitIdLabel.setStyleSheet("font-weight: bold; font-size: 14px;")
		self.suitIdInput.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; font-size: 14px; padding: 10px;")
		self.confirmButton.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; font-size: 14px; padding: 10px;")

		#Set layout
		self.layout.addWidget(self.suitIdLabel)
		self.layout.addWidget(self.suitIdInput)
		self.layout.addWidget(self.confirmButton)

		#Render the layout
		self.setLayout(self.layout)
		print("this debug message: render success")

	def confirmButtonClicked(self):
		suitId = self.suitIdInput.text()
		returnBoolean, msg = validateInput(suitId)
		print(f"this debug message: can send to input validator =>{returnBoolean}")

		if returnBoolean:
			self.window = RepairWindow()
			self.window.show()
			QMessageBox.about(self, "Suit Status", f"The Suit is in good condition.")
		else:
			QMessageBox.about(self, "Suit Status", msg)

class RepairWindow(QWidget):
	def __init__(self):
		super().__init__()
		#Create a window panel
		self.setWindowTitle("REPAIR SUIT")
		self.setGeometry(200, 200, 200, 200)

		self.layout = QVBoxLayout()

		#Create labels for the input fields
		self.suitIdLabel = QLabel("Enter Suit ID:")

	def confirmButtonClicked(self):
		suitId = self.suitIdInput.text()
		returnBoolean, msg = validateInput(suitId)
		print(f"this debug message: can send to input validator =>{returnBoolean}")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec())