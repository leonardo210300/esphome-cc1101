#ifndef CC1101TRANSCIVER_H
#define CC1101TRANSCIVER_H

#include <ELECHOUSE_CC1101_SRC_DRV.h>
#include "esphome/components/remote_transmitter/remote_transmitter.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/core/component.h"

class CC1101 : public esphome::PollingComponent, public esphome::sensor::Sensor {
public:
    CC1101(int SCK, int MISO, int MOSI, int CSN, int GDO0, float bandwidth, float freq, esphome::remote_transmitter::RemoteTransmitterComponent* remote_transmitter);
    void setup() override;
    void update() override;
    void set_pin_sck(int SCK);
    void set_pin_miso(int MISO);
    void set_pin_mosi(int MOSI);
    void set_pin_csn(int CSN);
    void set_pin_gdo0(int GDO0);
    void set_bandwidth(float bandwidth);
    void set_frequency(float freq);

private:
    int _SCK;
    int _MISO;
    int _MOSI;
    int _CSN;
    int _GDO0;
    float _bandwidth;
    float _freq;
    esphome::remote_transmitter::RemoteTransmitterComponent* _remote_transmitter;
};

#endif


