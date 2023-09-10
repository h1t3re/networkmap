import subprocess

def run_command(command=[], timeout="5"):
    proc = subprocess.Popen(command, bufsize=0, stdout=subprocess.PIPE)
    std_out, std_err = proc.communicate()
    std_out = std_out.strip()
    proc.kill()
    return std_out, std_err

def main():
    for i in range(1, 254):
        try:
            std_out, std_err = run_command(["ping", "-c 1", "192.168.1."+str(i)])
        except:
            print("Error running command.")
        if b'1 received' in std_out:
            print("host found: 192.168.1."+str(i))

if __name__ == "__main__":
    main()
