import Controller.csvParser as cp
import Model.suit as suit

def validateInput(suit_id):
    try:
        # Basic input checks
        if not suit_id:
            return False, "Suit ID cannot be empty"

        if not isinstance(suit_id, str):
            return False, "Suit ID must be a string"

        # Create suit object and validate using model's logic
        suit_obj = suit.Suit(suit_id)
        if suit_obj.isValidId():
            return True, "Valid Suit ID"
        else:
            return False, "Invalid Suit ID format. ID must be 6 characters long and not start with 0"

    except Exception as e:
        return False, f"Validation error: {str(e)}"