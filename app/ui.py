import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from app.transcriber import transcrever


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TranscreveAI")
        self.geometry("650x300")

        self.arquivo = None

        ctk.CTkLabel(self, text="🎙️ TranscreveAI", font=("Arial", 28, "bold")).pack(pady=30)

        self.label = ctk.CTkLabel(self, text="Nenhum vídeo selecionado")
        self.label.pack(pady=10)

        ctk.CTkButton(self, text="Escolher vídeo", command=self.escolher_video, width=250).pack(pady=10)
        ctk.CTkButton(self, text="Transcrever", command=self.transcrever_video, width=250).pack(pady=10)

    def escolher_video(self):
        self.arquivo = filedialog.askopenfilename(
            title="Escolha um vídeo",
            filetypes=[("Vídeos", "*.mov *.mp4 *.mkv *.m4a")]
        )
        if self.arquivo:
            self.label.configure(text=os.path.basename(self.arquivo))

    def transcrever_video(self):
        if not self.arquivo:
            messagebox.showwarning("Aviso", "Escolha um vídeo primeiro.")
            return

        saida = transcrever(self.arquivo)
        messagebox.showinfo("Concluído", f"Transcrição salva em:\n\n{saida}")
        os.system(f'open "{saida}"')


def iniciar():
    App().mainloop()
