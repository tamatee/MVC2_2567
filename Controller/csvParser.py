import csv

csv_path = "Model/database.csv"
csv_mont_path = "Model/mont.csv"

def parse_csv():
	with open(csv_path, mode='r') as file:
		csv_reader = csv.reader(file)
		data = []
		next(csv_reader)  # Skip the first row
		for row in csv_reader:
			data.append(row)
		return data

def parse_mont_csv():
	with open(csv_mont_path, mode='r') as file:
		csv_reader = csv.reader(file)
		data = []
		next(csv_reader)  # Skip the first row
		for row in csv_reader:
			data.append(row)
		return data

def search_cow(cow_id):
    data = parse_csv()  # Get the data from the CSV file

    for row in data:
        if row[0] == cow_id:  # Check if the cow_id matches
            if row[4].split(" ")[1] == "Goat":  # Check if the species is a goat in column 5
                print("Hit: This is a goat!")
                return False
            else :
                print("Hit: This is a cow!")
                return True

def edit_status_Milked(cow_id):
	data = parse_csv()
	for row in data:
		if row[0] == cow_id:
			row[5] = "Milked"
			break
	return True

def send_to_Mont(cow_id):
	data = parse_csv()
	data_mont = parse_mont_csv()
	for row in data:
		if row[0] == cow_id:
			csv.writer(data_mont, row)
			row = ""
			break
	return True