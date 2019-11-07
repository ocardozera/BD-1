# PROCEDIMENTO: Recebe a conexão e cria uma tabela

def criarTabela_aluno(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada nele para podermos executar nosso SQL
    cursor = conexao.cursor()
    
    # Monta o SQL a ser executado
    sql = """
    CREATE TABLE IF NOT EXISTS aluno (
        idaluno SERIAL NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        login TEXT NOT NULL,
        senha TEXT NOT NULL
        ); """

    #Executa o SQL
    cursor.execute(sql)


# Procedimento que recebe a conexão
# Inserir, alterar e excluir são Procedimentos parecidos
def inserirDados_aluno(conexao):

    #Pede os dados ao aluno
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")

    #Cria o cursor
    cursor = conexao.cursor()

    #Monta o SQL
    sql = """
    INSERT INTO aluno (nome, login, senha) VALUES (
        nome = "{}",
        login = "{}",
        senha = "{}"
    );
    """.format(nome, login, senha)

    #Executa
    cursor.execute(sql)

    # Quanto insere, altera ou exclui tem que fazer o commit
    # Que é como se fosse um "salvar" para registrar as alterações feitas
    conexao.commit()

    

