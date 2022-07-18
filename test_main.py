import main

FILE = open('job-role-requirements.txt','r')
LINE = 'DO NOT DELETE - Experience in PYTEST'
LINE_WITH_SYMBOLS = 'DO NOT DELETE - Experience in pytest/unittest'

TEST_KEYWORDS = ['experience', 'fundamental', 'skills']
TEST_SKILLS = ['golang', 'pytest', 'cookies']

KEYWORD = 'experience'
SKILL = 'pytest'

def test_get_first_line():
    assert main.get_first_line(FILE) == LINE

def test_get_keywords_and_skills_from_line():
    assert main.get_keywords_and_skills_from_line(LINE, TEST_KEYWORDS, TEST_SKILLS)[KEYWORD][0] == SKILL

def test_get_keywords_and_skills_from_line_with_symbols():
    assert main.get_keywords_and_skills_from_line(LINE_WITH_SYMBOLS, TEST_KEYWORDS, TEST_SKILLS)[KEYWORD][0] == SKILL

