import argparse
from colorama import init, Fore
import serial
import csv

init(autoreset=True)
connect_state = False
file_name="Serial2CSV_data.csv"

logo = """
╭━━━╮╱╱╱╱╱╱╱╱╭╮╭━━━┳━━━┳━━━┳╮╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱┃┃┃╭━╮┃╭━╮┃╭━╮┃╰╮╭╯┃
┃╰━━┳━━┳━┳┳━━┫┃╰╯╭╯┃┃╱╰┫╰━━╋╮┃┃╭╯
╰━━╮┃┃━┫╭╋┫╭╮┃┃╭━╯╭┫┃╱╭╋━━╮┃┃╰╯┃
┃╰━╯┃┃━┫┃┃┃╭╮┃╰┫┃╰━┫╰━╯┃╰━╯┃╰╮╭╯
╰━━━┻━━┻╯╰┻╯╰┻━┻━━━┻━━━┻━━━╯╱╰╯
"""

def main():

    global file_name

    print(Fore.YELLOW + logo)
    print(Fore.BLUE + "Created By :" + Fore.GREEN + " Sukarna Jana")
    print(Fore.BLUE + "Version    :" + Fore.GREEN + " 0.0.1V")
    print()

    parser = argparse.ArgumentParser(description="Serial Data Logger")
    parser.add_argument("-p", "--port", type=str, help="Serial port (e.g., COM3)")
    parser.add_argument("-b", "--baud", type=int, help="Baud rate (e.g., 9600)")
    parser.add_argument("-f", "--filename", type=str, help="Output CSV filename")

    args = parser.parse_args()

    if not args.port or not args.baud or not args.filename:
        parser.error(Fore.RED + "Please provide the required arguments: -p, -b, and -f\n" + Fore.CYAN + "example: python3 serial2csv.py -p COM3 -b 9600 -f output.csv" )

    print(Fore.CYAN + "Selected Serial Port: " + Fore.YELLOW + str(args.port))
    print(Fore.CYAN + "Baud Rate           : " + Fore.YELLOW + str(args.baud))
    print(Fore.CYAN + "Output Filename     : " + Fore.YELLOW + str(args.filename))
    print(Fore.YELLOW + "To Terminate/Stop u can press [Ctrl+C]")
    print()
    file_name = args.filename

    connect(str(args.port),int(args.baud))
    while isConnect():
        try:
            #printData()
            saveData()
        except KeyboardInterrupt:
            break


def connect(portNo,baud):
    global connect_state, device
    try:
        device = serial.Serial(port=portNo, baudrate=baud, timeout=0.1)
        connect_state = True
        print(Fore.GREEN + "Connection Establish Successfully")
    except:
        connect_state = False
        print(Fore.RED + "Connection Establish Failed")

def isConnect():
    if(connect_state):
        return True
    else:
        return False

def printData():
    try:
        if(isConnect()):
            ser_bytes = device.readline()
            data = (ser_bytes[0:len(ser_bytes)-2]).decode("utf-8")
            if(data != ""):
                print(Fore.GREEN + data)
                value_list = [int(value) for value in data.split(",")]
                print(value_list)
        else:
            print(Fore.RED + "[ERROR] Something Sent Wrong")
            exit()
    except:
        device.close()
        print(Fore.RED + "[ERROR] Something Sent Wrong")
        exit()

def saveData():
    try:
        if isConnect():
            ser_bytes = device.readline()
            data = (ser_bytes[0:len(ser_bytes) - 2]).decode("utf-8")
            if data != "":
                value_list = [int(value) for value in data.split(",")]

                # Open the CSV file in append mode and write the data
                with open(file_name, mode='a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(value_list)
                    print(Fore.CYAN + "Data saved to CSV:", value_list)

    except Exception as e:
        device.close()
        print(Fore.RED + "[ERROR] Something Went Wrong While Saving Data:", str(e))


if __name__ == "__main__":
    main()
