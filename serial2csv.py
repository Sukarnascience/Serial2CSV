import argparse
from colorama import init, Fore

init(autoreset=True)

logo = """
╭━━━╮╱╱╱╱╱╱╱╱╭╮╭━━━┳━━━┳━━━┳╮╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱┃┃┃╭━╮┃╭━╮┃╭━╮┃╰╮╭╯┃
┃╰━━┳━━┳━┳┳━━┫┃╰╯╭╯┃┃╱╰┫╰━━╋╮┃┃╭╯
╰━━╮┃┃━┫╭╋┫╭╮┃┃╭━╯╭┫┃╱╭╋━━╮┃┃╰╯┃
┃╰━╯┃┃━┫┃┃┃╭╮┃╰┫┃╰━┫╰━╯┃╰━╯┃╰╮╭╯
╰━━━┻━━┻╯╰┻╯╰┻━┻━━━┻━━━┻━━━╯╱╰╯
"""

def main():

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

def collectData(port,baud,fileName):
    pass

if __name__ == "__main__":
    main()
