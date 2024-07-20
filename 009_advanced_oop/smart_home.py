#!/usr/bin/python3

"""
This file contains solution to day #9 challenge:

Create a system to model a smart home with various devices.

Implement the following:

1. An abstract base class SmartDevice with:

Abstract methods: turn_on(), turn_off(), status()
A class method to track the total number of devices


2. Two concrete classes inheriting from SmartDevice:

SmartLight: Has brightness level and color
SmartThermostat: Has temperature setting

3. A SmartHome class that:

Can add and remove devices
Implements a context manager protocol to power all devices on/off
Uses a custom iterator to cycle through all devices


4. Implement property decorators for appropriate attributes

5. Use at least one dunder (magic) method in each class

6. Create a simple command-line interface 
to interact with the smart home system
"""


from abc import ABC, abstractmethod

class SmartDevice(ABC):
    _total_devices = 0

    def __init__(self, name):
        self.name = name
        self._is_on = False
        SmartDevice._total_devices += 1

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def status(self):
        pass

    @classmethod
    def get_total_devices(cls):
        return cls._total_devices

class SmartLight(SmartDevice):
    def __init__(self, name, max_brightness=100):
        super().__init__(name)
        self._brightness = 0
        self._color = "white"
        self._max_brightness = max_brightness

    def turn_on(self):
        self._is_on = True
        self._brightness = self._max_brightness // 2

    def turn_off(self):
        self._is_on = False
        self._brightness = 0

    def status(self):
        return (f"Light {self.name} is {'on' if self._is_on else 'off'}, "
                f"brightness: {self._brightness}, color: {self._color}")

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if 0 <= value <= self._max_brightness:
            self._brightness = value
        else:
            raise ValueError(f"Brightness must be between 0 and {self._max_brightness}")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def __str__(self):
        return f"SmartLight: {self.name}"

class SmartThermostat(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self._temperature = 20

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    def status(self):
        return (f"Thermostat {self.name} is {'on' if self._is_on else\
                'off'}, "
                f"temperature: {self._temperature}°C")

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if 10 <= value <= 30:
            self._temperature = value
        else:
            raise ValueError("Temperature must be between\
                    10°C and 30°C")

    def __str__(self):
        return f"SmartThermostat: {self.name}"

class SmartHome:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        if isinstance(device, SmartDevice):
            self.devices.append(device)
        else:
            raise TypeError("Device must be a SmartDevice")

    def remove_device(self, device):
        self.devices.remove(device)

    def __enter__(self):
        for device in self.devices:
            device.turn_on()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for device in self.devices:
            device.turn_off()

    def __iter__(self):
        return iter(self.devices)

    def __str__(self):
        return f"SmartHome with {len(self.devices)} devices"

def main():
    home = SmartHome()
    home.add_device(SmartLight("Living Room Light"))
    home.add_device(SmartLight("Bedroom Light"))
    home.add_device(SmartThermostat("Main Thermostat"))

    while True:
        print("\nSmart Home Control")
        print("1. Turn on all devices")
        print("2. Turn off all devices")
        print("3. Check device status")
        print("4. Adjust device settings")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            with home:
                print("All devices turned on.")
        elif choice == '2':
            for device in home:
                device.turn_off()
            print("All devices turned off.")
        elif choice == '3':
            for device in home:
                print(device.status())
        elif choice == '4':
            for i, device in enumerate(home.devices, 1):
                print(f"{i}. {device}")
            device_choice = int(input("Choose a device: ")) - 1
            if 0 <= device_choice < len(home.devices):
                device = home.devices[device_choice]
                if isinstance(device, SmartLight):
                    device.brightness = int(input("Enter brightness\
                            (0-100): "))
                    device.color = input("Enter color: ")
                elif isinstance(device, SmartThermostat):
                    device.temperature = float(input("Enter \
                            temperature (10-30°C): "))
                print(f"Settings updated. {device.status()}")
            else:
                print("Invalid device choice.")
        elif choice == '5':
            print("Exiting Smart Home Control.")
            break
        else:
            print("Invalid choice. Please try again.")

    print(f"Total devices created: {SmartDevice.get_total_devices()}")

if __name__ == "__main__":
    main()
