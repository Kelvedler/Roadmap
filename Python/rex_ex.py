import re

patterns = ['term1', 'term2']

text = 'This is the string with term1, but not the other'
split_term = '@'
email = 'user@gmail.com'

match = re.search(patterns[0], text)
split = re.split(split_term, email)
match_all = re.findall('match', 'test phrase match in middle match')
test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'
test_pattern = [r'\W+']


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print('Searching for pattern {}'.format(pat))
        print(re.findall(pat, phrase))
        print('\n')


print(match.start())
print(split)
print(match_all)
print(multi_re_find(test_pattern, test_phrase))
