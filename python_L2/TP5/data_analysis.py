import pandas as pd
from constantes import COLUMN_RENAME

def load_dataset():
    # Chargement des données
    data = pd.read_csv("data/top_1_france.csv")
    data.head()
    data.info()
    data.columns
    print(data.head())
    print(data.info())
    print(data.columns)

    return data


def rename_column(data):
    ''' Rename column top 1 pretax into top1'''

    data = data.rename(columns=COLUMN_RENAME)
    print(data.columns)

    return data

def clean_columns(data): 
    ''' Clear columns with caps and underscore '''

    data.columns = data.columns.str.lower().str.replace(' ', '').str.replace('_', '')
    print(data.columns)

    return data

def convert_columns(data):
    ''' convert year into int and top1 in float '''

    data['year'] = data['year'].astype(int)
    data['top1'] = data['top1'].astype(float)
    print(data.dtypes)
    
    return data

def filter_entity(data):
    ''' Filter data on entity == France and sort by year '''
    fr = data[data['entity'] == "France"]
    fr = fr.sort_values(by='year', ascending=True).reset_index(drop=True)
    print(fr['year'].min(), fr['year'].max())
    return fr

def check_data(fr):
    ''' Check data quality '''

    missing_values = fr.isna().sum()
    print(missing_values)
    
    fr['plage'] = fr['top1'].between(0,100, inclusive='both')
    fr_hors_plage = fr[~fr['plage']]
    print(fr_hors_plage)

    fr_unicity = fr["year"].duplicated().sum()
    print(fr_unicity)

    return fr


def stats_descriptives(fr):
    ''' Stats Descriptives Calcul '''

    stats = fr['top1'].describe()
    print(stats)

    année_max = fr.loc[fr['top1'].idxmax(), 'year']
    année_min = fr.loc[fr['top1'].idxmin(), 'year']
    print(année_max, année_min)

    return stats, année_max, année_min


def derivative_features(fr):
    ''' Derivative Features Calcul '''

    premiere_valeur = fr['top1'].iloc[0]
    annee_base = fr['year'].iloc[0]

    fr['top1_base100'] = (fr['top1'] / premiere_valeur) * 100
    fr['indice_100'] = fr['top1_base100']

    indice_100 = fr['top1_base100'].iloc[0]
    print(indice_100)

    return fr

def variation(fr):
    ''' Variation Calcul '''

    fr['delta_pts'] = fr['top1'].diff()
    print(fr['delta_pts'])
    
    fr['delta_pct'] = 100 * fr['top1'].pct_change()
    print(fr['delta_pct'])

    annee_hausse_pts = fr.loc[fr['delta_pts'].dropna().idxmax(), 'year']
    annee_baisse_pts = fr.loc[fr['delta_pts'].dropna().idxmin(), 'year']
    print(annee_hausse_pts, annee_baisse_pts)

    annee_hausse_pct = fr.loc[fr['delta_pct'].dropna().idxmax(), 'year']
    annee_baisse_pct = fr.loc[fr['delta_pct'].dropna().idxmin(), 'year']
    print(annee_hausse_pct, annee_baisse_pct)
    
    print("Les points de pourcentage mesurent la variation absolue (ex: de 10% à 12% = 2 points).")
    print("Le pourcentage mesure la variation relative (ex: de 10% à 12% = 20% d'augmentation).")

    return fr


def gap_data(fr):
    ''' Gap in Data in year column '''

    next_year = fr['year'].shift(-1)
    fr['gap'] = next_year - fr['year']
    print(fr['gap'])

    lignes_gap = fr[fr['gap'] > 1]
    print(lignes_gap[['year', 'gap']])

    return fr

def moving_average(fr, window=3):
    ''' Moyenne mobile courte (moving average) '''

    fr['mm3'] = fr['top1'].rolling(window=window, center=True).mean()
    print(fr[['year', 'top1', 'mm3']])

    return fr

def prepare_graphique(fr):
    ''' Préparer les données pour le tracé (section Graphiques) '''
    
    data_graphique = fr[['year', 'top1', 'mm3']]
    
    return data_graphique


# Le lissage par moyenne mobile modifie fondamentalement la lecture des données.
# Elle est utilsée pour les séries temporelles, elle permet de lisser les variations à court terme 
# et de mettre en évidence les tendances générales.
# Elle permet de réduire le bruit statistique présents dans les données brutes.
# Elle permet d'aligner mieux les valeurs lissées avec les périodes observées.
# Cela facilite l'identification des cycles et des changements de tendance à long terme.
# Elle permet de distinguer les mouvements structurels des variations conjoncturelles.
# Elle rend la série plus lisible en supprimant les outliers qui masquent la tendance.
# Elle réduit aussi la réactivité aux changements récents et peut retarder la détection de retournements.
# Pour une fenêtre de 3 ans, chaque valeur lissée représente la moyenne de 3 observations consécutives.
# Cela signifie que les variations annuelles sont atténuées au profit d'une vision sur 3 ans.
# Elle est donc un compromis entre la précision des données brutes et la clarté de la tendance.
# Elle transforme une série bruyante en une courbe lisible qui révèle les patterns sous-jacents.
# En finance quantitative, elle est utilisée pour des stratégies de trading, comme par exemple, le croisement
# entre une moyenne mobile courte et une moyenne mobile longue afin de détecter un changement de tendance.


def periode_splitting(fr):
    ''' Diviser en périodes et calculer la moyenne par période '''

    bins = [1820, 1900, 1946, 1981, 2026]
    labels = ['1820-1899', '1900-1945', '1946-1980', '1981-2025']
    fr['periode'] = pd.cut(fr['year'], bins=bins, labels=labels, include_lowest=True, right=False)
    
    moyenne_par_periode = fr.groupby('periode', observed=False)['top1'].mean()
    print(moyenne_par_periode)
    
    periode_max = moyenne_par_periode.idxmax()
    print(periode_max)
    
    return fr