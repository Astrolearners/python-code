import pandas as pd
import datetime

from modules.helpers.logger import logger
from modules.schemas.schemas import dataframe_schema, main_schema


class csvHandler():
    def __init__(self, csv_path):
        self.log = logger("csvHandler")
        self.dataframe_schema = dataframe_schema
        self.main_schema = main_schema
        self.csv_path = csv_path

        self.log.info("Initializing data frame...")
        self.dataFrame = pd.DataFrame(self.dataframe_schema, index=[0])

    def listData(self):
        return self.dataFrame

    def addData(self, data: dict):
        newData = self.dataframe_schema
        for i in data.keys():
            if i == "time":
                newData["time"] = data[i]
            elif i == "bme":
                for b in self.main_schema["bme"].keys():
                    newData[b] = data["bme"][b]
            elif i == "gps":
                for g in main_schema["gps"].keys():
                    newData[g] = data["gps"][g]
            elif i == "accelerometer":
                for a in main_schema["accelerometer"].keys():
                    if a == "accelerometer":
                        for a_a in self.main_schema["accelerometer"]["accelerometer"].keys():
                            newData[f"accelerometer-{a_a}"] = data["accelerometer"]["accelerometer"][a_a]
                    if a == "magnetometer":
                        for a_m in self.main_schema["accelerometer"]["magnetometer"].keys():
                            newData[f"magnetometer-{a_m}"] = data["accelerometer"]["magnetometer"][a_m]
            elif i == "rpi_temp":
                newData["rpi_temp"] = data[i]
        self.dataFrame.loc[len(self.dataFrame.index)] = newData

    def saveDataframe(self):
        self.log.info("Saving data to csv...")
        date_time = datetime.datetime.now()
        file_name = date_time.strftime("%d_%m_%y-data.csv")
        self.dataFrame.to_csv(f"{self.csv_path}/{file_name}")