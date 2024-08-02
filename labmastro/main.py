from labmastro.power_supply.hanmatek.hm.instrument import HanmatekHmInstrument
from labmastro.power_supply.hanmatek.hm.control import HanmatekHmControl


if __name__ == "__main__":
    instrument = HanmatekHmInstrument(port="/dev/tty.usbserial-214210")

    dc_control = HanmatekHmControl(instrument)

    dc_control.set_voltage(3.3)
    dc_control.set_current(0.05)
    dc_control.power_on()

    print("power", dc_control.get_power())
    print("voltage", dc_control.get_voltage())
    print("current", dc_control.get_current())
