# test_cases_2.py

test_cases_2 = [
        # TODO - check tests' comments

        # Test case 1: Pattern at the beginning of the text.
        ("patternabacabac", "pattern"),

        # Test case 2: Pattern at the end of the text.
        ("abacabacpattern", "pattern"),

        # Test case 3: Alternating pattern and text.
        ("abacababacabacababacab", "abacab"),

        # Test case 4: Unbalanced text.
        ("abababababababababababababababab", "abababababab"),

        # Test case 5: Large text with pattern at the end.
        ("a" * 1000000 + "b" * 5000, "b" * 5000),

        # Test case 6: Large text with complex pattern.
        ("a" * 1000000 + "ab" * 25000 + "a" * 1000000, "ab" * 25000),

        # Test case 7: Large text with a simpler pattern.
        ("ab" * 1000000, "abab"),

        # Test case 8: No pattern in the text.
        ("abcdefghijklmnopqrstuvwxyz", "12345"),

        # Test case 9: Pattern occurs multiple times.
        ("abcabcabcabcabc", "abc"),

        # Test case 10: Long text with a randomized complex pattern.
        ("abcdefghijklmnopqrstuwxyz" * 20000, "pqrs" * 5000 + "uvwxyz" * 5000),

        # Test case 11: Long text with an alternating pattern.
        ("0101010101" * 100000, "01" * 50000),

        # Test case 12: Long text with an overlapping pattern.
        ("abcdefgh" * 50000, "abcd" * 25000),

        # Test case 13: Long text with a complex pattern.
        ("a1b2c3d4e5f6g7h8i9j0" * 5000, "12345" * 1000 + "j0" * 1000),

        # Test case 14: Long text with a complex pattern.
        ("!@#$%^&*()_+=" * 25000, "!@#$" * 5000),

        # Test case 15: Long text with a repeating pattern.
        ("abcdefgh" * 100000, "abcdefgh" * 50000),

        # Test case 16: Large text with a randomized complex pattern.
        ("0123456789" * 200000, "56789" * 40000 + "23456" * 40000),

        # Test case 17: Large text with pattern at the end.
        ("a" * 1000000 + "b" * 5000, "b" * 5000),

        # Test case 18: Large text with complex pattern.
        ("a" * 1000000 + "ab" * 25000 + "a" * 1000000, "ab" * 25000),

        # Test case 19: Large text with a simpler pattern.
        ("ab" * 1000000, "abab"),

        # Test case 20: Large text with a complex pattern at the end.
        ("a" * 1000000 + "ab" * 25000 + "a" * 1000000, "ab" * 25000),

        # Test case 21: Large text with a simple pattern.
        ("ab" * 1000000, "abab"),

        # Test case 22: Long text with a randomized complex pattern at the beginning.
        ("0123456789" * 200000, "01234" * 40000),

        # Test case 23: Large text with a complex pattern at the end.
        ("abcdefghijklmnopqrstuvwxyz" * 50000, "uvwxyz" * 10000),

        # Test case 24: Long text with a randomized complex pattern in the middle.
        ("abcdefghijklmnopqrstuwxyz" * 100000, "pqrs" * 25000 + "uvwxyz" * 25000),

        # Test case 25: Long text with an alternating pattern.
        ("0101010101" * 50000, "01" * 25000)

    ]