import subprocess
import sys

def put_text_down(text, input_emu):
    if input_emu == "XDOTOOL":
        try:
            subprocess.run(["xdotool", "type", "--clearmodifiers", "--", text], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing xdotool: {e}")
        except FileNotFoundError:
            print("xdotool not found. Please install xdotool using:")
            print("sudo apt install xdotool")
            sys.exit(1)
    else:
        print(f"Unsupported input emulation method: {input_emu}")

if __name__ == "__main__":
    put_text_down("Hello, world!", "XDOTOOL")
