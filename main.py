from cmath import sin
from os import environ
import sys

import data_generator
import data_aggregator
        
def main():
    with open(sys.argv[1], 'r') as arg1, open(sys.argv[2], 'r') as arg2, open(sys.argv[3], 'r') as arg3:
        requirements = arg1.read().splitlines()
        keywords = arg2.read().splitlines()
        skills= arg3.read().splitlines()

        keyword_skills = dict()
        for line in requirements:
            matches = data_generator.get_keywords_and_skills_from_line(line, keywords, skills)

            for k, s in matches.items():

                if len(s) > 0:
                    if k in keyword_skills.keys():
                        keyword_skills[k] + s

                    else:
                        keyword_skills[k] = s

        # return some stats
        top = data_aggregator.get_top_keyword(keyword_skills=keyword_skills)
        print(f"The top keyword is '{top[0]}' with {top[1]} skills.")

if __name__ == '__main__':
    main()
