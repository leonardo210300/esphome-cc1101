import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.components import sensor
from esphome.const import CONF_ID, CONF_PIN

# Define the CC1101 class
cc1101_ns = cg.esphome_ns.namespace("cc1101")
CC1101 = cc1101_ns.class_("CC1101", cg.PollingComponent, sensor.Sensor)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(CC1101),
    cv.Required("pin_sck"): pins.gpio_output_pin_schema,
    cv.Required("pin_miso"): pins.gpio_output_pin_schema,
    cv.Required("pin_mosi"): pins.gpio_output_pin_schema,
    cv.Required("pin_csn"): pins.gpio_output_pin_schema,
    cv.Required("pin_gdo0"): pins.gpio_output_pin_schema,
    cv.Required("bandwidth"): cv.positive_float,
    cv.Required("frequency"): cv.positive_float,
}).extend(sensor.SENSOR_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_pin_sck(config["pin_sck"]))
    cg.add(var.set_pin_miso(config["pin_miso"]))
    cg.add(var.set_pin_mosi(config["pin_mosi"]))
    cg.add(var.set_pin_csn(config["pin_csn"]))
    cg.add(var.set_pin_gdo0(config["pin_gdo0"]))
    cg.add(var.set_bandwidth(config["bandwidth"]))
    cg.add(var.set_frequency(config["frequency"]))
    yield cg.register_component(var, config)
    yield sensor.register_sensor(var, config)
