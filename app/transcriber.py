from faster_whisper import WhisperModel
import os

_model = None


def get_model():
    global _model

    if _model is None:
        _model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

    return _model


def transcrever(video):

    model = get_model()

    segments, info = model.transcribe(
        video,
        language="pt"
    )

    saida = os.path.splitext(video)[0] + ".txt"

    with open(saida, "w", encoding="utf-8") as f:
        for segment in segments:
            f.write(segment.text.strip() + "\n")

    return saida
