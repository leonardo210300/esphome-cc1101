#ifndef CC1101TRANSCIVER_H
#define CC1101TRANSCIVER_H

#include <ELECHOUSE_CC1101_SRC_DRV.h>
#include "esphome/components/remote_transmitter/remote_transmitter.h"

class CC1101 : public PollingComponent, public Sensor {
public:
    float _freq;
    CC1101(int SCK, int MISO, int MOSI, int CSN, int GDO0, float bandwidth, float freq, esphome::remote_transmitter::RemoteTransmitterComponent* remote_transmitter);
    void setup() override;
    void update() override;
    void beginTransmission();
    void endTransmission();
    void setBW(float bandwidth);
    void setFreq(float freq);

private:
    int _SCK;
    int _MISO;
    int _MOSI;
    int _CSN;
    int _GDO0;
    float _bandwidth;
    esphome::remote_transmitter::RemoteTransmitterComponent* _remote_transmitter;
    float _moduleNumber;
    int _last_rssi;
    bool rssi_on;
};

#endif

