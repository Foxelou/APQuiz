# Simple quiz en utilisant les dictionnaires
def main():
    questions={'Quel est la capitale du Pérou ? ':'Lima',
        'Comment s\'appelle le petit du lion':'lionceau',
        'Comment dit on plage en espagnol ':'playa',
        'Quel est la longueur du canal de Nantes à Brest':'260',
    }
    print ("*** Début du Quiz ***\n")
    nom = input (" Entrez votre nom: ").title()
    print ()
    print("\nBien joué {0}, vous avez repondu à {1} de {2} questions.".format(nom, quiz(questions), len(questions)))

def quiz(qs):
    points = 0
    for qu,an in qs.items():
        if input(qu).lower() == an.lower():
            points += 1
            print("Juste.")
    else:
        print("Oups, la bonne réponse est \"{}\".".format(an))
        return points
    
if __name__ == "__main__":
    main()