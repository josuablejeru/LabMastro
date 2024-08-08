"""Hanmatek power supply controller."""

from minimalmodbus import Instrument


class HanmatekHmControl:
    """Manage a Hanmatek power supply."""

    def __init__(self, instrument: Instrument) -> None:
        self.instrument = instrument

    def get_voltage(self) -> float:
        """Read the current voltage display value."""
        voltage = self.instrument.read_register(0x0010, 2, functioncode=3)
        return round(voltage, 2)

    def get_current(self):
        """Read the current amperage display value."""
        current = self.instrument.read_register(0x0011, 3, functioncode=3)
        return round(current, 2)

    def get_power(self):
        """Read the current power display value."""
        # Read 32-bit power value split into two registers
        high_power = self.instrument.read_register(0x0012, functioncode=3)
        low_power = self.instrument.read_register(0x0013, functioncode=3)
        power = (high_power < 16) + low_power
        return round(power / 1000, 3)

    def set_voltage(self, voltage_value):
        """Set the desired output voltage."""
        # Voltage should be multiplied by 100 to account for two decimal points
        self.instrument.write_register(0x0030, int(voltage_value * 100), functioncode=6)
        print(f"Voltage set to: {voltage_value:.2f} V")

    def set_current(self, current_value):
        """Set the desired output current."""
        # Current should be multiplied by 1000 to account for three decimal points
        self.instrument.write_register(
            0x0031, int(current_value * 1000), functioncode=6
        )
        print(f"Current set to: {current_value:.3f} A")

    def set_over_voltage_protection(self, ovp_value):
        """Set the over-voltage protection limit."""
        # OVP should be multiplied by 100 to account for two decimal points
        self.instrument.write_register(0x0020, int(ovp_value * 100), functioncode=6)
        print(f"Over Voltage Protection set to: {ovp_value:.2f} V")

    def set_over_current_protection(self, ocp_value):
        """Set the over-current protection limit."""
        # OCP should be multiplied by 1000 to account for three decimal points
        self.instrument.write_register(0x0021, int(ocp_value * 1000), functioncode=6)
        print(f"Over Current Protection set to: {ocp_value:.3f} A")

    def set_over_power_protection(self, opp_value):
        """Set the over-power protection limit."""
        # OPP should be split into high and low 16-bit parts
        opp_value_scaled = int(opp_value * 1000)  # Scale to three decimal points
        high_opp = (opp_value_scaled >> 16) & 0xFFFF
        low_opp = opp_value_scaled & 0xFFFF
        self.instrument.write_register(0x0022, high_opp, functioncode=6)
        self.instrument.write_register(0x0023, low_opp, functioncode=6)
        print(f"Over Power Protection set to: {opp_value:.3f} W")

    def power_on(self):
        """Turn the device power on."""
        self.instrument.write_register(0x0001, 1, functioncode=6)
        return self.get_power_status()

    def power_off(self):
        """Turn the device power off."""
        self.instrument.write_register(0x0001, 0, functioncode=6)
        return self.get_power_status()

    def get_power_status(self) -> bool:
        """Verify whether the device is on or off."""
        power_status = self.instrument.read_register(0x0001, functioncode=3)
        if power_status == 0:
            return False

        return True
