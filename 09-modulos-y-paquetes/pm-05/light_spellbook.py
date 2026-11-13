import light_validator

def light_spell_allowed_ingredients() -> list:
    return (["earth", "air", "fire", "water"])

def light_spell_record(spell_name: str, ingredients: str) -> str:
    res, val_ingredients = light_validator.validate_ingredients(ingredients)
    if res == "VALID":
        return ("valid")
    else:
        return ("invalid")