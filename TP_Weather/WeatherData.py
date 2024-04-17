class TempDisplay:
    def update(self, temperature):
        print(f"Temperature: {temperature}")

class HumidityDisplay:
    def update(self, humidity):
        print(f"Humidity: {humidity}")

class PressureDisplay:
    def update(self, pressure):
        print(f"Pressure: {pressure}")


class WeatherData:

    def __init__(self):
        self.__dipsplay = [] 
        # self.__temperatureDisplay = TempDisplay()
        # self.__humidityDisplay = HumidityDisplay()
        # self.__pressureDisplay = PressureDisplay()


def getTemperature(self):
    return 25

def getHumidity(self):
    return 65

def getPressure(self):
    return 1020

def measurementsChanged(self):
    temperature = self.getTemperature()
    humidity = self.getHumidity()
    pressure = self.getPressure()

    self.__temperatureDisplay.update(temperature)
    self.__humidityDisplay.update(humidity)
    self.__pressureDisplay.update(pressure)