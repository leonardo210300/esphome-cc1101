#include "cc1101_component.h"

int CC1101_module_count = 0;

CC1101::CC1101(int SCK, int MISO, int MOSI, int CSN, int GDO0, float bandwidth, float freq, esphome::remote_transmitter::RemoteTransmitterComponent* remote_transmitter)
: PollingComponent(100), _SCK(SCK), _MISO(MISO), _MOSI(MOSI), _CSN(CSN), _GDO0(GDO0), _bandwidth(bandwidth), _freq(freq), _remote_transmitter(remote_transmitter) {
    _moduleNumber = CC1101_module_count++;
    _last_rssi = 0;
    rssi_on = false;
}

void CC1101::setup() {
    pinMode(_GDO0, INPUT);
    ELECHOUSE_cc1101.addSpiPin(_SCK, _MISO, _MOSI, _CSN, _moduleNumber);
    ELECHOUSE_cc1101.setModul(_moduleNumber);
    ELECHOUSE_cc1101.Init();
    ELECHOUSE_cc1101.setRxBW(_bandwidth);
    ELECHOUSE_cc1101.setMHZ(_freq);
    ELECHOUSE_cc1101.SetRx();
}

void CC1101::beginTransmission() {
    ELECHOUSE_cc1101.setModul(_moduleNumber);
    ELECHOUSE_cc1101.SetTx();
    pinMode(_GDO0, OUTPUT);
    #ifdef USE_ESP32
    _remote_transmitter->setup();
    #endif
    #ifdef USE_ESP8266
    noInterrupts();
    #endif
}

void CC1101::endTransmission() {
    digitalWrite(_GDO0, 0);
    pinMode(_GDO0, INPUT);
    #ifdef USE_ESP8266
    interrupts();
    #endif
    ELECHOUSE_cc1101.setModul(_moduleNumber);
    ELECHOUSE_cc1101.SetRx();
    ELECHOUSE_cc1101.SetRx();  // yes, twice
}

void CC1101::setBW(float bandwidth) {
    ELECHOUSE_cc1101.setModul(_moduleNumber);
    ELECHOUSE_cc1101.setRxBW(bandwidth);
}

void CC1101::setFreq(float freq) {
    ELECHOUSE_cc1101.setModul(_moduleNumber);
    ELECHOUSE_cc1101.setMHZ(freq);
}

void CC1101::update() {
    int rssi = 0;
    if (rssi_on) {
        ELECHOUSE_cc1101.setModul(_moduleNumber);
        rssi = ELECHOUSE_cc1101.getRssi();
        if (rssi != _last_rssi) {
            publish_state(rssi);
            _last_rssi = rssi;
        }
    }
}
