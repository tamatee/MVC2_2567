from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys
from Controller.inputValidator import validateInput
from Controller.csvParser import parse_csv
from Controller.milkProcess import milkCow

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Miking Cow")
		self.setGeometry(200, 200, 600, 400)

		self.layout = QVBoxLayout()

		self.cowIdLabel = QLabel("Enter Cow ID:")
		self.cowAgeLabel = QLabel("Enter Cow Age:")
		self.cowNomLabel = QLabel("Enter Cow Nom:")

		self.cowIdInput = QLineEdit()
		self.cowAgeInput = QLineEdit()
		self.cowNomInput = QLineEdit()

		# submit button
		self.submitButton = QPushButton("Submit")
		self.submitButton.clicked.connect(self.submitButtonClicked)

		# Apply styling to the labels
		self.cowIdLabel.setStyleSheet("font-weight: bold; font-size: 14px;")
		self.cowAgeLabel.setStyleSheet("font-weight: bold; font-size: 14px;")
		self.cowNomLabel.setStyleSheet("font-weight: bold; font-size: 14px;")

		# Apply styling to the input fields
		self.cowIdInput.setStyleSheet("font-size: 14px; height: 30px;")
		self.cowAgeInput.setStyleSheet("font-size: 14px; height: 30px;")
		self.cowNomInput.setStyleSheet("font-size: 14px; height: 30px;")

		# Apply styling to the submit button
		self.submitButton.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; font-size: 14px; padding: 10px;")

		self.layout.addWidget(self.cowIdLabel)
		self.layout.addWidget(self.cowIdInput)
		self.layout.addWidget(self.cowAgeLabel)
		self.layout.addWidget(self.cowAgeInput)

		self.layout.addWidget(self.cowNomLabel)
		self.layout.addWidget(self.cowNomInput)

		self.layout.addWidget(self.submitButton)

		self.setLayout(self.layout)

	def submitButtonClicked(self):
		cowId = self.cowIdInput.text()
		cowAge = self.cowAgeInput.text()
		cowNom = self.cowNomInput.text()

		isValid, msg = validateInput(cowId, cowAge, cowNom)
		if isValid:
			state = milkCow(cowId, cowAge, cowNom)
			QMessageBox.about(self, "Milking Status", f"The Cow is Milked.")
		else:
			print(msg)

		# Print the data from the CSV file (ไม่เกี่ยวกับโจทย์)
		data = parse_csv()
		print(data)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())