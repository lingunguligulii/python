missions = int(input("How many missions?"))

for mission in range(1, missions+1):
    print("Mission", mission)

    event = input("Enter event (skip/finish/continue): ")

    if event == "skip":
        print("mission skipped")
        continue

    elif event == "finish":
        print("Mission finished")
        break
    elif event == "continue":
        pass
    print("Mission", mission, "Completed")