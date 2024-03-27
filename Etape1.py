from matplotlib import pyplot as plt
import pandas as pd
from OuvrirFichier import ouvrirfichier

chemin_fichier = "MAT-SMS_Al-Dujaili_bbob-biobj/d05/1-separable_1-separable/bbob-biobj_f01_d05_hyp.tdat"
df = ouvrirfichier(chemin_fichier)
print(df)

df_instance_1 = df[df['instance'] == 1]

plt.figure(figsize=(10, 6))
plt.plot(df_instance_1['function evaluation'], df_instance_1['indicator value'], marker='o', linestyle='',markersize=5)
plt.title('Graphe de l\'instance 1')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.xscale('log')
plt.yscale('log')
plt.show()

# Obtenir la liste des instances uniques
instances = df['instance'].unique()

# Tracer le graphe en utilisant une échelle logarithmique
plt.figure(figsize=(10, 6))
for instance in instances:
    df_instance = df[df['instance'] == instance]
    plt.plot(df_instance['function evaluation'], df_instance['indicator value'], marker='o', linestyle='',markersize=5, label=f'Instance {instance}')
plt.title('Graphe de toutes les instances (échelle logarithmique)')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

# Agréger les données pour toutes les instances
df_aggregated = df.groupby('function evaluation')['indicator value'].agg([ 'median', 'min', 'max']).reset_index()

# Tracer le graphe agrégé
plt.figure(figsize=(10, 6))
plt.plot(df_aggregated['function evaluation'], df_aggregated['median'], label='Median', color='red')
plt.fill_between(df_aggregated['function evaluation'], df_aggregated['min'], df_aggregated['max'], alpha=0.2, color='gray', label='Min-Max Range')
plt.title('Graphe agrégé de toutes les instances')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()



