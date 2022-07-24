import data_aggregator

SKILLS_MATCH = {
    'experience': ['python', 'terraform', 'jenkins', 'ci', 'cd', 'jira', 'confluence', 'bitbucket', 'ansible'],
    'proficiency': ['linux', 'linux', 'terraform'],
    'comfortable': ['agile'],
}

TOP_KEYWORD = 'experience'
TOP_SKILL_COUNT = 9
TOP_SKILL_1 = 'linux'
TOP_SKILL_2 = 'terraform'
TOP_SKILL_1_COUNT = 2
TOP_SKILL_2_COUNT = 2

def test_get_top_keyword():
    assert data_aggregator.get_top_keyword(SKILLS_MATCH) == (TOP_KEYWORD, TOP_SKILL_COUNT)

def test_get_top_skill():
    assert data_aggregator.get_top_skill(SKILLS_MATCH) == [(TOP_SKILL_1, TOP_SKILL_1_COUNT), (TOP_SKILL_2, TOP_SKILL_2_COUNT)]