from cmath import sin
from os import environ
import sys

import data_generator
        
def main():
    with open(sys.argv[1], 'r') as arg1, open(sys.argv[2], 'r') as arg2, open(sys.argv[3], 'r') as arg3:
        requirements = arg1.read().splitlines()
        keywords = arg2.read().splitlines()
        skills= arg3.read().splitlines()

        single_data_store = dict()
        for line in requirements:
            matches = data_generator.get_keywords_and_skills_from_line(line, keywords, skills)

            for k, s in matches.items():

                if len(s) > 0:
                    if k in single_data_store.keys():
                        single_data_store[k] + s

                    else:
                        single_data_store[k] = s

        print(single_data_store)

if __name__ == '__main__':
    main()
