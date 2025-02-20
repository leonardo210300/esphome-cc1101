# __init__.py file for the cc1101 component

import esphome
from esphome import automation, component, sensor, remote_transmitter

# Define the CC1101 class
class CC1101(component.PollingComponent, sensor.Sensor):
    def __init__(self, SCK, MISO, MOSI, CSN, GDO0, bandwidth, freq, remote_transmitter):
        super().__init__()
        self._SCK = SCK
        self._MISO = MISO
        self._MOSI = MOSI
        self._CSN = CSN
        self._GDO0 = GDO0
        self._bandwidth = bandwidth
        self._freq = freq
        self._remote_transmitter = remote_transmitter
        self._moduleNumber = 0
        self._last_rssi = 0
        self.rssi_on = False

    def setup(self):
        pinMode(self._GDO0, INPUT)
        ELECHOUSE_cc1101.addSpiPin(self._SCK, self._MISO, self._MOSI, self._CSN, self._moduleNumber)
        ELECHOUSE_cc1101.setModul(self._moduleNumber)
        ELECHOUSE_cc1101.Init()
        ELECHOUSE_cc1101.setRxBW(self._bandwidth)
        ELECHOUSE_cc1101.setMHZ(self._freq)
        ELECHOUSE_cc1101.SetRx()

    def update(self):
        rssi = 0
        if self.rssi_on:
            ELECHOUSE_cc1101.setModul(self._moduleNumber)
            rssi = ELECHOUSE_cc1101.getRssi()
            if rssi != self._last_rssi:
                self.publish_state(rssi)
                self._last_rssi = rssi

    def beginTransmission(self):
        ELECHOUSE_cc1101.setModul(self._moduleNumber)
        ELECHOUSE_cc1101.SetTx()
        pinMode(self._GDO0, OUTPUT)
        self._remote_transmitter.setup()

    def endTransmission(self):
        digitalWrite(self._GDO0, 0)
        pinMode(self._GDO0, INPUT)
        ELECHOUSE_cc1101.setModul(self._moduleNumber)
        ELECHOUSE_cc1101.SetRx()
        ELECHOUSE_cc1101.SetRx()  # yes, twice

    def setBW(self, bandwidth):
        ELECHOUSE_cc1101.setModul(self._moduleNumber)
        ELECHOUSE_cc1101.setRxBW(bandwidth)

    def setFreq(self, freq):
        ELECHOUSE_cc1101.setModul(self._moduleNumber)
        ELECHOUSE_cc1101.setMHZ(freq)
