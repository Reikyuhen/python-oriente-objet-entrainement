def askInteger(sentence) -> int :
    while(True):
        try:
            value = int(input(sentence))
            return value
        except:
            print("Valeur invalide, ressayez.")