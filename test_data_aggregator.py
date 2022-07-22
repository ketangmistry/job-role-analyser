import data_aggregator

SKILLS_MATCH = {
    'experience': ['python', 'terraform', 'jenkins', 'ci', 'cd', 'jira', 'confluence', 'bitbucket', 'ansible'],
    'proficiency': ['linux', 'linux'],
    'comfortable': ['agile'],
    'experience': ['terraform', 'ansible'],
}

def test_get_stats_from_skills_match():
    assert data_aggregator.get_stats_from_skills_match(SKILLS_MATCH) == []