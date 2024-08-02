"""Hanmatek Power Supply, should be able to represent all from the HM Series."""

import minimalmodbus


class HanmatekHmInstrument(minimalmodbus.Instrument):
    def __init__(self, port: str, addr: int = 1) -> None:
        """
        Initialize the HM device with the specified port and slave address.

        :param port: The serial port to which the device is connected.
        :param slave_address: The Modbus slave address of the device.
        """

        super().__init__(
            port,
            slaveaddress=addr,
            mode=minimalmodbus.MODE_RTU,
            debug=False,
        )

        if self.serial is None:
            raise ValueError("Serial not found.")
        self.serial.baudrate = 9600
        self.serial.bytesize = 8
        self.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.serial.stopbits = 1
        self.serial.timeout = 1
