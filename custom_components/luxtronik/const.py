"""Constants for the Luxtronik integration."""

from homeassistant.const import (
    UnitOfTemperature,
    UnitOfTime, 
    UnitOfPressure,
    UnitOfEnergy,
    UnitOfElectricPotential,
    UnitOfPower,
    UnitOfFrequency,
    PERCENTAGE
)
from homeassistant.components.sensor import SensorDeviceClass

ATTR_PARAMETER = "parameter"
ATTR_VALUE = "value"

CONF_STATE_CLASS = "state_class"
CONF_INVERT_STATE = "invert"
CONF_SAFE = "safe"
CONF_GROUP = "group"
CONF_PARAMETERS = "parameters"
CONF_CALCULATIONS = "calculations"
CONF_VISIBILITIES = "visibilities"

CONF_TEMP = "temperature"
CONF_FREQUENCY = "frequency"
CONF_TIMESPAN = "timespan"
CONF_PRESSURE = "pressure"
CONF_TIMESTAMP = "timestamp"
CONF_ENERGY = "energy"
CONF_POWER = "power"
CONF_VOLTAGE = "voltage"
CONF_SPEED = "speed"
CONF_FLOW = "flow"

CONF_CELSIUS = "°C"
CONF_HOURS = "h"
CONF_MIN = "min"
CONF_SECONDS = "s"
CONF_KELVIN = "K"
CONF_BAR = "bar"
CONF_PERCENT = "%"
CONF_KWH = "kWh"
CONF_VOLT = "V"
CONF_LPH = "l/h"
CONF_WATT = "W"
CONF_HZ = "Hz"
CONF_RPM = "rpm"

CONF_LOCK_TIMEOUT = "lock_timeout"
CONF_UPDATE_IMMEDIATELY_AFTER_WRITE = "update_immediately_after_write"


ICONS = {
    "temperature": "mdi:thermometer",
    "timespan": "mdi:timer-sand",
    "ipv4_address": "mdi:ip-network-outline",
    "timestamp": "mdi:calendar-range",
    "errorcode": "mdi:alert-circle-outline",
    "pressure": "mdi:arrow-collapse-all",
    "percent": "mdi:percent",
    "speed": "mdi:rotate-right",
    "power": "mdi:flash",
    "energy": "mdi:lightning-bolt-circle",
    "voltage": "mdi:flash-outline",
    "flow": "mdi:chart-bell-curve",
    "level": "mdi:format-list-numbered",
    "count": "mdi:counter",
    "version": "mdi:information-outline",
    "frequency": "mdi:cosine-wave",
}

DEVICE_CLASSES = {
    CONF_TEMP: SensorDeviceClass.TEMPERATURE,
    CONF_PRESSURE: SensorDeviceClass.PRESSURE,
    CONF_TIMESPAN: SensorDeviceClass.DURATION,
    CONF_TIMESTAMP: SensorDeviceClass.TIMESTAMP,
    CONF_ENERGY: SensorDeviceClass.ENERGY,
    CONF_POWER: SensorDeviceClass.POWER,
    CONF_FREQUENCY: SensorDeviceClass.FREQUENCY,
    CONF_VOLTAGE: SensorDeviceClass.VOLTAGE,
    CONF_SPEED: SensorDeviceClass.SPEED,
    CONF_FLOW: SensorDeviceClass.VOLUME_FLOW_RATE,
}

UNITS = {
    CONF_CELSIUS: UnitOfTemperature.CELSIUS,
    CONF_SECONDS: UnitOfTime.SECONDS,
    CONF_KELVIN: UnitOfTemperature.KELVIN,
    CONF_BAR: UnitOfPressure.BAR,
    CONF_PERCENT: PERCENTAGE,
    CONF_KWH: UnitOfEnergy.KILO_WATT_HOUR,
    CONF_VOLT: UnitOfElectricPotential.VOLT,
    CONF_HOURS: UnitOfTime.HOURS,
    CONF_MIN: UnitOfTime.MINUTES,
    CONF_LPH: "l/h",
    CONF_WATT: UnitOfPower.WATT,
    CONF_HZ: UnitOfFrequency.HERTZ,
    CONF_RPM: "rpm",
}
