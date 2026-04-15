students = {
			"Ali":80,
			"Sara":90,
			"Ahmed":75
}

print(students.keys())
print(students.values())

highest = max(students.values())
print("Highest Marks:", highest)

for name in students:
    if students[name] == highest:
        print("Top Student:", name)
        print("Highest Marks:", highest)