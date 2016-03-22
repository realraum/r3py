import requests
import json


class r3temp():

    def __init__(self):
        self.loadStatusData()

    def loadTemp(self):
        # to be run on the device connected to the sensor!
        tfile = open("/sys/bus/w1/devices/10-000801375be4/w1_slave")
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return temperature

    def getTempFromSensor(self):
        # to be run on the device connected to the sensor!
        while True:
            temp = self.loadTemp()
            if temp < 85:
                break
        return temp

    def loadStatusData(self):
        resp = requests.get(url="https://realraum.at/status.json")
        self.data = resp.json()

    def getTempByName(self, name):
        try:
            return filter(lambda x: x['name'] == name, self.data[
                          'sensors']['temperature'])[0]['value']
        except KeyError:
            return 42

    def getTemp(self):
        return self.getTempByName('Temp@LoTHR')


def printInfo():
    api = r3temp()
    print 'Temp Outside:           ', api.getTempByName('Temp@Outside')
    print 'Temp in LoTHR:         ', api.getTempByName('Temp@LoTHR')
    print 'Temp in CX:            ', api.getTempByName('Temp@CX')
    print 'Temp in OLGA Room:     ', api.getTempByName('Temp@OLGA Room')
    print 'Temp in OLGA freezer: ', api.getTempByName('Temp@OLGA freezer')
    print 'Temp in UPS Battery:   ', api.getTempByName('Temp@UPS Yellow Battery')


if __name__ == '__main__':
    printInfo()
