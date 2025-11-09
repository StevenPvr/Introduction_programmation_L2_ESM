import matplotlib.pyplot as plt
import os

def graphique_top1_mm3(fr):
    ''' Tracer top1 et mm3 en fonction de year '''
    
    plt.figure(figsize=(10, 6))
    plt.plot(fr['year'], fr['top1'], 'o-', label='top1', markersize=4, linewidth=1)
    plt.plot(fr['year'], fr['mm3'], '-', label='mm3 (moyenne mobile)', linewidth=2)
    
    plt.xlabel('Année')
    plt.ylabel('Part du top 1% (%)')
    plt.title('Évolution de la part du top 1% en France (1820-2023)')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend()
    plt.tight_layout()
    
    return plt

def graphique_indice_base100(fr):
    ''' Tracer indice base 100 en fonction de year '''
    
    plt.figure(figsize=(10, 6))
    plt.plot(fr['year'], fr['indice_100'], 'o-', label='Indice base 100 (1820)', markersize=4, linewidth=1)
    
    plt.xlabel('Année')
    plt.ylabel('Indice (base 100 en 1820)')
    plt.title('Évolution de la part du top 1% - Indice base 100')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend()
    plt.tight_layout()
    
    return plt

def graphique_indice_comparaison(fr, annee_base2=1950):
    ''' Comparer deux indices avec années de base différentes '''
    
    premiere_valeur2 = fr[fr['year'] == annee_base2]['top1'].values[0]
    fr['top1_base100_2'] = (fr['top1'] / premiere_valeur2) * 100
    
    plt.figure(figsize=(10, 6))
    plt.plot(fr['year'], fr['top1_base100'], 'o-', label=f'Indice base 100 (1820)', markersize=4, linewidth=1)
    plt.plot(fr['year'], fr['top1_base100_2'], 's-', label=f'Indice base 100 ({annee_base2})', markersize=4, linewidth=1)
    
    plt.xlabel('Année')
    plt.ylabel('Indice (base 100)')
    plt.title('Comparaison des indices base 100')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend()
    plt.tight_layout()
    
    return plt

def graphique_barres_variations(fr):
    ''' Tracer diagramme en barres de delta_pts par année '''
    
    plt.figure(figsize=(12, 6))
    colors = ['green' if x > 0 else 'red' for x in fr['delta_pts']]
    plt.bar(fr['year'], fr['delta_pts'], color=colors, alpha=0.7, width=2)
    
    plt.xlabel('Année')
    plt.ylabel('Variation (points de pourcentage)')
    plt.title('Variations annuelles de la part du top 1%')
    plt.grid(True, alpha=0.3, linestyle='--', axis='y')
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
    plt.tight_layout()
    
    return plt

def export_figures(fr):
    ''' Exporter les figures dans TP5/plots/ '''
    
    os.makedirs("TP5/plots", exist_ok=True)
    
    # Graphique top1 + mm3
    plt1 = graphique_top1_mm3(fr)
    plt1.savefig("TP5/plots/top1_mm3.png", dpi=150, bbox_inches="tight")
    plt1.close()
    print("Figure exportée : TP5/plots/top1_mm3.png")
    
    # Graphique indice base 100
    plt2 = graphique_indice_base100(fr)
    plt2.savefig("TP5/plots/indice_base100.png", dpi=150, bbox_inches="tight")
    plt2.close()
    print("Figure exportée : TP5/plots/indice_base100.png")
    
    # Diagramme en barres des variations
    plt3 = graphique_barres_variations(fr)
    plt3.savefig("TP5/plots/variations_barres.png", dpi=150, bbox_inches="tight")
    plt3.close()
    print("Figure exportée : TP5/plots/variations_barres.png")

def export_csv(fr):
    ''' Exporter les données en CSV '''
    
    colonnes_utiles = ['year', 'top1', 'indice_100', 'delta_pts', 'delta_pct', 'mm3', 'periode']
    colonnes_existantes = [col for col in colonnes_utiles if col in fr.columns]
    fr_export = fr[colonnes_existantes]
    
    os.makedirs("out", exist_ok=True)
    fr_export.to_csv("out/france_top1_L2.csv", index=False)
    print("Données exportées : out/france_top1_L2.csv")

