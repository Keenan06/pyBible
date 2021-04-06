known_users = ["Caleb", "Ambre", "Aidan", "Kyle", "Cairo", "Theresa", "Nico", "Kayla"]

# print(len(known_users))

while True:
    print("Hi my name is Keens")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}.".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("Enjoy your stay on our system.")

        else:
            print("Are you a new user, {}? ").format(name))
            add = input("Are you sure (y/n)?:").strip().lower()
            if add == "y":
                known_users.append(name)
            elif add== "n":
                print("Bye bye")