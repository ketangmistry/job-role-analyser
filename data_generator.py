from io import FileIO

def get_first_line(file: FileIO) -> str:
    """Used for pytest as  controlled test

    Args:
        file (FileIO): file name with a list of job role requirement

    Returns:
        str: the first line from the job role requirement fole
    """
    return file.read().splitlines()[0]

def get_keywords_and_skills_from_line(line: str, keywords: list, skills: list) -> dict:
    """Correlates keywords and skills in a single job role requirement line

    Args:
        line (str): a single job description line
        keywords (list): a list of keywords you typically see in a job role requirement e.g. experience, demonstrates
        skills (list): a list of skills that I have

    Returns:
        dict: where a match occurs between keywords and skills
    """
    w = line.lower().replace('/', ' ').replace('(', ' ').replace(')', ' ').replace(',', '').split(' ')
    m = dict()

    if keywords is not None or skills is not None:
        for k in keywords:

            if k in w:
                # easy single word skills
                w = [skill in w for skill in skills]
                m[k] = [x for x, y in zip(skills, w) if y]

                # suport for multiple word skills 
                for skill in skills:
                    if len(skill.split(' ')) >= 2 and skill in line:
                        if k in m.keys():
                            m[k].append(skill)
                        else:
                            m[k] = [skill]

    return m