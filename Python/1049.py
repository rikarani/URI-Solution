input1 = input()
input2 = input()
input3 = input()

if (input1 == "vertebrado") :
    if (input2 == "ave") :
        if (input3 == "carnivoro") :
            print("aguia")
        else :
            print("pomba")
    elif (input2 == "mamifero") :
        if (input3 == "onivoro") :
            print("homem")
        else :
            print("vaca")
elif (input1 == "invertebrado") :
    if (input2 == "inseto") :
        if (input3 == "hematofago") :
            print("pulga")
        else :
            print("lagarta")
    elif (input2 == "anelideo") :
        if (input3 == "hematofago") :
            print("sanguessuga")
        else :
            print("minhoca")