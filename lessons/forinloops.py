"""Playing around with for in loops"""

names_list: list[str] = ["Alyssa", "Janet", "Vrinda"]
index: int = 0
for index in range(0, len(names_list)):
    print(index, ":", names_list[index])
    index += 1
