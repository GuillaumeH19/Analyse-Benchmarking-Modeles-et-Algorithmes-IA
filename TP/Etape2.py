from matplotlib import pyplot as plt
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

chemin_fichier = "MAT-SMS/bbob-biobj_f01_d05_hyp.tdat"
df = ouvrirfichier(chemin_fichier)

chemin_fichier = "MAT-SMS/bbob-biobj_f20_d05_hyp.tdat"
df2 = ouvrirfichier(chemin_fichier)

print(df)
print(df2)

df_instance_1 = df[df['instance'] == 1]
df_instance_2 = df2[df2['instance'] == 1]

plt.figure(figsize=(10, 6))
plt.plot(df_instance_1['function evaluation'], df_instance_1['indicator value'], marker='o', linestyle='',markersize=5,label=f'Prob1', color='red')
plt.plot(df_instance_2['function evaluation'], df_instance_2['indicator value'], marker='o', linestyle='',markersize=5, label=f'Prob2')
plt.title('Graphe de l\'instance 1')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.grid(True)
plt.legend()
plt.show()

# Obtenir la liste des instances uniques
instances = df['instance'].unique()
instances2 = df2['instance'].unique()
# Tracer le graphe en utilisant une échelle logarithmique
plt.figure(figsize=(10, 6))
for instance in instances:
    df_instance = df[df['instance'] == instance]
    df_instance2 = df2[df2['instance'] == instance]
    plt.plot(df_instance['function evaluation'], df_instance['indicator value'], marker='o', linestyle='-',markersize=5, label=f'Prob 1 Instance {instance}')
    plt.plot(df_instance2['function evaluation'], df_instance2['indicator value'], marker='o', linestyle='-',markersize=5, label=f'Prob 2 Instance {instance}')
plt.title('Graphe de toutes les instances (échelle logarithmique)')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.grid(True)
plt.legend()
plt.show()

# Agréger les données pour toutes les instances
df_aggregated = df.groupby('function evaluation')['indicator value'].agg([ 'median', 'min', 'max']).reset_index()
df_aggregated2 = df2.groupby('function evaluation')['indicator value'].agg([ 'median', 'min', 'max']).reset_index()
# Tracer le graphe agrégé
plt.figure(figsize=(10, 6))
plt.plot(df_aggregated['function evaluation'], df_aggregated['median'], label='Prob 1 Mediane', color='red')
plt.plot(df_aggregated2['function evaluation'], df_aggregated2['median'], label='Prob 2 Mediane', color='blue')
plt.title('Graphe agrégé de toutes les instances')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.grid(True)
plt.legend()
plt.show()
