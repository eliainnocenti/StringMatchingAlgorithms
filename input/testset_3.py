# testset_3.py

# Path: input/testset_3.py

# Test set 3 - tests with the same text but different patterns

testset_3_1 = [

        ("0123456789" * 200000000, "56789" * 4     + "23456" * 4),
        ("0123456789" * 200000000, "56789" * 40    + "23456" * 40),
        ("0123456789" * 200000000, "56789" * 400   + "23456" * 400),
        ("0123456789" * 200000000, "56789" * 4000  + "23456" * 4000),
        ("0123456789" * 200000000, "56789" * 40000 + "23456" * 40000)

]