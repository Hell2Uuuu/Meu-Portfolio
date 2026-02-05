import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text


connection_string = 'sqlite:///galo_stats.db'
engine = create_engine(connection_string)



print("--- INICIANDO ---")

try:
    #LEITURA
    print("Lendo arquivo CSV...")
   
    df = pd.read_csv('/data/jogos_brasileirao.csv') 

    #FILTRAGEM (ETL)
    print("Filtrando jogos do Galo...")
    galo_df = df[(df['home_team'] == 'Atlético-MG') | (df['away_team'] == 'Atlético-MG')].copy()

    # Lógica de Pontos
    def get_points(row):
        if row['home_team'] == 'Atlético-MG':
            if row['home_score'] > row['away_score']: return 3
            elif row['home_score'] == row['away_score']: return 1
        else:
            if row['away_score'] > row['home_score']: return 3
            elif row['away_score'] == row['home_score']: return 1
        return 0

    galo_df['pontos'] = galo_df.apply(get_points, axis=1)

    #CARGA NO SQL
    print("Salvando no MySQL...")
    galo_df.to_sql('historico_partidas', con=engine, if_exists='replace', index=False)
    
    #GRÁFICO
    print("Gerando gráfico...")
    df_anual = galo_df.groupby('year')['pontos'].sum().reset_index()
    
    plt.bar(df_anual['year'], df_anual['pontos'], color='black')
    plt.title("Pontos do Galo por Ano")
    plt.savefig('grafico_galo.png')
    print("Sucesso! Gráfico salvo como 'grafico_galo.png'")

except FileNotFoundError:
    print("ERRO: O arquivo 'jogos_brasileirao.csv' não foi encontrado na pasta D:\\project.")
    print("Verifique se o nome do arquivo está correto e se ele está na mesma pasta do script.")
except Exception as e:
    print(f"Outro erro ocorreu: {e}")
    print("Exportando dados para o Power BI...")
galo_df.to_csv('base_dados_galo_powerbi.csv', index=False, encoding='utf-8-sig')
print("Arquivo 'base_dados_galo_powerbi.csv' criado com sucesso!")