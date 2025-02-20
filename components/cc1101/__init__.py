import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID, CONF_NAME

# Define the CC1101 class
cc1101_ns = cg.esphome_ns.namespace('cc1101')
CC1101 = cc1101_ns.class_('CC1101', cg.PollingComponent, sensor.Sensor)

CONF_PIN_SCK = "pin_sck"
CONF_PIN_MISO = "pin_miso"
CONF_PIN_MOSI = "pin_mosi"
CONF_PIN_CSN = "pin_csn"
CONF_PIN_GDO0 = "pin_gdo0"
CONF_BANDWIDTH = "bandwidth"
CONF_FREQUENCY = "frequency"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(CC1101),
    cv.Required(CONF_NAME): cv.string,
    cv.Required(CONF_PIN_SCK): cv.int_,
    cv.Required(CONF_PIN_MISO): cv.int_,
    cv.Required(CONF_PIN_MOSI): cv.int_,
    cv.Required(CONF_PIN_CSN): cv.int_,
    cv.Required(CONF_PIN_GDO0): cv.int_,
    cv.Required(CONF_BANDWIDTH): cv.float_,
    cv.Required(CONF_FREQUENCY): cv.float_,
}).extend(sensor.SENSOR_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_name(config[CONF_NAME]))
    cg.add(var.set_pin_sck(config[CONF_PIN_SCK]))
    cg.add(var.set_pin_miso(config[CONF_PIN_MISO]))
    cg.add(var.set_pin_mosi(config[CONF_PIN_MOSI]))
    cg.add(var.set_pin_csn(config[CONF_PIN_CSN]))
    cg.add(var.set_pin_gdo0(config[CONF_PIN_GDO0]))
    cg.add(var.set_bandwidth(config[CONF_BANDWIDTH]))
    cg.add(var.set_frequency(config[CONF_FREQUENCY]))
    yield cg.register_component(var, config)
    yield sensor.register_sensor(var, config)


