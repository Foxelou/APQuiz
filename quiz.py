import json
import random

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
    dico=qs.items()
    liste=[]
    peu_tombe=[]
    for elt in dico:
        liste.append(elt)
    for i in range(len(liste)):
        peu_tombe.append(i)
  
    for _ in range(nombre_de_questions):
        
        aleatoire=random.randint(0,len(liste))
        print(aleatoire)
        if len(peu_tombe)!=0:
            while aleatoire not in peu_tombe :
                aleatoire=random.randint(0,len(liste))
                print(aleatoire)
            peu_tombe.remove(aleatoire)
            print(peu_tombe)
            reponse=input(liste[aleatoire][0])
            if reponse == liste[aleatoire][1]:
                points += 1
                print("Juste.")
            else:
                print("Oups, la bonne réponse est : ",liste[aleatoire][1])
    return points
    # for qu,an in qs.items():
    #     if str(input(qu)).lower() == str(an).lower():
    #         points += 1
    #         print("Juste.")
    #     else:
    #         print("Oups, la bonne réponse est \"{}\".".format(an))
    # return points
    
if __name__ == "__main__":
    main()