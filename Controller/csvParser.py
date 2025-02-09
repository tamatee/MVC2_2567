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

def writeCsv(data):
    with open(csvPath, mode='w', encoding='utf-8', newline='') as file:
        csvWriter = csv.writer(file)
        
        # Header of the CSV (ปรับตามจริงหากมี)
        csvWriter.writerow(["Suit ID", "Status", "Durability"])
        
        # Write modified data rows
        csvWriter.writerows(data)

def repairDuraStatus(suitId):
    data = parseCsv()
    updated = False
    
    for row in data:
        if row[0] == suitId:
            row[2] = str(min(int(row[2]) + 25, 100))
            updated = True
            break

    if updated:
        writeCsv(data)
        return True
    return False

def searchSuit(suitId):
    data = parseCsv()  # Get the data from the CSV file

    for row in data:
        if row[0] == suitId:
            # Return a copy to prevent unintended modifications
            return row.copy() 