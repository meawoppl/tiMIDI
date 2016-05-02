import platform
import os


def autodetectMidiDevices(searchDir="/dev"):
    assert "Linux" in platform.system(), "Autodetection on Linux only"
    allDevices = os.listdir("/dev")
    midiDevices = [dev for dev in allDevices if dev.startswith("midi")]

    # Echo the device list, and details about the device
    print("Device Name     Readable     Writiable")
    for device in midiDevices:
        devPath = os.path.join(searchDir, device)
        readable = os.access(device, os.R_OK)
        writable = os.access(device, os.W_OK)

        print(devPath, readable, writable)


if __name__ == "__main__":
    autodetectMidiDevices()
