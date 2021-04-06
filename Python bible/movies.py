movies = {
    "Spongebob": [1,14],
    "Godzilla": [13,30],
    "American Pie 10": [18,17],
    "Human centipede": [21,12]
}

while True:
    choice = input("What would you like to watch? :").strip()

    if choice in movies:
        age=int(input("How old are you?").strip())
        #check age
        if age >= movies[choice][0]:
            # available seats
            if movies[choice][1]>0:
                print(" That will be R40, enjoy!")
                movies[choice][1] = movies[choice][1] -1
            else:
                print("No more seats available")

        else:
            print("You're way too young kid")

    else:
        print("This movie is unavailable")
        