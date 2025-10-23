#import os
#os.chdir("/Users/steven/Documents/Cours FASEST /L2/S3/intro_programmation/python_L2/data/") # Changement de répertoire même si le fichier de data était déjà pointable.
#os.getcwd()


import pandas as pd

pd.set_option('display.max_columns', None)  # Pour afficher toutes les colonnes si nécessaire
pd.set_option('display.width', None)  # Pour éviter les coupures dans l'affichage

df = pd.read_csv("data/aviation_2024.csv")
head = (df.head()) # Le fichier contient les pays, le code des pays, l'année, les émissions de CO2 des pays par habitant (en kg de CO2) et un doublon de l'année.
# df.head affiche les 5 premières lignes du dataframe et les noms des colonnes. Cela permet d'avoir un aperçu rapide des données chargées.

info = (df.info())
describe = (df.describe()) # Les commandes indiquent des informations sur le dataframe, notamment le type de données (ici float, int64, object).
# Le nombre de lignes non nulles (permet de savoir si des données sont manquantes, afin d'appliquer un traitement si nécessaire comme la suppression, l'imputation, l'interpolation en cas de données temporelles etc).
# Les statistiques descriptives de base (mean, std, min, quartiles, max) pour les colonnes numériques.

isna = (df.isna().sum()) # Permet de compter le nombre de valeurs manquantes par colonne, mais nous avions déjà l'info avec df.info(). Ici aucune valeur manquante.
columns = (df.columns) # Entity = Pays, Code = raccourci du nom du pays, Year = Année, CO2 emissions (kg per capita) = émissions de CO2 par habitant à l'année venant de l'utilisation de l'avion.
sort_values = (df.sort_values(by=df.columns[3], ascending=False).head(5)) # Qatar, Iceland, United Arab Emirates, Singapore, Maldives sont les pays avec les plus fortes émissions de CO2 par habitant liées à l'aviation en 2021.
# Résultats cohérents car ce sont des pays riches avec une forte activité aérienne par habitant due au tourisme (compté dans les émissions par habitant même si les touristes ne sont pas des habitants du pays).
# Dépendance à l'avion pour les déplacements (Iceland, Maldives) et des hubs aériens internationaux (Singapore, UAE) avec de faibles taux de population.

mean = df[df.columns[3]].mean() # Utilisation de df.columns car mettre le nom d'une colonne en brut n'est pas une bonne pratique de programmation. J'utilise mean même si ça n'est pas nécessaire car la donnée est déjà une moyenne par habitant.
median = df[df.columns[3]].median()
min_val = df[df.columns[3]].min()
max_val = df[df.columns[3]].max()
# La distribution des émissions entre les pays est très dispersée car la richesse des pays est très hétérogène. Un min et un max avec une étendue de 3766 kg de CO2 par habitant.

single_pays = df[df['Entity'] == 'France'] # 307 kg de CO2 par habitant en 2024 pour la France.

# Affichage des résultats
print("Informations sur le DataFrame :")
print(head)
print(info)
print(describe)
print(isna)
print(columns)
print(sort_values)
print(single_pays)
print("Statistiques descriptives :")
print(f"Mean : {mean}")
print(f"Median : {median}")
print(f"Min : {min_val}")
print(f"Max : {max_val}")

# Visualisation simple

import matplotlib.pyplot as plt # Afin de sauvegarder la figure.
import pandas as pd

save_path = "TP4/top10_aviation_co2_emissions.png"
top10 = df.sort_values(by=df.columns[3], ascending=False).head(10)
top10.plot(kind="bar", x="Entity", y=[df.columns[3]], title="Top 10 des pays avec les plus fortes émissions de CO2 par habitant liées à l'aviation en 2021")
print("Top 10 des pays avec les plus fortes émissions de CO2 par habitant liées à l'aviation en 2021 :")
print(top10)
plt.savefig(save_path) # Il y a un écart important entre les pays du top 10, avec un écart d'environ 3000 kg de CO2 par habitant entre le Qatar et l'Islande.
plt.show()

# Statistiques descriptives et interprétation économiques.

stats = df[df.columns[3]].describe()
print("Statistiques descriptives complètes :")
print(stats) # Affiche les statistiques descriptives complètes pour les émissions de CO2 par habitant liées à l'aviation de toute la série statistique.
# La différence entre la moyenne et la médiane signifie qu'il y a une forte asymétrie positive (mean > median) dans la distribution des émissions de CO2.

top5_max = df.sort_values(by=df.columns[3], ascending=False).head(5)
top5_min = df.sort_values(by=df.columns[3], ascending=True).head(5)
print("Top 5 des pays avec les plus fortes émissions de CO2 par habitant liées à l'aviation en 2021 :")
print(top5_max)
print("Top 5 des pays avec les plus faibles émissions de CO2 par habitant liées à l'aviation en 2021 :")
print(top5_min)
# Question déjà répondue plus haut.

variance = df[df.columns[3]].var()
std = df[df.columns[3]].std()
print(f"Variance : {variance}")
print(f"Écart-type : {std}") # L'écart-type est d'environ 500 kg de CO2 par habitant (la variance servant qu'à calculer le std). Cela signifie de fortes inégalités environnementales entre pays. 
# Attention aux biais énormes, ici nous avons seulement les émissions de CO2 agrégées des habitants par pays sur une année. On ne peut pas analyser les inégalités au sein d'un même pays
# Si des émissions sont attribuées aux habitants du pays, alors que ce sont des touristes étrangers, si l'avion est le seul moyen de se déplacer, les autres types d'émissions de CO2 etc.
# Il ne faut pas tirer des conclusions hâtives sans de nombreuses autres données pertinentes et une analyse fine du contexte économique, géographique et social.

mean_values = df[df.columns[3]].mean()
france_values = df[df['Entity'] == 'France'][df.columns[3]].mean()
print(f"Moyenne des émissions de CO2 par habitant liées à l'aviation : {mean_values} kg de CO2")
print(f"Émissions de CO2 par habitant liées à l'aviation en France : {france_values} kg de CO2")

# La France a des émissions de CO2 par habitant liées à l'aviation en moyenne très légèrement supérieures à la moyenne mondiale, alors que les revenus moyens des Français sont en moyenne très nettement supérieurs à la moyenne mondiale. Donc des émissions relativement faibles.
# Les facteurs économiques sont un haut revenu moyen, une forte activité touristique, une accessibilité aux transports aériens aisée.
# Cela peut aussi être expliqué par un prix du billet d'avion relativement élevé en France (prix d'équilibre élevé), les taxes sur les billets d'avion, la forte demande pour les billets d'avion (prix en fonction de l'offre et de la demande).
# Géographiquement, la France est positionnée au centre de l'Europe, donc il y a de nombreuses alternatives à l'avion. Au sein de la France, il y a de nombreuses routes, de nombreuses voies ferrées, des réseaux de bus etc.

print("TP terminé.")
