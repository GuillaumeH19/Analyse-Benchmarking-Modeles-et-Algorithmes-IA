from matplotlib import pyplot as plt
import pandas as pd
from OuvrirFichier import ouvrirfichier

chemin_fichier = "MAT-SMS_Al-Dujaili_bbob-biobj/d05/1-separable_1-separable/bbob-biobj_f01_d05_hyp.tdat"
df = ouvrirfichier(chemin_fichier)

chemin_fichier = "DEMO_Tusar_bbob-biobj/d05/1-separable_1-separable/bbob-biobj_f01_d05_hyp.tdat"
df2 = ouvrirfichier(chemin_fichier)

chemin_fichier = "RANDOMSEARCH-5_Auger_bbob-biobj/d05/1-separable_1-separable/bbob-biobj_f01_d05_hyp.tdat"
df3 = ouvrirfichier(chemin_fichier)

print(df)
print(df2)
print(df3)

df_instance_1 = df[df['instance'] == 1]
df_instance_2 = df2[df2['instance'] == 1]
df_instance_3 = df3[df3['instance'] == 1]

plt.figure(figsize=(10, 6))
plt.plot(df_instance_1['function evaluation'], df_instance_1['indicator value'], marker='o', linestyle='',markersize=5,label=f'MAT-SMS', color='red')
plt.plot(df_instance_2['function evaluation'], df_instance_2['indicator value'], marker='o', linestyle='',markersize=5, label=f'DEMO', color='blue')
plt.plot(df_instance_3['function evaluation'], df_instance_3['indicator value'], marker='o', linestyle='',markersize=5, label=f'RANDOMSEARCH-5', color='green')
plt.title('Graphe de l\'instance 1')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

instances = df['instance'].unique()
instances2 = df2['instance'].unique()
instances3 = df3['instance'].unique()

label_prob1 = 'MAT-SMS'
label_prob2 = 'DEMO'
label_prob3 = 'RANDOMSEARCH-5'

plt.figure(figsize=(10, 6))
for instance in instances:
    df_instance = df[df['instance'] == instance]
    df_instance2 = df2[df2['instance'] == instance]
    df_instance3 = df3[df3['instance'] == instance]
    plt.plot(df_instance['function evaluation'], df_instance['indicator value'], marker='o', linestyle='',markersize=3, label=label_prob1,color='red')
    plt.plot(df_instance2['function evaluation'], df_instance2['indicator value'], marker='o', linestyle='',markersize=3, label=label_prob2,color='blue')
    plt.plot(df_instance3['function evaluation'], df_instance3['indicator value'], marker='o', linestyle='',markersize=3, label=label_prob3,color='green')
    label_prob1 = ''
    label_prob2 = ''
    label_prob3 = ''

plt.title('Graphe de toutes les instances')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

df_aggregated = df.groupby('function evaluation')['indicator value'].agg([ 'median', 'min', 'max']).reset_index()
df_aggregated2 = df2.groupby('function evaluation')['indicator value'].agg([ 'median', 'min', 'max']).reset_index()
df_aggregated3 = df3.groupby('function evaluation')['indicator value'].agg([ 'median', 'min', 'max']).reset_index()

plt.figure(figsize=(10, 6))
plt.plot(df_aggregated['function evaluation'], df_aggregated['median'], label='MAT-SMS', color='red')
plt.fill_between(df_aggregated['function evaluation'], df_aggregated['min'], df_aggregated['max'], alpha=0.5, color='red', label='Min-Max Range')
plt.plot(df_aggregated2['function evaluation'], df_aggregated2['median'], label='DEMO', color='blue')
plt.fill_between(df_aggregated2['function evaluation'], df_aggregated2['min'], df_aggregated2['max'], alpha=0.5, color='blue', label='Min-Max Range')
plt.plot(df_aggregated3['function evaluation'], df_aggregated3['median'], label='RANDOMSEARCH-5', color='green')
plt.fill_between(df_aggregated3['function evaluation'], df_aggregated3['min'], df_aggregated3['max'], alpha=0.5, color='green', label='Min-Max Range')
plt.title('Graphe agrégé de toutes les instances')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()