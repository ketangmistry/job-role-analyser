

def get_top_keyword(keyword_skills: dict) -> tuple:
    """Gets the top keyword and associated skills count

    Args:
        keyword_skills (dict): keywords and list of associated skills

    Returns:
        tuple: top keyword and its skills count
    """
    top: str
    count = 0

    for k, v in keyword_skills.items():
        if len(v) > count:
            count = len(v)
            top = k
    
    return (top,count)

def get_top_skill(keyword_skills: dict) -> list:
    skills = dict()

    for k, v in keyword_skills.items():
        # TODO: need to add skills and increment counts when iterating
        pass