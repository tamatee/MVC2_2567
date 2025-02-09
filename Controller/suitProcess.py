import Controller.csvParser as cp
import Model.suit as suit

def searchSuit(suitId):
    if cp.searchSuit(suitId) == None:
        return None, "Suit not found"
    return cp.searchSuit(suitId), "Suit repair Successful"

def repairSuit(suitId):
    cp.repairDuraStatus(suitId)