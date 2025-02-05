import json

theme = "Culture Générale"
nombre_de_questions = 10
questions = None

def initialiser_quiz():
    global theme
    global nombre_de_questions
    global questions
    
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    theme = config['theme']
    nombre_de_questions = config['nombre_de_questions']
    questions = config["questions"][theme]


# Simple quiz en utilisant les dictionnaires
def main():
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
        if str(input(qu)).lower() == str(an).lower():
            points += 1
            print("Juste.")
        else:
            print("Oups, la bonne réponse est \"{}\".".format(an))
    return points
    
if __name__ == "__main__":
    main()