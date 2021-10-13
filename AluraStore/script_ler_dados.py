################### Lendo dados e criando banco_alura_store ####################
import sqlite3
import pandas as pd

path_banco = "banco_alura_store.sqlite"
connection = sqlite3.connect(path_banco)
cursor = connection.cursor()

def funcao_insere_dados (arquivo):
    sql_file = open(arquivo)
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

# criando tabela de produtos
funcao_insere_dados("financeiro_produtos.sql")

# criando tabela de vendedores
funcao_insere_dados("financeiro_vendedores.sql")

# criando tabela de pedidos
funcao_insere_dados("financeiro_pedidos.sql")

# criando tabela de nota_fiscal
funcao_insere_dados("financeiro_notas_fiscais.sql")

def funcao_salva_excel(connection):
    print("Salvando os dados em excel")
    writer = pd.ExcelWriter(f'dados_alura_store.xlsx',
                            engine='xlsxwriter')

    for i in ('notas_fiscais', "produtos", "pedidos", "vendedores"):
        print(i)
        if(i == 'notas_fiscais'):
            aux = aux\
                .assign(valor_venda = lambda x:
            x['valor_venda'] if x['valor_venda'] < 
        aux = pd.read_sql_query(f"select * from {i}", connection)

        aux.to_excel(writer, sheet_name=i, index=False)
    writer.save()
    writer.close()

funcao_salva_excel(connection)