import main

FILE = open('job-role-requirements.txt','r')
LINE = 'DO NOT DELETE - Experience in PYTEST'
LINE_WITH_SYMBOLS = 'DO NOT DELETE - Experience in pytest/unittest'
LINE_WITH_MULTI_WORD_SKILL = 'DO NOT DELETE - Experience in code reviews'

TEST_KEYWORDS = ['experience', 'fundamental', 'skills']
TEST_SKILLS = ['golang', 'pytest', 'cookies']
TEST_MULTI_WORD_SKILL = ['python', 'code reviews', 'sdlc', 'helm', 'opsgenie']

KEYWORD = 'experience'
SKILL = 'pytest'
MULTI_WORD_SKILL = 'code reviews'

def test_get_first_line():
    assert main.get_first_line(FILE) == LINE

def test_get_keywords_and_skills_from_line():
    assert main.get_keywords_and_skills_from_line(LINE, TEST_KEYWORDS, TEST_SKILLS)[KEYWORD][0] == SKILL

def test_get_keywords_and_skills_from_line_with_symbols():
    assert main.get_keywords_and_skills_from_line(LINE_WITH_SYMBOLS, TEST_KEYWORDS, TEST_SKILLS)[KEYWORD][0] == SKILL

def test_get_keywords_and_multi_word_skills():
    assert main.get_keywords_and_skills_from_line(LINE_WITH_MULTI_WORD_SKILL, TEST_KEYWORDS, TEST_MULTI_WORD_SKILL)[KEYWORD][0] == MULTI_WORD_SKILL

