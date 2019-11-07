#Importa a biblioteca do SQLite para usar o banco
import sqlite3



#Importa tudo que tem dentro do arquivo aluno.py
import aluno

################################
###### Programa principal ######
################################

# Cria a conexão com o banco de dados
conexao = sqlite3.connect("banco.sqlite")

# Executa o procedimento
aluno.criarTabela_aluno(conexao)

#Executa o procedimento
aluno.inserirDados_aluno(conexao)


#Fecha a conexão
conexao.close()