#include "cc1101_component.h"

CC1101::CC1101(int SCK, int MISO, int MOSI, int CSN, int GDO0, float bandwidth, float freq, esphome::remote_transmitter::RemoteTransmitterComponent* remote_transmitter)
    : PollingComponent(100), _SCK(SCK), _MISO(MISO), _MOSI(MOSI), _CSN(CSN), _GDO0(GDO0), _bandwidth(bandwidth), _freq(freq), _remote_transmitter(remote_transmitter) {}

void CC1101::setup() {
    // Initialization code
}

void CC1101::update() {
    // Update code
}

void CC1101::set_pin_sck(int SCK) {
    _SCK = SCK;
}

void CC1101::set_pin_miso(int MISO) {
    _MISO = MISO;
}

void CC1101::set_pin_mosi(int MOSI) {
    _MOSI = MOSI;
}

void CC1101::set_pin_csn(int CSN) {
    _CSN = CSN;
}

void CC1101::set_pin_gdo0(int GDO0) {
    _GDO0 = GDO0;
}

void CC1101::set_bandwidth(float bandwidth) {
    _bandwidth = bandwidth;
}

void CC1101::set_frequency(float freq) {
    _freq = freq;
}
