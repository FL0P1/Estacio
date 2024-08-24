import tkinter as tk
from tkinter import messagebox

class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = self.calcular_media()
        self.status = self.verificar_status()

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def verificar_status(self):
        return "Aprovado" if self.media >= 6 else "Reprovado"

class SistemaNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Notas - CRUD")
        
        self.alunos_db = {}  # Dicionário para armazenar os alunos
        
        # Labels e Entradas
        self.lbl_nome = tk.Label(root, text="Nome do Aluno:")
        self.lbl_nome.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)
        
        self.lbl_nota1 = tk.Label(root, text="Nota 1:")
        self.lbl_nota1.grid(row=1, column=0, padx=10, pady=5)
        self.entry_nota1 = tk.Entry(root)
        self.entry_nota1.grid(row=1, column=1, padx=10, pady=5)
        
        self.lbl_nota2 = tk.Label(root, text="Nota 2:")
        self.lbl_nota2.grid(row=2, column=0, padx=10, pady=5)
        self.entry_nota2 = tk.Entry(root)
        self.entry_nota2.grid(row=2, column=1, padx=10, pady=5)
        
        self.lbl_nota3 = tk.Label(root, text="Nota 3:")
        self.lbl_nota3.grid(row=3, column=0, padx=10, pady=5)
        self.entry_nota3 = tk.Entry(root)
        self.entry_nota3.grid(row=3, column=1, padx=10, pady=5)
        
        # Botões de Ação
        self.btn_adicionar = tk.Button(root, text="Adicionar/Atualizar Aluno", command=self.adicionar_atualizar_aluno)
        self.btn_adicionar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        self.btn_deletar = tk.Button(root, text="Deletar Aluno", command=self.deletar_aluno)
        self.btn_deletar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        self.btn_listar = tk.Button(root, text="Listar Alunos", command=self.listar_alunos)
        self.btn_listar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        self.txt_output = tk.Text(root, height=10, width=50)
        self.txt_output.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def adicionar_atualizar_aluno(self):
        nome = self.entry_nome.get()
        try:
            nota1 = float(self.entry_nota1.get())
            nota2 = float(self.entry_nota2.get())
            nota3 = float(self.entry_nota3.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos nas notas.")
            return

        aluno = Aluno(nome, nota1, nota2, nota3)
        self.alunos_db[nome] = aluno
        messagebox.showinfo("Sucesso", f"Aluno {nome} adicionado/atualizado com sucesso!")
        self.limpar_campos()

    def deletar_aluno(self):
        nome = self.entry_nome.get()
        if nome in self.alunos_db:
            del self.alunos_db[nome]
            messagebox.showinfo("Sucesso", f"Aluno {nome} deletado com sucesso!")
        else:
            messagebox.showerror("Erro", f"Aluno {nome} não encontrado.")
        self.limpar_campos()

    def listar_alunos(self):
        self.txt_output.delete(1.0, tk.END)
        if not self.alunos_db:
            self.txt_output.insert(tk.END, "Nenhum aluno cadastrado.\n")
        else:
            for nome, aluno in self.alunos_db.items():
                self.txt_output.insert(tk.END, f"Nome: {nome}\nMédia: {aluno.media:.2f}\nStatus: {aluno.status}\n\n")
    
    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_nota1.delete(0, tk.END)
        self.entry_nota2.delete(0, tk.END)
        self.entry_nota3.delete(0, tk.END)

# Inicialização da interface gráfica
root = tk.Tk()
app = SistemaNotas(root)
root.mainloop()
