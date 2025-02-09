from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys
from Controller.inputValidator import validateInput
from Controller.suitProcess import repairSuit, searchSuit

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.suitId = ""
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
		self.suitId = self.suitIdInput.text()
		returnBoolean, msg = validateInput(self.suitId)
		print(f"this debug message: can send to input validator =>{returnBoolean}")

		if returnBoolean:
			self.window = RepairWindow(self.suitId)
			self.window.show()
			# QMessageBox.about(self, "Suit Status", f"The Suit is in good condition.")
			print(self.suitId)
			self.suitIdInput.setText(searchSuit(self.suitId[0])[0])
		else:
			QMessageBox.about(self, "Suit Status", msg)

class RepairWindow(QWidget):
	suitId = ""
	def __init__(self, suitId):
		super().__init__()
		self.suitId = suitId
		#Create a window panel
		self.setWindowTitle("REPAIR SUIT")
		self.setGeometry(200, 200, 500, 500)

		self.layout = QVBoxLayout()

		#Create labels for the input fields
		suitInfo = searchSuit(suitId)[0]
		self.suitIdLabel = QLabel("getSuitId:" + suitInfo[0])
		self.suitTypeLabel = QLabel("getSuitType:" + suitInfo[1])
		self.suitDurabilityLabel = QLabel("getSuitDurability:" + suitInfo[2])
		self.repairButton = QPushButton("Repair Suit")
		self.repairButton.clicked.connect(self.repairButtonClicked)

		#Apply styling to the labels
		self.suitIdLabel.setStyleSheet("font-weight: bold; font-size: 14px;")
		self.suitTypeLabel.setStyleSheet("font-weight: bold; font-size: 14px;")
		self.suitDurabilityLabel.setStyleSheet("font-weight: bold; font-size: 14px;")
		self.repairButton.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; font-size: 14px; padding: 10px;")

		#Set layout
		self.layout.addWidget(self.suitIdLabel)
		self.layout.addWidget(self.suitTypeLabel)
		self.layout.addWidget(self.suitDurabilityLabel)
		self.layout.addWidget(self.repairButton)

		#Render the layout
		self.setLayout(self.layout)
		print("this debug message: render success")

	def repairButtonClicked(self):
		returnList = repairSuit(self.suitIdLabel.text()[10:])
		if not returnList:
			QMessageBox.about(self, "Suit Status", "Suit repaired successfully.")
		else:
			QMessageBox.about(self, "Suit Status", "Suit repaired unsuccessfully.")
		self.suitId = ""
		self.close()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec())