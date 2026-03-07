class Device:
    def __init__(self, mac_address: str):
        self.mac_address = mac_address
        self.received_data = None

class Network:
    def __init__(self):
        self.devices = {}

    def add_device(self, device: Device):
        if device.mac_address in self.devices:
            print(f"Device with MAC {device.mac_address} already exists.")
        else:
            self.devices[device.mac_address] = device
            print(f"Device {device.mac_address} added to the network.")

    def send_data(self, data, device_mac):
        device = self.devices.get(device_mac)
        if device:
            device.received_data = data
            print(f"Data successfully sent to device {device_mac}")
        else:
            print("MAC address is wrong… unable to send data.")

phone = Device("00:1A:2B:3C:4D:5E")
laptop = Device("11:22:33:44:55:66")
tablet = Device("AA:BB:CC:DD:EE:FF")

router = Network()
router.add_device(phone)
router.add_device(laptop)
router.add_device(tablet)

router.send_data("www.youtube.com", "11:22:33:44:55:66")
router.send_data("www.github.com", "AA:BB:CC:DD:EE:FF")

print(laptop.received_data)
print(tablet.received_data)
