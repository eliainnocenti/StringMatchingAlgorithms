# testset_2.py

# Path: input/testset_2.py

# Test set 2 - tests with the same text of different sizes but same pattern in every test case

testset_2_1 = [

        ("0123456789" * 2000,      "56789" * 40 + "23456" * 40),
        ("0123456789" * 20000,     "56789" * 40 + "23456" * 40),
        ("0123456789" * 200000,    "56789" * 40 + "23456" * 40),
        ("0123456789" * 2000000,   "56789" * 40 + "23456" * 40),
        ("0123456789" * 20000000,  "56789" * 40 + "23456" * 40)

]

testset_2_2 = [

        ("0123456789" * 2000,      "56789" * 400 + "23456" * 400),
        ("0123456789" * 20000,     "56789" * 400 + "23456" * 400),
        ("0123456789" * 200000,    "56789" * 400 + "23456" * 400),
        ("0123456789" * 2000000,   "56789" * 400 + "23456" * 400),
        ("0123456789" * 20000000,  "56789" * 400 + "23456" * 400)

]

testset_2_3 = [

        ("0123456789" * 2000,      "56789" * 4000 + "23456" * 4000),
        ("0123456789" * 20000,     "56789" * 4000 + "23456" * 4000),
        ("0123456789" * 200000,    "56789" * 4000 + "23456" * 4000),
        ("0123456789" * 2000000,   "56789" * 4000 + "23456" * 4000),
        ("0123456789" * 20000000,  "56789" * 4000 + "23456" * 4000)

]