import os
import time
import serial 
import keyboard
import threading
import pandas as pd
from datetime import datetime
import serial.tools.list_ports

class IPM650:
    def __init__(self, port, baudrate = 9600, timeout = .5):
        self.port = port 
        self.baudrate = baudrate
        self.timeout = timeout
        self.conn = None
        self.data = pd.DataFrame()

    def open_connection(self):
        print("\nFUTEK IPM650 Connection Initilizing ...")
        time.sleep(3)
        try:
            self.conn = serial.Serial(self.port, self.baudrate, timeout = self.timeout)
            print("\nSerial Connection Established\n")

            print('  vendor: FUTEK')
            print('  description: IPM650 Python API')
            print('  model: LSB201 - IPM650')
            print('  port: ', self.port)
            print('  baudrate: ', self.baudrate)
            print('  timeout: ', self.timeout)
            print(' ')

        except serial.SerialException as e:
            print(f"Error: {e}")

    def close_connection(self):
        if self.conn and self.conn.isOpen():
            self.conn.close()
            self.conn = None
            # print("Serial Connection Disconnected")
        else:
            print("No Active Serial Connection.")

    def start_test(self, sample_size, print_vals = False):
        values = []

        if self.conn and self.conn.isOpen():
            while len(values) < sample_size:
                try:
                    serial_output = self.conn.readline().decode('utf-8', errors = 'replace').strip()
                    lines = serial_output.split('\n')

                    for line in lines:
                        if "lbs" in line:
                            parts = line.split()
                            for i, part in enumerate(parts):
                                if part == "lbs":
                                    try:
                                        value = abs(float(parts[i - 1]))
                                        values.append(value)
                                    except ValueError:
                                        print("Value Error")
                                        pass

                except serial.SerialException as e:
                    print(f"Error Reading Data: {e}")
        
        else:
            print("No Active Serial Connection.")
        
        if print_vals == True:
            print(values)

        if len(self.data.columns) == 0:
            self.data[0] = values
        else:
            new_column_name = len(self.data.columns)
            self.data[new_column_name] = values

    def read_values(self):
        flag = True
        if self.conn and self.conn.isOpen():
            while flag:
                serial_output = self.conn.readline().decode('utf-8', errors = 'replace').strip()
                lines = serial_output.split('\n')

                for line in lines:
                    if "lbs" in line:
                        parts = line.split()
                        for i, part in enumerate(parts):
                            if part == "lbs":
                                value = abs(float(parts[i - 1]))
                                print(value)
                if keyboard.is_pressed('esc'):
                    flag = False

    def read_singlevalue(self):
        if self.conn and self.conn.isOpen():
            serial_output = self.conn.readline().decode('utf-8', errors = 'replace').strip()
            lines = serial_output.split('\n')

            for line in lines:
                if "lbs" in line:
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if part == "lbs":
                            value = abs(float(parts[i - 1]))
                            print(value)
                            return(value)


    def store_data(self, save_data = True):
        if save_data == True:
            save_dir = os.path.join('data', 'raw', 'futek')
            datetime_stamp = datetime.now().strftime('%d%b%y_%H-%M-%S')
            file_name = f"futek_dawdata_{datetime_stamp}.csv"
            file_path = os.path.join(save_dir, file_name)
            self.data.to_csv(file_path, index = False)