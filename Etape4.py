from matplotlib import pyplot as plt
import pandas as pd
from OuvrirFichier import ouvrirfichier

chemin_fichier = "MAT-SMS_Al-Dujaili_bbob-biobj/d05/1-separable_1-separable/bbob-biobj_f01_d05_hyp.tdat"
df = ouvrirfichier(chemin_fichier)

chemin_fichier = "MAT-SMS_Al-Dujaili_bbob-biobj/d05/2-moderate_2-moderate/bbob-biobj_f20_d05_hyp.tdat"
df2 = ouvrirfichier(chemin_fichier)

chemin_fichier = "MAT-SMS_Al-Dujaili_bbob-biobj/d05/1-separable_2-moderate/bbob-biobj_f03_d05_hyp.tdat"
df3 = ouvrirfichier(chemin_fichier)

chemin_fichier = "MAT-SMS_Al-Dujaili_bbob-biobj/d05/3-ill-conditioned_4-multi-modal/bbob-biobj_f37_d05_hyp.tdat"
df4 = ouvrirfichier(chemin_fichier)

print(df)
print(df2)
print(df3)
print(df4)

df_instance_1 = df[df['instance'] == 1]
df_instance_2 = df2[df2['instance'] == 1]
df_instance_3 = df3[df3['instance'] == 1]
df_instance_4 = df4[df4['instance'] == 1]

plt.figure(figsize=(10, 6))
plt.plot(df_instance_1['function evaluation'], df_instance_1['indicator value'], marker='o', linestyle='',markersize=5,label=f'1-separable_1-separable', color='red')
plt.plot(df_instance_2['function evaluation'], df_instance_2['indicator value'], marker='o', linestyle='',markersize=5, label=f'2-moderate_2-moderate', color='blue')
plt.plot(df_instance_3['function evaluation'], df_instance_3['indicator value'], marker='o', linestyle='',markersize=5, label=f'1-separable_2-moderate', color='purple')
plt.plot(df_instance_4['function evaluation'], df_instance_4['indicator value'], marker='o', linestyle='',markersize=5, label=f'3-ill-conditioned_4-multi-modal', color='green')
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
instances4 = df4['instance'].unique()

label_prob1 = '1-separable_1-separable'
label_prob2 = '2-moderate_2-moderate'
label_prob3 = '1-separable_2-moderate'
label_prob4 = '3-ill-conditioned_4-multi-modal'

plt.figure(figsize=(10, 6))
for instance in instances:
    df_instance = df[df['instance'] == instance]
    df_instance2 = df2[df2['instance'] == instance]
    df_instance3 = df3[df3['instance'] == instance]
    df_instance4 = df4[df4['instance'] == instance]
    plt.plot(df_instance['function evaluation'], df_instance['indicator value'], marker='o', linestyle='',markersize=3, label=label_prob1,color='red')
    plt.plot(df_instance2['function evaluation'], df_instance2['indicator value'], marker='o', linestyle='',markersize=3, label=label_prob2,color='blue')
    plt.plot(df_instance3['function evaluation'], df_instance3['indicator value'], marker='o', linestyle='',markersize=3, label=label_prob3,color='purple')
    plt.plot(df_instance4['function evaluation'], df_instance4['indicator value'], marker='o', linestyle='',markersize=3, label=label_prob4,color='green')
    label_prob1 = ''
    label_prob2 = ''
    label_prob3 = ''
    label_prob4 = ''

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
df_aggregated4 = df4.groupby('function evaluation')['indicator value'].agg([ 'median', 'min', 'max']).reset_index()

plt.figure(figsize=(10, 6))
plt.plot(df_aggregated['function evaluation'], df_aggregated['median'], label='1-separable_1-separable', color='red')
plt.fill_between(df_aggregated['function evaluation'], df_aggregated['min'], df_aggregated['max'], alpha=0.2, color='red', label='Min-Max Range')
plt.plot(df_aggregated2['function evaluation'], df_aggregated2['median'], label='2-moderate_2-moderate', color='blue')
plt.fill_between(df_aggregated['function evaluation'], df_aggregated2['min'], df_aggregated2['max'], alpha=0.2, color='blue', label='Min-Max Range')
plt.plot(df_aggregated3['function evaluation'], df_aggregated3['median'], label='1-separable_2-moderate', color='purple')
plt.fill_between(df_aggregated['function evaluation'], df_aggregated3['min'], df_aggregated3['max'], alpha=0.2, color='purple', label='Min-Max Range')
plt.plot(df_aggregated4['function evaluation'], df_aggregated4['median'], label='3-ill-conditioned_4-multi-modal', color='green')
plt.fill_between(df_aggregated['function evaluation'], df_aggregated4['min'], df_aggregated4['max'], alpha=0.2, color='green', label='Min-Max Range')
plt.title('Graphe agrégé de toutes les instances')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
