import json
import random

nom = ""
theme = "Culture Générale"
nombre_de_questions = 2
nombre_option_reponse = 2
questions = None
reponsesUtlisateur = {}

def initialiser_quiz():
    global theme
    global nombre_de_questions
    global nombre_option_reponse
    global questions
    
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    theme = config['theme']
    nombre_de_questions = config['nombre_de_questions']
    nombre_option_reponse = config['nombre_options_reponse']
    questions = config["questions"][theme]


# Simple quiz en utilisant les dictionnaires
def main():
    global nom
    print ("*** Début du Quiz ***\n")
    initialiser_quiz()
    nom = input (" Entrez votre nom: ").title()
    print ()
    print(f"Thème du quiz : {theme}")
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