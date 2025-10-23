import matplotlib.pyplot as plt
import numpy as np # Import de numpy pour le calcul de la moyenne et l'intégrer directement dans le graphique.
import os

notes = [12, 14, 10, 8, 16, 15, 9]
export_path = os.path.join('TP3', 'histogramme_notes.png') # Je laisse le chemin dans le fichier principal pour l'exercice.

def plot_notes(notes):
    '''On trie correctement les notes et on crée l'histogramme.'''

    # Je trie les notes dans l'ordre et je compte le nombre de valeurs dans "notes". Et je converti en array numpy pour le calcul de la moyenne.
    notes_array = np.array(notes)
    notes_triees = np.sort(notes_array)
    indices = range(1, len(notes_triees) + 1) 

    # Création du plot avec x et y
    plt.title('Histogramme des notes')
    plt.xlabel('Numéro de la note')
    plt.ylabel('Notes obtenues')
    plt.xticks(indices)
    plt.axhline(y=notes_triees.mean(), color='red', linestyle='dashed', linewidth=1)
    plt.bar(indices, notes_triees, edgecolor='black', alpha=0.2) # Utilisation de plt.bar car une occurence par note donc pas de distribution à analyser. Histogramme avec barres toutes égales à 1.
    plt.savefig(export_path)
    plt.show()
    plt.close() # Je ferme le plot pour libérer la mémoire.

plot_notes(notes)

# Questions de vérification

# bin compte la fréquence, ici il n'y a que des valeurs uniques donc les barres sont mauvaises. utilisation de plt.bar afin d'afficher la valeur de la note directement.

# L'axe x affichera position de la note dans la liste triée, l'axe y affiche la valeur de la note.

# Si j'avais mis range (8, 16) à la place de (0, 20) en cas d'utilisation de plot.hist, la notes 16 n'aurait pas été prise en compte.

# La couleur s'éclaircit en utilisant l'argument alpha dans plt.bar.

# Exercice 2 : Comparaison de deux classes

import matplotlib.pyplot as plt # J'appelle à nouveau les dépendances pour ne pas avoir à executer tout le fichier de code.
import numpy as np
import os

classe_A = [12, 14, 10, 8, 16, 15, 9] # Je rééecris la liste pour plus de clarté et ne pas écraser l'ancienne.
classe_B = [11, 13, 12, 7, 17, 14, 10]
export_path2 = os.path.join('TP3', 'histogramme_comparaison.png')

def plot_comparaison(classe_A, classe_B):
    ''' Je crée un histogramme comparant les deux classes en triant d'abord les notes et en les convertissant en array numpy pour le calcul de la moyenne.'''
    plt.clf() # On nettoie le plot précédent pour éviter les chevauchements sinon ça crash.
    note_array_A = np.array(classe_A) # Je converti en np array pour le calcul statistique
    note_array_B = np.array(classe_B)
    notes_triees_A = np.sort(note_array_A)
    notes_triees_B = np.sort(note_array_B)
    indices_A = range(1, len(notes_triees_A) + 1) # Je prends que l'indice de la première classe, les deux classes ont le même nombre de notes.

    # Création du plot de comparaison
    plt.title('Comparaison des notes entre deux classes')
    plt.xlabel('Numéro de la note')
    plt.ylabel('Notes obtenues')
    plt.xticks(list(indices_A)) # Les deux classes ont le même nombre de notes, donc on peut utiliser indices_A seulement.
    plt.axhline(y=notes_triees_A.mean(), color='blue', linestyle='dashed', linewidth=1, label='Moyenne Classe A')
    plt.axhline(y=notes_triees_B.mean(), color='green', linestyle='dashed', linewidth=1, label='Moyenne Classe B')
    plt.bar(np.array(indices_A) - 0.2, notes_triees_A, width=0.4, color='blue', edgecolor='black', alpha=0.5, label='Classe A')
    plt.bar(np.array(indices_A) + 0.2, notes_triees_B, width=0.4, color='green', edgecolor='black', alpha=0.5, label='Classe B')
    plt.legend()
    plt.savefig(export_path2)
    plt.show()
    plt.close()

plot_comparaison(classe_A, classe_B)

# Les moyennes sont identiques car il y a qu'une barre visible de moyenne.

# Non les distributions ne se recouvrent pas parfaitement, mais les deux classes ont des notes similaires.

# La moyenne ne montre pas la dispersion des notes, les outliers, etc.

# Exercice 3 : Boîte à moustaches

import matplotlib.pyplot as plt
import os

export_path3 = os.path.join('TP3', 'boite_a_moustaches.png')
classe_A2 = [12, 14, 10, 8, 16, 15, 9] # Je change à nouveau le nom pour plus de clarté.
classe_B2 = [11, 13, 12, 7, 17, 14, 10]

def plot_boite_a_moustaches(classe_A2, classe_B2):
    ''' Création d'une boîte à moustaches pour constater ou non une différence avec l'observation du diagramme en barres.'''
    plt.clf()
    plt.title('Boite à moustaches des notes des deux classes')
    plt.ylabel('Notes obtenues')
    plt.boxplot([classe_A2, classe_B2], tick_labels=['Classe A', 'Classe B'])
    plt.savefig(export_path3)
    plt.show()
    plt.close()

plot_boite_a_moustaches(classe_A2, classe_B2)


# Le boxplot montre la médiane, quartiles (Q1, Q3),l'étendue interquartile, et les outliers, ce qui n'était pas visible dans le diagramme en barres.

# La médiane "coupe" la série statistiques en deux parties égales. Ici, on constate la même médiane pour les deux groupes. 

# L'analyse de présence d'outliers dépendent du contexte, du type de série statistique et de l'interprétation que l'on en fait. Notamment si l'on veut les traiter dans le cadre de modèle d'apprentissage. 
# Ici, on peut dire que les 7 et 17 de la classe B sont des outliers par rapport aux autres notes. 
# Même si ce n'est pas extrême, cela peut tromper si l'on se base que sur la moyenne, ainsi que sur la médiane dans ce cas. La classe B est un peu plus hétérogène que la classe A.

# Exercice 4 : Statistiques descriptives par classe.



class StatsDescriptives:
    '''Classe afin de regrouper les fonctions de stats descriptives.'''
    
    # Je défini les listes à l'intérieur de la classe afin qu'elles soient accessibles par toutes les fonctions.
    classe_A3 = [12, 14, 10, 8, 16, 15, 9]
    classe_B3 = [11, 13, 12, 7, 17, 14, 10]

    # Moyenne, médiane, mode, écart-type, variance, min, max sont utiles pour décrire l'échantillon.

    def somme_effectifs(self):
        return len(self.classe_A3), len(self.classe_B3)
    
    def moyenne(self):
        moy = (sum(self.classe_A3) / len(self.classe_A3), sum(self.classe_B3) / len(self.classe_B3))
        return moy
    
    def mediane(self):
        ''' Trie des valeurs dans l'ordre croissant et calcule la médiane.'''
        med_A_triees = sorted(self.classe_A3) # Sorted tri de base dans l'ordre croissant, donc suffisant ici.
        med_B_triees = sorted(self.classe_B3)
        med_A = med_A_triees[len(med_A_triees) // 2] if len(med_A_triees) % 2 != 0 else (med_A_triees[len(med_A_triees) // 2 - 1] + med_A_triees[len(med_A_triees) // 2]) / 2
        med_B = med_B_triees[len(med_B_triees) // 2] if len(med_B_triees) % 2 != 0 else (med_B_triees[len(med_B_triees) // 2 - 1] + med_B_triees[len(med_B_triees) // 2]) / 2
        return med_A, med_B
    
    def min_max(self):
        min_A = min(self.classe_A3)
        max_A = max(self.classe_A3)
        min_B = min(self.classe_B3)
        max_B = max(self.classe_B3)
        return min_A, max_A, min_B, max_B
    
    def ecart_type(self):
        moy_A = sum(self.classe_A3) / len(self.classe_A3) # Calcul de la moyenne pour chaque classe afin de calculer la variance.
        moy_B = sum(self.classe_B3) / len(self.classe_B3)
        variance_A = sum((x - moy_A) ** 2 for x in self.classe_A3) / len(self.classe_A3) # Calcul de la variance pour chaque classe.
        variance_B = sum((x - moy_B) ** 2 for x in self.classe_B3) / len(self.classe_B3)
        ecart_type_A = variance_A ** 0.5 # On élève à la puissance 1/2 la variance pour obtenir l'écart-type.
        ecart_type_B = variance_B ** 0.5
        return ecart_type_A, ecart_type_B



stats = StatsDescriptives()
print("Effectifs des classes A et B :", stats.somme_effectifs())
print("Moyennes des classes A et B :", stats.moyenne())
print("Médianes des classes A et B :", stats.mediane())
print("Min/Max de la classe A :", stats.min_max()[0:2]) # Je réutilise ce qui est appris au TP1 pour une meilleure clarté du print() :)
print("Min/Max de la classe B :", stats.min_max()[2:4]) 
print("Écart-type de la classe A :", stats.ecart_type()[0])
print("Écart-type de la classe B :", stats.ecart_type()[1])

# Même moyenne et mediane entre les deux classes. Cependant, on constate que l'écart-type est plus élevé pour la classe B, les notes min-max aussi. 
# La classe B est donc plus dispersée que la classe A.

# Si une note de 0 est ajoutée dans les classes, alors la moyenne chutera pour les deux classes.
# La médiane sera également affectée car on passe d'un nombre de valeur impair à pair, donc la médiane sera la moyenne des deux valeurs centrales.
# L'écart-type augmentera aussi car la dispersion des notes sera plus grande avec une note de 0.

print("TP terminé.")