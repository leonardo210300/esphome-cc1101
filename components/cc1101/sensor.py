import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID, CONF_NAME, UNIT_DECIBEL, ICON_SIGNAL, DEVICE_CLASS_SIGNAL_STRENGTH

# Define the CC1101 component namespace
cc1101_ns = cg.esphome_ns.namespace('cc1101')
CC1101 = cc1101_ns.class_('CC1101', cg.PollingComponent, sensor.Sensor)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(CC1101),
    cv.Optional(CONF_NAME): cv.string,
}).extend(sensor.SENSOR_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    if CONF_NAME in config:
        cg.add(var.set_name(config[CONF_NAME]))
    yield cg.register_component(var, config)
    yield sensor.register_sensor(var, config)
