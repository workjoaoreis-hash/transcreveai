import customtkinter as ctk
from tkinter import filedialog, messagebox
from app.transcriber import transcrever


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("TranscreveAI")
        self.geometry("700x250")

        self.arquivo = None

        self.label = ctk.CTkLabel(
            self,
            text="Nenhum vídeo selecionado"
        )
        self.label.pack(pady=20)

        self.botao_escolher = ctk.CTkButton(
            self,
            text="Escolher vídeo",
            command=self.escolher_video
        )
        self.botao_escolher.pack(pady=10)

        self.botao_transcrever = ctk.CTkButton(
            self,
            text="Transcrever",
            command=self.transcrever_video
        )
        self.botao_transcrever.pack(pady=10)

    def escolher_video(self):

        arquivo = filedialog.askopenfilename(
            filetypes=[
                (
                    "Vídeos",
                    "*.mp4 *.mov *.mkv *.m4a"
                )
            ]
        )

        if arquivo:
            self.arquivo = arquivo
            self.label.configure(text=arquivo)

    def transcrever_video(self):

        if not self.arquivo:
            messagebox.showwarning(
                "Aviso",
                "Escolha um vídeo primeiro."
            )
            return

        self.botao_transcrever.configure(state="disabled")
        self.update()

        try:

            saida = transcrever(self.arquivo)

            messagebox.showinfo(
                "Concluído",
                f"Transcrição salva em:\n\n{saida}"
            )

        except Exception as e:

            messagebox.showerror(
                "Erro",
                str(e)
            )

        self.botao_transcrever.configure(state="normal")


def iniciar():
    app = App()
    app.mainloop()
