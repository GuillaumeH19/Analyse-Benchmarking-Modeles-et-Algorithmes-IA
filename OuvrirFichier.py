import pandas as pd

def ouvrirfichier(chemin_fichier):
    with open(chemin_fichier, 'r') as file:
        lines = file.readlines()

    data = []
    current_instance = None

    # Parcourir chaque ligne du fichier
    for line in lines:
        # Ignorer les lignes de commentaire commençant par '%'
        if line.startswith('%'):
            if 'instance' in line:
                current_instance = int(line.split(',')[0].split('=')[1].strip())
        else:
            values = line.strip().split('\t')
            values.append(current_instance)
            data.append(values)
    df = pd.DataFrame(data, columns=['function evaluation', 'indicator value', 'instance'])
    df['function evaluation'] = df['function evaluation'].astype(float)
    df['indicator value'] = df['indicator value'].astype(float)
    return df
