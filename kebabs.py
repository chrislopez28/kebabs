import re


def kebab_case(s: str) -> str:
    punctuation_pattern = re.compile(r'[?!.,\'\"]')
    capitals_pattern = re.compile(r'(?<!^)(?=[A-Z])')
    underscore_pattern = re.compile(r'_')
    multispace_pattern = re.compile(r'\s+')
    spaces_pattern = re.compile(r' ')

    s = punctuation_pattern.sub('', s)
    s = capitals_pattern.sub(' ', s)
    s = underscore_pattern.sub(' ', s)
    s = multispace_pattern.sub(' ', s)
    s = spaces_pattern.sub('-', s).lower()
    return s


def main():
    print(kebab_case("The best of times              and the worst of times"))
    print(kebab_case("theBestOfTimes"))
    print(kebab_case("theBestOfTimes? It's steve's"))


if __name__ == '__main__':
    main()
