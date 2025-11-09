from data_analysis import *
from visualisation import export_figures, export_csv


def run_data_analysis():
    ''' Run data_analysis module '''

    data_loaded = load_dataset()
    column_rename = rename_column(data_loaded)
    data_cleaned = clean_columns(column_rename)
    data_convert = convert_columns(data_cleaned)
    fr_filter = filter_entity(data_convert)
    data_check = check_data(fr_filter)
    data_stats = stats_descriptives(data_check)
    data_derivative = derivative_features(data_check)
    data_variation = variation(data_derivative)
    data_gap = gap_data(data_variation)
    data_moving_average = moving_average(data_gap)
    data_graphique = prepare_graphique(data_moving_average)
    data_periode = periode_splitting(data_moving_average)
    
    return data_loaded, data_cleaned, column_rename, data_convert, fr_filter, data_check, data_stats, data_derivative, data_variation, data_gap, data_graphique, data_periode

def run_visualisation_export(fr):
    ''' Générer les graphiques et exporter '''
    
    export_figures(fr)
    export_csv(fr)

def main():
    ''' Run complete analysis '''
    
    results = run_data_analysis()
    data_periode = results[-1]
    
    run_visualisation_export(data_periode)
    
    print('Traitement complet terminé')

if __name__ == "__main__":
    main()
    
