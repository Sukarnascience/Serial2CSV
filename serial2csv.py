import argparse

def main():
    parser = argparse.ArgumentParser(description="Arduino Data Logger")
    parser.add_argument("-p", "--port", type=str, help="Serial port (e.g., COM3)")
    parser.add_argument("-b", "--baud", type=int, help="Baud rate (e.g., 9600)")
    parser.add_argument("-f", "--filename", type=str, help="Output CSV filename")

    args = parser.parse_args()

    if not args.port or not args.baud or not args.filename:
        parser.error("Please provide the required arguments: -p, -b, and -f")

    print(f"Serial Port: {args.port}")
    print(f"Baud Rate: {args.baud}")
    print(f"Output Filename: {args.filename}")

if __name__ == "__main__":
    main()
