import light_spellbook

def validate_ingredients(ingredients: str) -> tuple[str, str]:
    low_ingredients = ingredients.lower()
    for i in light_spellbook.light_spell_allowed_ingredients():
        if i in low_ingredients:
            return ("VALID", ingredients)
    return ("INVALID", ingredients)