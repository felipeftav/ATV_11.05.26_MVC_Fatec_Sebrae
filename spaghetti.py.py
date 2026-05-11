import sqlite3

def rodar_sistema_baguncado():
    # CONEXÃO DIRETA NO MEIO DO CÓDIGO
    conexao = sqlite3.connect('vault_original.db')
    cursor = conexao.cursor()
    
    # CRIAÇÃO DE TABELA MISTURADA
    cursor.execute('''CREATE TABLE IF NOT EXISTS suspeitos 
                      (id INTEGER PRIMARY KEY, nome TEXT, crime TEXT, periculosidade INTEGER)''')
    conexao.commit()

    while True:
        print("\n---  ARQUIVO MORTO (SISTEMA ANTIGO) ---")
        print("1. Cadastrar Suspeito")
        print("2. Listar Todos")
        print("0. Sair")
        
        escolha = input("O que deseja? ")

        if escolha == '1':
            # INTERFACE E LÓGICA DE DADOS COLADOS
            nome = input("Nome do meliante: ")
            crime = input("Delito: ")
            nivel = input("Nível de perigo (1-10): ")
            
            # Se o usuário digitar uma letra no nível, o sistema explode aqui!
            # Não há validação separada.
            cursor.execute("INSERT INTO suspeitos (nome, crime, periculosidade) VALUES (?, ?, ?)", 
                           (nome, crime, int(nivel)))
            conexao.commit()
            print("Registro jogado na gaveta!")

        elif escolha == '2':
            # BUSCA E EXIBIÇÃO MISTURADAS
            cursor.execute("SELECT * FROM suspeitos")
            linhas = cursor.fetchall()
            print("\n--- FICHA CRIMINAL ---")
            for linha in linhas:
                # Se mudarmos a ordem das colunas no SQL, esse print quebra!
                print(f"ID: {linha[0]} | Suspeito: {linha[1]} | Crime: {linha[2]} | Perigo: {linha[3]}/10")
        
        elif escolha == '0':
            conexao.close()
            print("Desligando...")
            break
        else:
            print("Comando inválido!")

if __name__ == "__main__":
    rodar_sistema_baguncado()
