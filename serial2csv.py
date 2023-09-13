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
    print()
    file_name = file_name

    connect(str(args.port),int(args.baud))
    while isConnect():
        printData()
        saveData()

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
        else:
            print(Fore.RED + "[ERROR] Something Sent Wrong")
            exit()
    except:
        print(Fore.RED + "[ERROR] Something Sent Wrong")
        exit()

def saveData():
    pass

if __name__ == "__main__":
    main()
