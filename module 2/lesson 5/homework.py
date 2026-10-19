print("Library Shelf Organizer")
print("-----------------------")

shelves = int(input("Enter number of shelves: "))
sections = int(input("Enter sections per shelf: "))

location = 1

print("Library shelf layout")

for shelf in range(1, shelves + 1):
    for section in range(1, sections + 1):
        for section in range(1, section + 1):
            print(f"Shelf {shelf} - Location {location}", end=" ")
            location += 1
        print()