from view import SuspeitoView
from presenter import SuspeitoPresenter

if __name__ == "__main__":
    v = SuspeitoView()
    p = SuspeitoPresenter(v)
   
    # Loop de execução
    while True:
        op = v.exibir_menu()
        if op == '1': 
            nome, crime, nivel = v.obter_dados_novo_suspeito()
            p.adicionar_suspeito(nome, crime, nivel)
        elif op == '2': 
            p.listar_suspeitos()
        elif op == '0': 
            break