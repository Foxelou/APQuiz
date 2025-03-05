# Projet d'Atelier Professionnalisation

Nom d'utilisateur Github : <br>
foxelou -> Elouan<br>
kurbtica -> Maël

## Instructions

Par groupes de 2, vous travaillerez à la réalisation d'une application console de quiz. L’accent sera mis sur les étapes fonctionnelles ainsi que sur l’organisation du travail en équipe via Trello. La recette aura pour but de rendre votre application robuste, les éventuelles erreurs de paramétrage devront être gérées. L’atelier sera découpé en itérations.

## 1 Première itération
Pour la première itération, nous allons paramétrer le thème du questionnaire et le nombre de questions qui seront posées.
Pour cela, vous implémenterez les objectifs suivants :
- La création d’un fichier de configuration JSON qui définit le thème du questionnaire et le nombre de questions posées.
- La création d’une fonction Python qui va charger les données du fichier de configuration et gérer l’initialisation du jeu.
## 2 Deuxième itération
Pour cette itération, nous souhaitons charger les questions du quiz, tirer au hasard les questions qui seront posées et les afficher.
Pour cela, vous implémenterez les objectifs suivants :
- L’ajout de questions de test dans le fichier de configuration JSON.
- Le tirage aléatoire de n questions (n étant le nombre de questions paramétré dans le fichier de configuration). Les questions ne doivent pas apparaître plusieurs fois dans une même session de quiz.
- L’affichage d’une question avec ses réponses possibles.
- La possibilité de valider une réponse et afficher la question suivante (nous omettrons l’évaluation de la réponse dans cette étape)
## 3 Troisième itération
Pour cette troisième itération, nous voulons évaluer les réponses, donner des points, et afficher le score final à la fin du quiz.
Pour cela, vous implémenterez les objectifs suivants :
- L’ajout des bonnes réponses aux questions dans le fichier de configuration JSON.
- La vérification d’une réponse lors de la validation par l’utilisateur, et l’attribution ou non de points.
- Une conclusion propre du quiz après la validation de la dernière réponse, l’affichage du score final, et la possibilité de relancer un quiz.
## 4 Quatrième itération
La quatrième itération introduira la possibilité d’avoir un nombre différent de réponses pour chaque question. Il faudra pouvoir décider du nombre de réponses à afficher pour chaque question, et ces réponses devront être tirées au sort parmi une sélection.
Pour cela, vous implémenterez les objectifs suivants :
- L’adaptation du fichier de configuration JSON pour coller aux nouvelles exigences.
- Le tirage aléatoire de n réponses pour une question donnée (n étant précisé pour chaque question dans le fichier de configuration JSON) Les réponses ne doivent pas apparaître plusieurs fois dans une même question.
## 5 Cinquième itération
Pour la cinquième itération, nous souhaitons rendre possible qu’une question ait plusieurs bonnes réponses à cocher. Il faut que la question soit validée uniquement si toutes les bonnes réponses, et seulement celles-ci sont cochées.
Pour cela, vous implémenterez les objectifs suivants :
- L’adaptation du fichier de configuration JSON pour coller aux nouvelles exigences.
- L’adaptation du code afin de prendre en compte la possibilité que de telles questions soient tirées.
## 6 Sixième itération
Enfin, cette dernière itération permettra à l’utilisateur de choisir un quiz parmi une liste de choix.
Tous les quiz seront paramétrés dans le même fichier JSON. Pour cela, vous implémenterez les objectifs suivants :
- L’adaptation du fichier de configuration JSON pour coller aux nouvelles exigences.
- L’adaptation de l’écran de fin de quiz permettant de lancer un nouveau quiz, ou de relancer le même quiz.