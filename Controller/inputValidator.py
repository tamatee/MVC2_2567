import Controller.csvParser as cp

# รหัสพนักงานต้องเป็นตัวเลข 8 หลัก และไม่ขึ้นต้นด้วย 0
def isValidId(id):
    print(id)
    print(len(id))
    print(not id.startswith('0'))
    return len(id) == 6 and not (id.startswith('0'))

def validateInput(suitId):
    isValid = True
    msg = ""
    print("Input Validation")
    if not isValidId(suitId):
        isValid = False
        msg = "Invalid Suit Id. Please enter a valid Suit ID."

    return isValid, msg
