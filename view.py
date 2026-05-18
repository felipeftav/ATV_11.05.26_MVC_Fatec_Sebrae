#
# class SuspeitoView:
#     def exibir_menu(self):
#         print("\n--- 🕵️ DATA VAULT PRO (MVC) ---")
#         print("1. Cadastrar Suspeito")
#         print("2. Listar Todos")
#         print("0. Sair")
#         return input("Escolha uma opção: ")

#     def obter_dados_suspeito(self):
#         nome = input("Nome do meliante: ")
#         crime = input("Delito: ")
#         nivel = input("Nível de perigo (1-10): ")
#         return nome, crime, nivel

#     def mostrar_lista(self, suspeitos):
#         print("\n--- 📋 FICHA CRIMINAL ---")
#         for s in suspeitos:
#             print(f"ID: {s[0]} | Suspeito: {s[1]} | Crime: {s[2]} | Perigo: {s[3]}/10")

#     def mostrar_mensagem(self, msg):
#         print(f" system >> {msg}")

class SuspeitoView:
    # A View agora apenas recebe ordens do que imprimir
    def exibir_sucesso(self, mensagem):
        print(f"\n[OK] {mensagem}")

    def exibir_erro(self, mensagem):
        print(f"\n[ERRO] {mensagem}")

    def mostrar_tabela_suspeitos(self, lista_formatada):
        print("\n--- RELATÓRIO DE INVESTIGAÇÃO ---")
        for linha in lista_formatada:
            print(linha)

    def obter_input_usuario(self, prompt):
        return input(prompt)

    def exibir_menu(self):
        print("\n1. Adicionar | 2. Listar | 0. Sair")
        return self.obter_input_usuario("Escolha: ")

    def obter_dados_novo_suspeito(self):
        nome = self.obter_input_usuario("Nome: ")
        crime = self.obter_input_usuario("Crime: ")
        nivel = self.obter_input_usuario("Nível de perigo (1-10): ")
        return nome, crime, nivel
    
    def exibir_total(self, total):
        print(f"\nTotal de suspeitos cadastrados: {total}")