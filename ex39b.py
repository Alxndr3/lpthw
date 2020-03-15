brazil_states_dict= {}

while True:
    brazil_states = (str(input("type a brazilian state: ")).title())
    brazil_state_abbreviation = str(input('Now type its abbreviation: ')).upper()
    brazil_states_dict[brazil_states] = brazil_state_abbreviation
    continuar = str(input('Would you like to continue, YES/NO: ')).strip().upper()
    while continuar not in 'YESNO': 
        continuar = str(input('Would you like to continue, YES/NO: ')).strip().upper()
    if continuar == 'NO': 
        break
    else:
        continue

print(brazil_states_dict)
