# Imports
from customtkinter import *
from CTkListbox import *


# Variaveis globais

dados = [] # matriz que guarda os valores do dataset alocados na memória principal

quantidade_coletada = 30 # Quantidade de países coletados do dataset


# Classes de objeto
class SearchBar:
    def __init__(self, window_root):
        # Create and place widgets
        self.search_entry = CTkEntry(window_root, placeholder_text="Pesquise pelo país", width=350, font=("arial bold", 20), corner_radius=0)
        self.search_entry.grid(row=1, column=2, padx=padx, pady=pady, ipadx=padxi, ipady=padyi)
        self.search_entry.bind("<KeyRelease>", self.update_list)

        self.search_button = CTkButton(window_root, text="Buscar", command=self.search, width=40, corner_radius=0, bg_color='transparent', font=("arial bold", 18))
        self.search_button.grid(row=1, column=2, padx=(280, 0), pady=pady, ipadx=padxi, ipady=6)

        self.listbox = CTkListbox(window_root, command=self.select_item, width=320, height=250, font=("arial", 25))
        self.listbox.grid(row=2, column=2, padx=padx, pady=pady, ipadx=padxi, ipady=padyi, rowspan=2)


        # Populate initial listbox
        self.update_listbox(countrys[:quantidade_coletada])

    def update_list(self, event=None):
        search_text = self.search_entry.get().lower()
        filtered_data = [item for item in countrys[:quantidade_coletada] if search_text in item.lower()]
        self.update_listbox(filtered_data)


    def update_listbox(self, items):
        self.listbox.delete(0, END)
        for item in items:
            self.listbox.insert(END, item)

    
    def select_item(self, selected):
        self.search_entry.delete(0, END)
        self.search_entry.insert(0, selected)
    
    def search(self):
        if self.search_entry.get() != "":
            country_select(self.search_entry.get())



# Funções
## Faz a leitura do dataset e aloca seus valores na memória
def read_dataset(dataset_url):
    global dados
    dataset = open(dataset_url, 'r')

    for linha in dataset:
        info = linha.strip()
        dados.append(info.split(","))
    
    dataset.close()


def country_select(selected):
    global dados
    rankf = 0
    ouro = 0
    prata = 0
    bronze = 0
    code = 0


    for linha in dados:
        if selected.title() == linha[1]:
            rankf = linha[0]
            ouro = linha[3]
            prata = linha[4]
            bronze = linha[5]
            code = linha[6]
    
    if selected.title() in "Big Data":
        rank.configure(text="Isso é um easter egg")
        rank_ouro.configure(text="ERROR: Luana não encontrada")
        rank_silver.configure(text="Era melhor ver o filme do pelé")
        rank_bronze.configure(text="Shadow o ouriço...")
        total_medalhas.configure(text="Vim fazer um anúncio")
    elif rankf == 0:
        rank.configure(text="País não encontrado")
        rank_ouro.configure(text="País não encontrado")
        rank_silver.configure(text="País não encontrado")
        rank_bronze.configure(text="País não encontrado")
        total_medalhas.configure(text="País não encontrado")
    else:
        rank.configure(text=f"Rank: {rankf}")
        rank_ouro.configure(text=f"Ouro: {ouro}")
        rank_silver.configure(text=f"Prata: {prata}")
        rank_bronze.configure(text=f"Bronze: {bronze}")
        total_medalhas.configure(text=f"Total: {code}")



if __name__ == "__main__":

    w = 300
    h = 100
    padx = (0, 0)
    pady = 15
    padxi = "5px"
    padyi = "5px"
    borda = 10

    # Inicializa a interface gráfica
    window = CTk()
    # faz a leitura do dataset
    read_dataset("_datasets/olympics2024.csv")


    # Configurações iniciais da tela
    window.title("Manipulador de dataset") # nome da janela atual
    window.geometry("1280x620") # tamanho da janela atual
    window.grid_columnconfigure((0, 2), weight=1)
    window.resizable(False, False) # tamanho movel da janela atual

    # Declaracão de frames
    frame_rank = CTkFrame(window, width=400, height=620, corner_radius=0).grid(row = 0, column = 0, rowspan=5)
    frame_country = CTkFrame(window, width=400, height=620, corner_radius=0).grid(row = 0, column = 1, rowspan=5)
    frame_control = CTkFrame(window, width=400, height=620, corner_radius=0).grid(row = 0, column = 2, rowspan=5)

    # divisão da coluna dos paises
    countrys = []
    for linha in dados:
        if linha[1] != "Country":
            countrys.append(linha[1])


    # Conteudo do frame de rank

    CTkLabel(window, w, h, text="Rank nas olimpiadas:", font=("arial bold", 21), corner_radius=borda).grid(row=0, column=0, padx=padx, pady=pady, ipadx=padxi, ipady=padyi)
    rank = CTkLabel(window, w, h, text="Selecione o país", font=("arial bold", 21), corner_radius=borda)
    rank.grid(row=1, column=0, padx=padx, pady=pady, ipadx=padxi, ipady=padyi, rowspan=2)

    # Conteudo do frame de medalhas

    CTkLabel(window, w, h, text="Medalhas obtidas:", font=("arial bold", 21), corner_radius=borda).grid(row=0, column=1, padx=padx, pady=pady, ipadx=padxi, ipady=padyi)
    ## Ouro
    rank_ouro = CTkLabel(window, w, h, text="Medalhas de ouro", font=("arial bold", 21), corner_radius=borda)
    rank_ouro.grid(row=1, column=1, padx=padx, pady=pady, ipadx=padxi, ipady=padyi)
    ## Prata
    rank_silver = CTkLabel(window, w, h, text="Medalhas de prata", font=("arial bold", 21), corner_radius=borda)
    rank_silver.grid(row=2, column=1, padx=padx, pady=pady, ipadx=padxi, ipady=padyi)
    # Bronze
    rank_bronze = CTkLabel(window, w, h, text="Medalhas de bronze", font=("arial bold", 21), corner_radius=borda)
    rank_bronze.grid(row=3, column=1, padx=padx, pady=pady, ipadx=padxi, ipady=padyi)

    # Conteudo do frame de controle
    CTkLabel(window, w, h, text="Escolha o país:", font=("arial bold", 21), corner_radius=borda).grid(row=0, column=2, padx=padx, pady=pady, ipadx=padxi, ipady=padyi)


    total_medalhas = CTkLabel(window, w, h, text="Total de medalhas", font=("arial bold", 21), corner_radius=borda)
    total_medalhas.grid(row=3, column=0, padx=padx, pady=pady, ipadx=padxi, ipady=padyi)

    search_bar = SearchBar(window)

    # main loop
    window.mainloop()
    # End
