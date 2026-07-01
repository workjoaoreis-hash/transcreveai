import threading


class TranscriptionWorker:

    def __init__(self, transcriber, video, callback_ok, callback_error):
        self.transcriber = transcriber
        self.video = video
        self.callback_ok = callback_ok
        self.callback_error = callback_error

    def start(self):
        thread = threading.Thread(
            target=self._run,
            daemon=True
        )
        thread.start()

    def _run(self):
        try:
            resultado = self.transcriber(self.video)
            self.callback_ok(resultado)
        except Exception as e:
            self.callback_error(str(e))

            