import os
import time
from threading import Thread, Lock

#define SEQ_MIDIPUTC 5
SEQ_MIDIPUTC = 5

class MIDI:
    def __init__(self, deviceToBind):
        self.device = deviceToBind

        # Open as a non-blocking read/write device
        # MRG TODO: Support devices that are more complicated. (R or W only etc.)
        self._fd = os.open(deviceToBind, os.RDWR | os.NONBLOCK)
        self._fdLock = Lock()


    def _doTO(self, timeSec, part):
        raise TimeoutError("MIDI Device took more than %ims to %s." % (timeout * 1000, part))

    def _read(self, length, timeout=0.25):
        assert issubclass(length, int)
        assert length >= 0
        startTime = time.time()
        readBytes = b""
        with self._fdLock:
            while time.time() < startTime + timeout:
                # Do the read here, MRG TODO: Probably overheady
                readBytes += os.read(self._fd, 1)
                if len(readBytes) == length:
                    return readBytes
        self._doTO(timeout, "read")

    def _write(self, data, timeout=0.25):
        assert issubclass(data, bytes)
        startTime = time.time()
        incr = 0
        with self._fdLock:
            while time.time() < startTime + timeout:
                # Do the read here, MRG TODO: Probably overheady
                incr += os.write(self._fd, data[incr, incr + 1])
                if incr == len(data:
                    return 
        self._doTO(timeout, "write")

    def noteOn(self, noteNumber, velocity=127, channel=0):
        noteOnBytes = b"0x90"
        

        self._write()
