import tkinter as tk
from tkinter import messagebox


produtos = []


def cadastrarProduto():
    nome = entrada_nome.get()
    preco = entrada_preco.get()
    quantidade = entrada_quantidade.get()

    if nome == "" or preco == "" or quantidade == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        preco = float(preco)
        quantidade = int(quantidade)
    except:
        messagebox.showerror("Erro", "Digite valores válidos para preço e quantidade!")
        return

    if preco <= 0 or quantidade <= 0:
        messagebox.showwarning("Aviso", "Preço e quantidade devem ser maiores que zero!")
        return

    produto = [nome, preco, quantidade]

    produtos.append(produto)

    messagebox.showinfo("Sucesso", "Produto cadastrado!")

    entrada_nome.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)

def abrirProdutos():

    janela_produtos = tk.Toplevel(janela)
    janela_produtos.title("Produtos Cadastrados")
    janela_produtos.geometry("600x400")

    titulo = tk.Label(
        janela_produtos,
        text="Produtos Cadastrados",
        font=("Arial", 18)
    )
    titulo.pack(pady=20)


    cabecalho = tk.Label(
        janela_produtos,
        text="Produto          Preço          Quantidade",
        font=("Arial", 12, "bold")
    )
    cabecalho.pack()

    # Mostrar produtos
    if len(produtos) == 0:
        mensagem = tk.Label(
            janela_produtos,
            text="Nenhum produto cadastrado."
        )
        mensagem.pack(pady=20)

    else:
        for produto in produtos:

            nome = produto[0]
            preco = produto[1]
            quantidade = produto[2]

            texto = f"{nome}          R$ {preco:}          {quantidade}"

            produto_label = tk.Label(
                janela_produtos,
                text=texto,
                font=("Arial", 11)
            )
            produto_label.pack(pady=5)

    botao_voltar = tk.Button(
        janela_produtos,
        text="Voltar",
        command=janela_produtos.destroy
    )
    botao_voltar.pack(pady=20)


janela = tk.Tk()

janela.title("Gerenciador de Estoque")
janela.geometry("500x450")


titulo = tk.Label(
    janela,
    text="Gerenciador de Estoque",
    font=("Arial", 20)
)
titulo.pack(pady=20)


label_nome = tk.Label(
    janela,
    text="Nome do produto:"
)
label_nome.pack()

entrada_nome = tk.Entry(janela, width=35)
entrada_nome.pack(pady=5)


label_preco = tk.Label(
    janela,
    text="Preço:"
)
label_preco.pack()

entrada_preco = tk.Entry(janela, width=35)
entrada_preco.pack(pady=5)


label_quantidade = tk.Label(
    janela,
    text="Quantidade:"
)
label_quantidade.pack()

entrada_quantidade = tk.Entry(janela, width=35)
entrada_quantidade.pack(pady=5)


botao_cadastrar = tk.Button(
    janela,
    text="Cadastrar Produto",
    command=cadastrarProduto
)
botao_cadastrar.pack(pady=15)


botao_produtos = tk.Button(
    janela,
    text="Ver Produtos",
    command=abrirProdutos
)
botao_produtos.pack()


janela.mainloop()