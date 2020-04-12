for i in range(0,14):
    s=str(input())
    if(s.upper() and len(s)<=14):
        if(s=="HELLO"):
            print("Case 1: ENGLISH")
        elif(s=="HOLA"):
            print("Case 2: SPANISH")
        elif(s=="HALLO"):
            print("Case 3: GERMAN")
        elif(s=="BONJOUR"):
            print("Case 4: FRENCH")
        elif(s=="CIAO"):
            print("Case 5: ITALIAN")
        elif(s=="ZDRAVSTVUJTE"):
            print("Case 6: RUSSIAN")
        elif(s=="#"):
            exit
        else:
            print("UNKNOWN")
    else:
        print("Length is so huge")
exit
