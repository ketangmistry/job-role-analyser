import main

FILE = open('job-role-requirements.txt','r')
LINE = 'DO NOT DELETE - EXPERIENCE IN PYTEST'

SKILLS = ['golang', 'pytest', 'cookies']
KEYWORDS = ['experience', 'fundamental', 'skills']

KEY = 'experience'
VALUE = 'pytest'

def test_get_first_line():
    assert main.get_first_line(FILE) == LINE

def test_get_keywords_and_skills_from_line():
    assert main.get_keywords_and_skills_from_line(LINE, SKILLS, KEYWORDS)[KEY][0] == VALUE

