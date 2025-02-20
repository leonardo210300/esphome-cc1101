import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID, CONF_NAME

# Define the CC1101 class
cc1101_ns = cg.esphome_ns.namespace('cc1101')
CC1101 = cc1101_ns.class_('CC1101', cg.PollingComponent, sensor.Sensor)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(CC1101),
    cv.Required(CONF_NAME): cv.string,
    cv.Required("pin_sck"): cv.int_,
    cv.Required("pin_miso"): cv.int_,
    cv.Required("pin_mosi"): cv.int_,
    cv.Required("pin_csn"): cv.int_,
    cv.Required("pin_gdo0"): cv.int_,
    cv.Required("bandwidth"): cv.float_,
    cv.Required("frequency"): cv.float_,
}).extend(sensor.SENSOR_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_name(config[CONF_NAME]))
    cg.add(var.set_pin_sck(config["pin_sck"]))
    cg.add(var.set_pin_miso(config["pin_miso"]))
    cg.add(var.set_pin_mosi(config["pin_mosi"]))
    cg.add(var.set_pin_csn(config["pin_csn"]))
    cg.add(var.set_pin_gdo0(config["pin_gdo0"]))
    cg.add(var.set_bandwidth(config["bandwidth"]))
    cg.add(var.set_frequency(config["frequency"]))
    yield cg.register_component(var, config)
    yield sensor.register_sensor(var, config)

    yield sensor.register_sensor(var, config)
