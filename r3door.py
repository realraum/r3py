import json
import requests


class r3door():

    def __init__(self):
        self.loadStatus()

    def loadStatus(self):
        resp = requests.get(url="http://realraum.at/status.json")
        self.data = resp.json()

    def getStatusByName(self, name):
        try:
            return filter(lambda x: x['name'] == name,
                          self.data['sensors']['door_locked'])[0]['value']
        except KeyError:
            return true

    def getDoorstatus(self):
        locked = self.getStatusByName('TorwaechterLock')
        kontakted = self.getStatusByName('TorwaechterAjarSensor')
        return (locked, kontakted)


def printInfo():
    api = r3door()
    status = api.getDoorstatus()
    print 'locked:   ', status[0]
    print 'kontakted:', status[1]

if __name__ == '__main__':
    printInfo()
