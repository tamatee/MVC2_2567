import csv

csvPath = "Model/database_hero_suit.csv"

def parseCsv():
	with open(csvPath, mode='r', encoding='utf-8') as file:
		csvReader = csv.reader(file)
		data = []
		next(csvReader)  # Skip the first row
		for row in csvReader:
			data.append(row)
		return data

def searchSuit(suitId):
    data = parseCsv()  # Get the data from the CSV file

    for row in data:
        if row[0] == suitId:  # Check if the cow_id matches
            print(f"Hit: here your suit{row}")
            return False

def repairDuraStatus(suitId):
	data = parseCsv()
	for row in data:
		if row[0] == suitId:
			row[2] = min(row[2] + 25, 100)
			break
	return True