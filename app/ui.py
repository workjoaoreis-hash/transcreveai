import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from app.transcriber import transcrever

CYAN = "#00E5FF"
BG = "#111111"
CARD = "#181818"
TEXT = "#FFFFFF"
MUTED = "#B0B0B0"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TranscreveAI")
        self.geometry("760x520")
        self.configure(fg_color=BG)

        self.arquivo = None
        self.txt_final = None

        self.main = ctk.CTkFrame(self, fg_color=BG)
        self.main.pack(fill="both", expand=True, padx=40, pady=35)

        ctk.CTkLabel(
            self.main,
            text="🎙️",
            font=("Arial", 44)
        ).pack(pady=(0, 5))

        ctk.CTkLabel(
            self.main,
            text="TranscreveAI",
            font=("Arial", 34, "bold"),
            text_color=TEXT
        ).pack()

        ctk.CTkLabel(
            self.main,
            text="Da voz ao conhecimento.",
            font=("Arial", 15),
            text_color=MUTED
        ).pack(pady=(5, 25))

        self.drop = ctk.CTkFrame(
            self.main,
            fg_color=CARD,
            corner_radius=22,
            border_width=2,
            border_color=CYAN,
            height=150
        )
        self.drop.pack(fill="x", pady=(0, 22))
        self.drop.pack_propagate(False)

        self.label_video = ctk.CTkLabel(
            self.drop,
            text="📹 Nenhum vídeo selecionado\n\nClique em “Escolher vídeo”",
            font=("Arial", 16),
            text_color=TEXT
        )
        self.label_video.pack(expand=True)

        self.btn_escolher = ctk.CTkButton(
            self.main,
            text="Escolher vídeo",
            command=self.escolher_video,
            width=280,
            height=44,
            fg_color=CYAN,
            text_color="#000000",
            hover_color="#00BFD6",
            font=("Arial", 15, "bold")
        )
        self.btn_escolher.pack(pady=6)

        self.btn_transcrever = ctk.CTkButton(
            self.main,
            text="Transcrever",
            command=self.transcrever_video,
            width=280,
            height=44,
            fg_color="#FFFFFF",
            text_color="#000000",
            hover_color="#DADADA",
            font=("Arial", 15, "bold")
        )
        self.btn_transcrever.pack(pady=6)

        self.status = ctk.CTkLabel(
            self.main,
            text="Status: aguardando...",
            font=("Arial", 14),
            text_color=MUTED
        )
        self.status.pack(pady=(18, 10))

        self.actions = ctk.CTkFrame(self.main, fg_color=BG)
        self.actions.pack(pady=5)

        self.btn_abrir_txt = ctk.CTkButton(
            self.actions,
            text="Abrir TXT",
            command=self.abrir_txt,
            width=135,
            height=38,
            state="disabled",
            fg_color=CARD,
            border_width=1,
            border_color=CYAN,
            text_color=TEXT,
            hover_color="#222222"
        )
        self.btn_abrir_txt.grid(row=0, column=0, padx=8)

        self.btn_abrir_pasta = ctk.CTkButton(
            self.actions,
            text="Abrir pasta",
            command=self.abrir_pasta,
            width=135,
            height=38,
            state="disabled",
            fg_color=CARD,
            border_width=1,
            border_color=CYAN,
            text_color=TEXT,
            hover_color="#222222"
        )
        self.btn_abrir_pasta.grid(row=0, column=1, padx=8)

    def escolher_video(self):
        arquivo = filedialog.askopenfilename(
            title="Escolha um vídeo",
            filetypes=[
                ("Vídeos", "*.mov *.mp4 *.mkv *.m4a"),
                ("Todos os arquivos", "*.*")
            ]
        )

        if arquivo:
            self.arquivo = arquivo
            self.txt_final = None
            self.label_video.configure(
                text=f"📹 {os.path.basename(arquivo)}"
            )
            self.status.configure(text="Status: vídeo selecionado.")
            self.btn_abrir_txt.configure(state="disabled")
            self.btn_abrir_pasta.configure(state="disabled")

    def transcrever_video(self):
        if not self.arquivo:
            messagebox.showwarning("Aviso", "Escolha um vídeo primeiro.")
            return

        self.status.configure(text="Status: transcrevendo... aguarde.")
        self.btn_transcrever.configure(state="disabled")
        self.update()

        try:
            saida = transcrever(self.arquivo)
            self.txt_final = saida

            self.status.configure(text="Status: concluído.")
            self.btn_transcrever.configure(state="normal")
            self.btn_abrir_txt.configure(state="normal")
            self.btn_abrir_pasta.configure(state="normal")

            messagebox.showinfo(
                "Concluído",
                f"Transcrição salva em:\n\n{saida}"
            )

        except Exception as erro:
            self.status.configure(text="Status: erro.")
            self.btn_transcrever.configure(state="normal")
            messagebox.showerror("Erro", str(erro))

    def abrir_txt(self):
        if self.txt_final:
            os.system(f'open "{self.txt_final}"')

    def abrir_pasta(self):
        if self.txt_final:
            pasta = os.path.dirname(self.txt_final)
            os.system(f'open "{pasta}"')


def iniciar():
    App().mainloop()

    