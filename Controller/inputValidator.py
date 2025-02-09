import Controller.csvParser as cp

# รหัสพนักงานต้องเป็นตัวเลข 8 หลัก และไม่ขึ้นต้นด้วย 0
def isValidId(id):
    print(id)
    print(len(id))
    print(not id.startswith('0'))
    return len(id) == 8 and not (id.startswith('0'))

# วัวต้องมีอายุ 1-10 ปี
def isValidAge(age):
    try:
        regex = age.split('y')
        regex2 = regex[1].split('m')
    except:
        return False
    return regex[0].isdigit() and 1 <= int(regex[0]) <= 10 and 1 <= int(regex2[0]) <= 12
# วัวต้องมีเต้านม 4 เต้านม
def isValidNom(nom):
    return nom == 4

# วัวตัวนั้นต้องไม่ใช่แพะ
def isValidSpicie(id):
    # เรียกจาก csvParser.py หากเป็น Goat จะ return False
    a = cp.search_cow(id)
    return a

def validateInput(cowId, cowAge, cowNom):
    isValid = True
    msg = ""

    if not isValidId(cowId):
        isValid = False
        msg = "Invalid Cow Id. Please enter a valid Cow ID."

    if not isValidSpicie(cowId):
        isValid = False
        msg = "Invalid Specie. Please enter a Cow, not a Goat."

    if not isValidAge(cowAge):
        isValid = False
        msg = "Invalid Cow Age. Please enter a valid Cow Age (1-10 years)."

    if not isValidNom(cowNom):
        isValid = False
        msg = "Invalid Nom Cnt. Please enter a valid Nom Cnt (4 Nom)."

    return isValid, msg
