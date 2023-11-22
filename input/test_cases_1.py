# test_cases_1.py

test_cases_1 = [
        # TODO - check tests' comments

        # Test case 1: Basic test with a simple pattern.
        ("abcdefg", "cd"),

        # Test case 2: Multiple non-overlapping occurrences.
        ("xyxyxy", "xy"),

        # Test case 3: Overlapping pattern.
        ("bababababa", "aba"),

        # Test case 4: Pattern at the beginning of the text.
        ("racecar", "race"),

        # Test case 5: Pattern at the end of the text.
        ("moonlight", "light"),

        # Test case 6: Pattern repeated in the text.
        ("patternpattern", "pattern"),

        # Test case 7: Numeric text with pattern.
        ("0123456789012345", "2345"),

        # Test case 8: Pattern of words.
        ("treefrogstreefrogs", "treefrogs"),

        # Test case 9: Palindromic pattern.
        ("abcdeedcba", "deed"),

        # Test case 10: Pattern not in text.
        ("thisisaverylongtextwithnopattern", "pattern"),

        # Test case 11: Short pattern repeated.
        ("abcdefabcdef", "abcdef"),

        # Test case 12: Repeating pattern.
        ("ababababababababababab", "abab"),

        # Test case 13: Pattern not in the text.
        ("abcdefghi", "ijk"),

        # Test case 14: Pattern at the middle of the text.
        ("pythonisfun", "is"),

        # Test case 15: Empty text.
        ("", "pattern"),

        # Test case 16: Long pattern.
        ("z" * 100, "z" * 10),

        # Test case 17: Pattern of vowels.
        ("abcdefghijklmnopqrstuwxyz", "aeiou"),

        # Test case 18: Digits pattern.
        ("124578915", "69"),

        # Test case 19: No match.
        ("one", "two"),

        # Test case 20: Lorem Ipsum text.
        ("loremipsumdolorsitamet", "ipsumdolor"),
    ]