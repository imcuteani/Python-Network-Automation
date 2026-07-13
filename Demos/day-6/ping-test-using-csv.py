# ping test using Python CSV file (input hosts.csv and output the device_output.csv)

import csv 
import os 
import platform 
import subprocess

plat = platform.system() 

def ping_host(hostname): 
    """
    Pings a host and returns True if reachable, False otherwise
    """
    # Determine the OS and apply the correct fix 
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # building the command (e.g. ping -n l 8.8.8.8)
    command = ['ping', param, '1', hostname]

    try:
        # run command without popping in the console window or printing output 
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except Exception:
        return False


def process_ping_list(input_csv, output_csv):
    """
    Reads hosts from input_csv, pings them and saves the results to output_csv.
    """
    with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        
        # use DictReader assuming the CSV has a column header named ip
        reader = csv.DictReader(infile)

        # define output headers
        fieldnames = ['ip', 'status'] 
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        # looping over the input IPs 
        for row in reader: 
            ip_address = row['ip'].strip()
            if not ip_address:
                continue

            print(f"Pinging {ip_address}......")
            is_up = ping_host(ip_address)

            # Determine the status of the host in text format 
            status = "UP" if is_up else "DOWN"

            # Write the row output to the output file 
            writer.writerow({'ip': ip_address, 'status': status})
            print(f"{ip_address} is {status}")

if __name__ == "__main__":
    # specify the file name here
    input_file = 'hosts.csv'
    output_file = 'ping_results.csv'

    # Run the function
    process_ping_list(input_file, output_file)            
     

