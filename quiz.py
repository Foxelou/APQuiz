import json

theme = "Culture Générale"
nombre_de_questions = 10

def initialiser_quiz():
    global theme
    global nombre_de_questions
    
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    theme = config['theme']
    nombre_de_questions = config['nombre_de_questions']

# Simple quiz en utilisant les dictionnaires
def main():
    questions={'Quel est la capitale du Pérou ? ':'Lima',
        'Comment s\'appelle le petit du lion ? ':'lionceau',
        'Comment dit on plage en espagnol ? ':'playa',
        'Quel est la longueur du canal de Nantes à Brest ? ':'260',
    }

    print ("*** Début du Quiz ***\n")
    initialiser_quiz()
    nom = input (" Entrez votre nom: ").title()
    print ()
    print(f"Thème du quiz : {theme}")
    print(f"Nombre de questions : {nombre_de_questions}\n")
    print("\nBien joué {0}, vous avez répondu correctement à {1} sur {2} questions.".format(nom, quiz(questions), len(questions)))

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