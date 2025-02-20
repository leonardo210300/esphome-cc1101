# __init__.py file for the cc1101 component

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

# Declare the CC1101 class
CC1101 = cg.global_ns.class_("CC1101", cg.PollingComponent, sensor.Sensor)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(CC1101),
}).extend(sensor.SENSOR_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield sensor.register_sensor(var, config)
