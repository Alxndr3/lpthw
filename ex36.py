def start():
    print("You are preparing for a nice travell.")
    print("There is two options, Canada and Europe")
    print("Which one do you take?")

    choice = str(input("> ")).upper()

    if choice == "CANADA":
        canada()
    elif choice == "EUROPE":
        europe()
    else:
        print("I said Canada or Europe")
        print("Donkey face")
        exit(0)

def canada():
    while True:
        print("As Canada is a so big country")
        print("You can choose one province b/w two")
        print("Do you choose Quebec or Ontario?")

        province = str(input("> ")).upper()

        if province == "QUEBEC":
            provQuebec()
        elif province == "ONTARIO":
            provOntario()
        else:
            print("Wrong choice Animal 8-D")

def europe():
    from random import choice
    from time import sleep
    print("You can visit three countries.")
    print('''
    As there are so many in Eroupe, I'll rafle three for you
    among the ones below.
    ''')
    print('''
    Austria	Italy
    Belgium	Latvia
    Bulgaria	Lithuania
    Croatia	Luxembourg
    Cyprus	Malta
    Czechia	Netherlands
    Denmark	Poland
    Estonia	Portugal
    Finland	Romania
    France	Slovakia
    Germany	Slovenia
    Greece	Spain
    Hungary	Sweden
    Ireland	United Kingdom
    ''')
    countEurope = ('Austria', 'Italy', 'Belgium', 'Latvia', 'Bulgaria', 'Lithuania', 'Croatia',	'Luxembourg', 'Cyprus', 'Malta', 'Czechia', 'Netherlands', 'Denmark', 'Poland', 'Estonia', 'Portugal', 'Finland', 'Romania', 'France', 'Slovakia', 'Germany', 'Slovenia', 'Greece', 'Spain', 'Hungary', 'Sweden', 'Ireland', 'United Kingdom')
    sleep(3)

    threeCount = []

    for x in range(1, 4):
        threeCount.append(choice(countEurope))

    print(f"You lucky ducky you're going to {threeCount}")


def provQuebec():
    speakFrench = str(input("Do you speak french?")).upper()
    if speakFrench == "YES":
        print("Nice, Have fun!")
    else:
        provOntario()

def provOntario():
    print("Do you speak english")
    speakEnglish = input("> ").upper()
    if speakEnglish == 'YES':
        print("Have fun!")
    else:
        print("You're in trouble")
    exit(0)


start()
