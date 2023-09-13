# Serial2CSV

**Author:** Sukarna Jana  
**Version:** 0.0.1V  
**Last Update:** 13-09-2023  

## Introduction

Serial2CSV is a Python-based tool designed to simplify the process of logging data from Arduino or other devices connected via a serial port and saving it into a CSV (Comma-Separated Values) file. This tool automates the data logging process and helps you organize and analyze your data more efficiently.

## Prerequisites

Before using Serial2CSV, ensure you have the following prerequisites installed:

1. **Python**: Serial2CSV is a Python script, so you need to have Python installed on your computer. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

## Usage

### Windows Users

Windows users can set up Serial2CSV by following these steps:

1. **Clone the Repository**: Start by cloning this repository to your local machine:

    ```bash
    git clone https://github.com/Sukarnascience/Serial2CSV.git
    ```

2. **Navigate to the Project Directory**: Change your current directory to the project directory:

    ```bash
    cd Serial2CSV
    ```

3. **Run the Setup Script**: Execute the setup script to check for Python, install required packages, and set up the environment for data logging:

    ```bash
    setup.bat
    ```

    The script will guide you through the process, ensuring that Python is installed and any potential errors are handled gracefully.

### Linux and macOS Users

For users of Linux and macOS, follow these steps to set up Serial2CSV:

1. **Clone the Repository**: Start by cloning this repository to your local machine:

    ```bash
    git clone https://github.com/Sukarnascience/Serial2CSV.git
    ```

2. **Navigate to the Project Directory**: Change your current directory to the project directory:

    ```bash
    cd Serial2CSV
    ```

3. **Install Required Packages**: Manually install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

### Logging Data

Once you've set up Serial2CSV, you can log data from your Arduino by running the following command:

```bash
python serial2csv.py -p COMX -b 9600 -f output.csv
```

* `-p` or `--port`: Specify the serial port to which your Arduino is connected (e.g., COM3).
* `-b` or `--baud`: Set the baud rate (e.g., 9600) to match your Arduino's communication settings.
* `-f` or `--filename`: Choose the name for the output CSV file.

example: 
* Windows
    ```bash
    python serial2csv.py -p COM3 -b 9600 -f output.csv
    ```
* Linux and macOS 
    ```bash
    python3 serial2csv.py -p /dev/ttyACM0 -b 9600 -f output.csv
    ```

    
* **Data Logging**: Serial2CSV will continuously log data from the serial port and save it into the specified CSV file.

* **Stop Logging**: To stop data logging, press `Ctrl+C` in the terminal where Serial2CSV is running.

* **Data Analysis**: Once data logging is complete, you can use tools like Microsoft Excel or Python's data analysis libraries to analyze and visualize your data from the CSV file.

## Example Arduino Code

Here's an example Arduino code snippet to send data to Serial2CSV:


```arduino
void setup() {
    Serial.begin(9600);  // Set the baud rate to match Serial2CSV
}

void loop() {
    // Your code to collect data
    int sensorValue = analogRead(A0);
    
    // Send data over serial
    Serial.print(sensorValue);
    Serial.print(",");
    
    // Add more data if needed, separated by ","
    
    Serial.println();
    // Delay if necessary to control data rate
    delay(1000);
}
```

> Dummy Code to Upload on Arduino to test
```c
void setup() {
  Serial.begin(9600);  // Set the baud rate to match your receiving device
  randomSeed(analogRead(0));  // Initialize the random number generator with a seed
}

void loop() {
  static int SNo = 0;  // Initialize the serial number counter

  // Print SNo as the first value in the CSV format
  Serial.print(SNo);

  // Generate and print 8 random integers
  for (int i = 0; i < 8; i++) {
    int randomValue = random(0, 101);  // Generate a random integer between 0 and 100 (adjust as needed)
    
    // Print a comma and the random integer value
    Serial.print(",");
    Serial.print(randomValue);
  }

  Serial.println();  // Print a newline character to indicate the end of the CSV line

  SNo++;  // Increment the serial number counter
  delay(1000);  // Delay for a second (adjust as needed for your desired data rate)
}

```

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
