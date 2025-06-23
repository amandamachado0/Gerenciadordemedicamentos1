import tkinter as tk
from tkinter import messagebox

medicamentos = {}


def adicionar_medicamento():
    nome = entrada_nome.get()
    horarios_str = entrada_horarios.get()
    quantidade_str = entrada_quantidade.get()

    try:
        quantidade = int(quantidade_str)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.")
        return

    horarios = [h.strip() for h in horarios_str.split(',')]
    
    medicamentos[nome] = {
        'horarios': horarios,
        'quantidade': quantidade
    }

    
    entrada_nome.delete(0, tk.END)
    entrada_horarios.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)

    messagebox.showinfo("Sucesso", f"Medicamento '{nome}' cadastrado com sucesso!")

def remover_medicamento():
    nome = entrada_remover.get()
    if nome in medicamentos:
        del medicamentos[nome]
        messagebox.showinfo("Removido", f"Medicamento '{nome}' removido com sucesso.")
        entrada_remover.delete(0, tk.END)
        mostrar_medicamentos()
    else:
        messagebox.showwarning("Não encontrado", f"Medicamento '{nome}' não encontrado.")


def mostrar_medicamentos():
    texto_saida.delete(1.0, tk.END)
    if not medicamentos:
        texto_saida.insert(tk.END, "Nenhum medicamento cadastrado.")
    else:
        for nome, dados in medicamentos.items():
            texto_saida.insert(tk.END, f"\nMedicamento: {nome}\n")
            texto_saida.insert(tk.END, f"  Horários: {', '.join(dados['horarios'])}\n")
            texto_saida.insert(tk.END, f"  Quantidade: {dados['quantidade']} comprimido(s)\n")


janela = tk.Tk()
janela.title("Gerenciador de Medicamentos")


tk.Label(janela, text="Nome do medicamento:").pack()
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

tk.Label(janela, text="Horários (separados por vírgula):").pack()
entrada_horarios = tk.Entry(janela, width=40)
entrada_horarios.pack()

tk.Label(janela, text="Quantidade de comprimidos por horário:").pack()
entrada_quantidade = tk.Entry(janela, width=40)
entrada_quantidade.pack()

tk.Button(janela, text="Adicionar medicamento", command=adicionar_medicamento).pack(pady=1)
tk.Button(janela, text="Mostrar medicamentos cadastrados", command=mostrar_medicamentos).pack(pady=1)

texto_saida = tk.Text(janela, height=15, width=60)
texto_saida.pack(pady=10)

tk.Label(janela, text="Nome do medicamento para remover:").pack()
entrada_remover = tk.Entry(janela, width=40)
entrada_remover.pack()
tk.Button(janela, text="Remover medicamento", command=remover_medicamento).pack(pady=5)


janela.mainloop()
