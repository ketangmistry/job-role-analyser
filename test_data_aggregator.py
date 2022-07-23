import data_aggregator

SKILLS_MATCH = {
    'experience': ['python', 'terraform', 'jenkins', 'ci', 'cd', 'jira', 'confluence', 'bitbucket', 'ansible'],
    'proficiency': ['linux', 'linux'],
    'comfortable': ['agile'],
}

TOP_KEYWORD = 'experience'

def test_get_top_keyword():
    assert data_aggregator.get_top_keyword(SKILLS_MATCH) == TOP_KEYWORD