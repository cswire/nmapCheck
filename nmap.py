import subprocess
import shlex

def run_nmap_scan():
    try:
        # Prompt for user input
        url = input("Enter a URL or IP address for scanning: ").strip()

        # Construct the nmap command
        command = f"nmap -sV -A {shlex.quote(url)}"

        # Run the command and capture output
        result = subprocess.run(command, shell=True, text=True, capture_output=True)

        # Display the result
        if result.stdout:
            print("Scan Results:")
            print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_nmap_scan()
