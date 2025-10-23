# Exercice 1 - Créer un dossier de TP

# La commande permettant de revenir en arrière dans un dossier est cd --

# ls permet de lister les fichiers et dossiers dans le répertoire courant et dir permet de lister les fichiers et dossiers dans un répertoire spécifique.

# Exercice 2 - Script vs Interpréteur

# Exécuter un script permet d'exécuter un code de haut en bas. L'exécution s'arrête si une erreur survient. Alors que l'interpréteur permet d'exécuter des commandes une par une et de continuer même si une erreur survient.

# Il est préférable d'utiliser un script pour exécuter l'ensemble du code et du programme et l'interpréteur pour tester chaque partie du code individuellement et repérer les erreurs plus rapidement, sans avoir besoin de lancer entièrement le script, notamment si celui-ci utilise beaucoup de données à charger et des modèles lourds. 

# Exercice 3 - Python comme calculatrice

# La différence entre / et // est que / n'arrondit pas le résultat alors que // arrondit le résultat à l'entier inférieur.

# L'opérateur % donne le reste de la division euclidienne entre deux nombres.

# Le type de résultat de 20/6 est un float, c'est à dire un nombre à virgule.

# Exercice 4 - Ordre des opérations

# La priorité des opérations en Python est la même qu'en mathématiques, de ce fait dans le calcul 2 + 3 * 4, la priorité est à la multiplication, puis l'addition. Alors que le calcul (2 + 3) * 4 donne la priorité à l'addition grâce aux parenthèses.

# Python choisit l'ordre des opérations comme en mathématiques. 

# Exercice 5 - Chaînes de caractères

"Python" * 3 # Renvoie "PythonPythonPython" et permet de multiplier la chaîne de caractères "Python" 3 fois de suite.

len("Université de Lille") # Renvoie le nombre de l'ensemble des caractères dans la chaîne, espaces compris. Ici c'est 19.

s = "Python"
print(s[0]) # P
print(s[-1]) # n

# Exercice 6 - Créer des variables

# "Alice" est de type chaîne de caractères (str), 22 est de type entier (int), 1450.75 est de type flottant (float), True est un booléen (bool)

# int est un nombre entier, float est un nombre à virgule.

# Afin d'afficher toutes les variables en une seule avec print, on utilise la syntaxe suivante : 

nom = "Alice"
age = 22
revenu = 1450.75
etudiant = True

print(nom, age, revenu, etudiant)

# Exercice 7 - Conversions

# Il est nécessaire de convertir les variables afin de s'assurer qu'elles sont du bon type pour les changements qu'on souhaite effectuer dessus.

float("3.14") # Float 3.14 renvoie le nombre 3.14 alors que de base c'est une chaîne de caractères dû aux guillemets.

# Exercice 8 - Affichage formaté

print(nom, "a", age, "ans") # Affiche les valeurs des variables nom et age dans une phrase en rajoutant la chaine de caractères entre les valeurs.

print(f"{nom} a {age} ans") # Affiche la même chose que la ligne précédente mais en utilisant une f-string.

# La seconde écriture est plus lisible et plus simple à écrire, car moins de guillemets et de virgules sont nécessaires.

# Exercice 9 - Listes

# append() permet d'ajouter un élément à la fin de la liste initiale.

notes = [12, 15, 9]
notes[0] = 20
print(notes)  # [20, 15, 9]

sum(notes) / len(notes)  # Calcule la moyenne des notes dans la liste.

# Exercice 10 - Indexation de chaînes

mot = "Python"
print(mot[0])  # P
print(mot[-1])  # n
print(mot[0:3])  # Pyt
print(mot[::-1])  # nohtyP // Écrit le mot à l'envers
print(mot[2:])  # thon // Renvoie l'ensemble du mot excepté les deux premières lettres.
print(mot[3:])  # hon // Renvoie l'ensemble du mot excepté les trois premières lettres.
# OU
print(mot[-3:])  # hon // Renvoie les trois dernières lettres du mot.
# OU
print(mot[3:6])  # hon // Renvoie les lettres d'indice 3 à 5 inclus.

# Exercice 11 - Mise à jour de variable

# La valeur finale de x est : 7 car x += 1 est équivalent à x = x + 1

# Ce sont des écritures équivalentes, excepté que la première a 9 caractères et la seconde a 6 caractères.

# Exercice 12 - Booléens simples

# = est une affectation d'une valeur à une variable, alors que == est une comparaison entre deux valeurs.

# Le résultat quand x < 5 quand x = 10 est False.

# Exercice 13 - Opérateurs logiques

# and s'arrête au premier False et or s'arrête au premier True, cela permet d'éviter les calculs lourds si les critères ne sont pas remplis.

# not permet d'avoir la réponse inverse d'une condition. Exemple : si a = True, alors not a = False.

# Exercice 14 - Booléens implicites

# print(bool(0)) renvoie False car tout nombre différent de 0 est True et 0 est False. Pour les valeurs vides, bool renvoie False.

# bool(" ") renvoie True car c'est une valeur non vide, même si elle ne contient rien dû à l'espacement.

# Python renvoie False pour les zéros numériques, les séquences et collections vides, sinon il renvoie True.

# Exercice 15 - Mini-défis

from math import prod
from functools import reduce
import operator as op

x = 10
y = 13
valeur = [x, y]
    
print(sum(valeur)) # Renvoie 23, la somme de x et y.
print(prod(valeur)) # Renvoie 130, le produit de x et y.
print(reduce(op.sub, valeur)) # Renvoie -3, la soustraction de x et y.
print(reduce(op.truediv, valeur)) # Renvoie 0.7692307692307693, la division de x par y.

prenom = input("Votre prénom ? ")
print(f"Bonjour {prenom} !")

prenom_2 = ["Mbappe", "Dembele", "Doue"]

print(prenom_2[1])  # Dembele

"2" + 3 # Erreur car on additionne une chaîne de caractères avec un entier.
int("2") + 3 # Correct car grâce à int on convertit la chaîne de caractères en entier, donc l'addition peut se faire.

len(prenom_2) # En utilisant len sans guillemets, on obtient la taille de la liste, qui est de 3 ici.
