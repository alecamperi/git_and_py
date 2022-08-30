from functools import reduce

# list_1 = [1,2,4,6,11,22,33,44]
# list_2 = [50, 40, 80]

# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# print(f(200))

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])