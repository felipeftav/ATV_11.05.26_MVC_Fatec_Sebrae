from model import SuspeitoModel
from view import SuspeitoView
            
class SuspeitoPresenter:
    def __init__(self, view):
        self.model = SuspeitoModel()
        self.view = view

    def adicionar_suspeito(self, nome, crime, nivel):
        if nome and crime and nivel:
            try:
                self.model.salvar_suspeito(nome, crime, nivel)
                self.view.exibir_sucesso("Suspeito fichado no sistema.")
            except ValueError:
                self.view.exibir_erro("Nível de perigo deve ser um número!")
        else:
            self.view.exibir_erro("Dados inválidos!")

    def listar_suspeitos(self):
        # O Presenter busca os dados brutos no Model
        dados_brutos = self.model.listar_todos()
       
        # O Presenter TRADUZ os dados para um formato que a View entenda
        # (Isso é a essência do MVP)
        dados_limpos = [f"ID #{s[0]}: {s[1].upper()} (Delito: {s[2]} | Perigo: {s[3]})" for s in dados_brutos]
       
        self.view.mostrar_tabela_suspeitos(dados_limpos)
        
        quantidade_total = len(dados_brutos)
        
        self.view.exibir_total(quantidade_total)