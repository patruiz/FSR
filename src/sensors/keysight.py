import keysight_kt34400 
import keysight_kt34400.keysight_kt34400
import pandas as pd 
import numpy as np 
import keyboard
import datetime
import time
import os 

class EDU34450A:
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.idQuery = True
        self.reset = True
        self.options = "QueryInstrStatus=True, Simulate=False, Trace=True"
        self.driver = None
        self.sample_delay = None 
        self.data = []
        
    def configure_driver(self):
        print("\nKeysight EDU34450A Python Driver Initilizing ...")
        time.sleep(3)
        try:
            self.driver = keysight_kt34400.Kt34400(self.resource_name, self.idQuery, self.reset, self.options)
            print("\nDriver Initialized\n")

            # print('  identifier: ', self.driver.identity.identifier)
            # print('  revision:   ', self.driver.identity.revision)
            print('  vendor:     ', self.driver.identity.vendor)
            print('  description:', self.driver.identity.description)
            print('  model:      ', self.driver.identity.instrument_model)
            print('  resource:   ', self.driver.driver_operation.io_resource_descriptor)
            print('  options:    ', self.driver.driver_operation.driver_setup)
            print(' ')

            self.driver.utility.reset()

            self.driver.trigger.source = keysight_kt34400.TriggerSource.IMMEDIATE

            # self.driver.resistance.configure(10E+3,keysight_kt34400.keysight_kt34400.Resolution.MIN)
            self.driver.resistance.configure(1E+8, keysight_kt34400.keysight_kt34400.Resolution.MED)

            self.sample_delay = datetime.timedelta(milliseconds=2e+6)

        except Exception as e:
            print("\n Exception:", e.__class__.__name__, e.args)


    def read_values(self):
        flag = True
        while flag:
            val = self.driver.measurement.read(self.sample_delay)
            print(val)
            self.data.append(val)
            if keyboard.is_pressed('esc'):
                flag = False
        self.store_data(self.data, '1', False)

    def read_singlevalue(self):
        val = self.driver.measurement.read(self.sample_delay)
        print(val)
        return val 

    def store_data(self, data, fsr_num, save_data = True):
        if save_data == True:
            save_dir = os.path.join('data', 'raw', 'keysight')
            datetime_stamp = datetime.datetime.now().strftime('%d%b%y_%H-%M-%S')
            file_name = f"FSR{fsr_num}_calibration_{datetime_stamp}.csv"
            file_path = os.path.join(os.getcwd(), save_dir, file_name)

            print(f"Data Saved in: {file_path}")
            print(f"Data Array Length: {len(data)}")

            data_array = np.array(self.data)

            df = pd.DataFrame(data_array)
            df.to_csv(file_path, index = False)
