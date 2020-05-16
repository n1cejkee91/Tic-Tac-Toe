text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

a = int(input())
spisok = [word for sentense in text for word in sentense if len(word) <= a]
print(spisok)