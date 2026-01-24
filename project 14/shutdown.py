import subprocess
import platform

def shutdown_computer(seconds=0):
    """
    Shuts down the computer based on the OS.
    :param seconds: Time to wait before shutting down (default 0).
    """
    system_os = platform.system().lower()
    
    try:
        if system_os == "windows":
            # /s = shutdown, /t = time in seconds
            subprocess.run(["shutdown", "/s", "/t", str(seconds)], check=True)
            print(f"Windows will shut down in {seconds} seconds.")
            
        elif system_os == "linux" or system_os == "darwin":  # darwin is macOS
            # -h = halt/shutdown, +m = minutes (0 is 'now')
            # Note: On many Linux systems, this requires sudo/root privileges
            time_arg = "now" if seconds == 0 else f"+{seconds // 60}"
            subprocess.run(["sudo", "shutdown", "-h", time_arg], check=True)
            print(f"Unix-based system shutdown initiated.")
            
    except subprocess.CalledProcessError as e:
        print(f"Error: Could not execute shutdown. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Change the number to set a delay in seconds
    shutdown_computer(seconds=0)