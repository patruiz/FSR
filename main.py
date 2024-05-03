import os
import mouse
import keyboard
import datetime
from src.sensors.futek import IPM650
from src.sensors.keysight import EDU34450A

def main(FSR_dir):
    os.system('cls')

    futek_port = 'COM3'
    LoadCell = IPM650(port=futek_port, baudrate=115200, timeout=1)
    LoadCell.open_connection()

    resource_name = 'USB0::0x2A8D::0x8E01::CN62180061::0::INSTR'
    DMM = EDU34450A(resource_name)
    DMM.configure_driver()

    datetime_stamp = datetime.datetime.now().strftime('%d%b%y_%H-%M-%S')
    file_name = f"calibration_data_{datetime_stamp}.csv"
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'raw', file_name)

    with open(file_path, 'w') as csvfile:
        csvfile.write("Sensor, Timestamp, Value\n")

        flag = True
        while flag:
            timestamp = datetime.datetime.now()

            loadcell_value = LoadCell.read_singlevalue()
            dmm_value = DMM.read_singlevalue()

            csvfile.write(f"LoadCell, {timestamp}, {loadcell_value}\n")
            csvfile.write(f"DMM, {timestamp}, {dmm_value}\n")

            mouse.click(button='left')

            if keyboard.is_pressed('p'):
                flag = False

        csvfile.close()

    LoadCell.close_connection() 
    # DMM.close_connection()

if __name__ == "__main__":
    FSR_dir = 'FSR_S2'
    main(FSR_dir)