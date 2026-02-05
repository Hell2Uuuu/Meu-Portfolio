# 🐔 Galo Data Intelligence: Pipeline de ETL e Business Intelligence
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Power BI](https://img.shields.io/badge/Power_BI-Analytics-yellow?style=for-the-badge&logo=power-bi)
![SQL](https://img.shields.io/badge/SQL-Database-orange?style=for-the-badge)

> Analisando duas décadas de performance do Clube Atlético Mineiro através de Engenharia de Dados e Visualização Estratégica.


A ideia principal do Projeto
Este projeto visa realizar uma análise profunda do desempenho do Atlético Mineiro no Campeonato Brasileiro (2003-2023). O objetivo foi transformar dados brutos de partidas em insights acionáveis sobre aproveitamento, mando de campo e histórico contra adversários.

🛠️ Tecnologias e Ferramentas
* **Python (Pandas):** Extração, limpeza e transformação dos dados (ETL).
* **SQL (SQLite/MySQL):** Modelagem e persistência dos dados tratados.
* **Power BI:** Criação de dashboard interativo com métricas de BI (DAX).


Pipeline de Dados (ETL)

O processo de engenharia foi dividido em três etapas principais:

1. **Extração:** Consumo de um dataset histórico contendo mais de 8.000 registros de partidas da Série A.
2. **Transformação (Business Rules):** * Filtragem seletiva de partidas onde o Atlético-MG figurava como mandante ou visitante.
   * Desenvolvimento de lógica condicional para determinação de resultados (Vitória, Empate, Derrota) e atribuição de pontuação (3, 1, 0).
3. **Carga:** Exportação dos dados normalizados para banco de dados SQL e arquivos otimizados para consumo em ferramentas de BI.


📈 Dashboard e Insights
O dashboard final foca no storytelling dos dados, permitindo identificar:

* **Evolução Histórica:** O ápice de performance em 2021 com aproveitamento de 74%.
* **Métricas Absolutas:** 780 jogos analisados, acumulando 327 vitórias e um aproveitamento médio histórico de 0,50.
* **Fator Casa:** Comparação direta do aproveitamento como Mandante vs. Visitante, destacando a força do estádio.
* **Análise de Adversários:** Top 5 equipes com maior e menor índice de dificuldade para o clube.

Print do Dashboard

<img width="1174" height="658" alt="image" src="https://github.com/user-attachments/assets/52613fe7-6b99-487a-8044-7483ae68ebb6" />



## 🚀 Como Executar
1. Clone o repositório.
2. Execute o script em `src/main.py` para processar os dados brutos da pasta `data/`.
3. Abra o arquivo `.pbix` na pasta `dashboard/` para visualizar as análises.

---
Autor: Robert Barbosa da Silva 
