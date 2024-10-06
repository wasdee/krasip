import whisper
import time
from typing import Any

model_load_start: float = time.time()
model: Any = whisper.load_model("turbo")
model_load_end: float = time.time()

model_load_time: float = model_load_end - model_load_start
print(f"Model load time: {model_load_time:.2f} seconds")

transcription_start: float = time.time()
result: dict[str, Any] = model.transcribe("recorded_audio.mp3")
transcription_end: float = time.time()

transcription_time: float = transcription_end - transcription_start
print(f"Transcription time: {transcription_time:.2f} seconds")
print(f"Transcribed text: {result['text']}")

# $ /home/ben/Devs/Playground/krasip/.venv/bin/python /home/ben/Devs/Playground/krasip/Jigsaws/transcript.py
# /home/ben/Devs/Playground/krasip/.venv/lib/python3.12/site-packages/whisper/__init__.py:150: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
#   checkpoint = torch.load(fp, map_location=device)
# Model load time: 7.27 seconds
# Transcription time: 0.76 seconds
# Transcribed text: สวัสดีครับ ชื่อเป็นครับ ยินดีที่ใต้พิจัดนะคะ Hello my name is Ben