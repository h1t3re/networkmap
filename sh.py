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
            packet = scapy.sr(scapy.ICMP(type=8)/scapy.IP(dst="192.168.1."+str(i)), verbose=True)
        except:
            print(".")

if __name__ == "__main__":
    main()
