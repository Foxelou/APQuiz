import json
import random

nom = ""

config = None
theme = "Culture Générale"
themes_disponibles = []
nombre_de_questions = 2
nombre_option_reponse = 2
questions = None
reponsesUtlisateur = {}

def initialiser_quiz():
    global config
    global themes_disponibles
    global nombre_de_questions
    global nombre_option_reponse
    
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    nombre_de_questions = config['nombre_de_questions']
    nombre_option_reponse = config['nombre_options_reponse']
    themes_disponibles = list(config["questions"].keys())


# Simple quiz en utilisant les dictionnaires
def main():
    global nom
    global theme
    global questions
    print ("*** Début du Quiz ***\n")
    initialiser_quiz()
    nom = input (" Entrez votre nom: ").title()
    print ()
    print("Choix du theme du quiz :")
    numero_option = 0
    for theme_option in themes_disponibles:
        print("Quiz " + str(numero_option + 1) + ") " + str(theme_option))
        numero_option += 1
    print("Entrez ci-dessous le numéro de quiz sur lequel vous voulez vous évaluer :")
    reponse=input(" > ")
    #reponsesUtlisateur[liste[aleatoire][0]] = reponse

    theme = themes_disponibles[int(reponse)-1]
    questions = config["questions"][theme]

    print(f"Nombre de questions : {nombre_de_questions}\n")
    quiz(questions)
    correction()

def quiz(qs):
    dico=qs.items()
    liste=[]
    peu_tombe=[]
    for elt in dico: # mettre tous les elements de dico dans liste
        liste.append(elt)
    for i in range(len(liste)): # mettre les ID des questions dans peu_tombe
        peu_tombe.append(i)
  
    for _ in range(nombre_de_questions):
        
        aleatoire=random.randint(0,len(liste))
        if len(peu_tombe)!=0:
            while aleatoire not in peu_tombe :
                aleatoire=random.randint(0,len(liste))
            peu_tombe.remove(aleatoire)
            print(liste[aleatoire][0])

            options = []
            while liste[aleatoire][1]["reponse"] not in options:
                options = random.sample(list(liste[aleatoire][1]["options"]), nombre_option_reponse)

            numero_option = 0
            for option in options:
                print("Option " + str(numero_option + 1) + ") " + str(option))
                numero_option += 1
            reponse=input(" > ")
            if reponse.isdigit():
                reponsesUtlisateur[liste[aleatoire][0]] = options[int(reponse)-1]
            else:
                reponsesUtlisateur[liste[aleatoire][0]] = reponse


def correction():
    global questions
    global reponsesUtlisateur
    points = 0

    for question, answers in questions.items():
        if question in reponsesUtlisateur:
            if str(reponsesUtlisateur[question]).lower() != str(answers["reponse"]).lower():
                print("- Correction de la question :")
                print("   " + question)
                print("   Votre choix : " + str(reponsesUtlisateur[question]))
                print("   Correction  : " + str(answers["reponse"]))
            else:
                points += 1
    
    print("\nBien joué {0}, vous avez répondu correctement à {1} sur {2} questions.".format(nom, points, nombre_de_questions))
    relance=input("une autre partie ? y/n \n > ")
    if relance=="y":
        questions = None
        reponsesUtlisateur = {}
        main()


    
if __name__ == "__main__":
    main()