# krasip
an ubuntu 24 desktop daemon that provide ai dictation (including openai whisper)

## MVP
- [x] x11 keyboard input

## Getting Started

### dependencies
```
sudo apt-get update
sudo apt-get install python3-dev portaudio19-dev # PyAudio

sudo apt-get install xdotool # X11 keyboard input

sudo apt update && sudo apt install ffmpeg # whisper
```

# Information
- [status-of-whisper](https://alphacephei.com/nsh/2024/04/20/status-of-whisper.html) - whisper is not designed for realtime transcription, despite in could be used for it.

# Similar projects
- [nerd-dictation](https://github.com/ideasman42/nerd-dictation) - limited to offline vosk, bad UX - no init feedback, no status bar, no hotkeys, no hotkeys, no hotkeys

