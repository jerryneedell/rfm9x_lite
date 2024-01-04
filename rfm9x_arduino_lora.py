# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Example to display raw packets including header
# Author: Jerry Needell
#
import board
import busio
import digitalio
import rfm9x_lite
import time
# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip.
CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze RFM radio
rfm9x = rfm9x_lite.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# Wait to receive packets.
print("Waiting for packets...")
# initialize flag and timer
while True:
    # Look for a new packet: 
    packet = rfm9x.receive()
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("Received (raw header+payload):", [hex(x) for x in packet[0:]])
        print("Received (raw header+payload): {0}".format(packet[0:]))
        print("RSSI: {0}".format(rfm9x.last_rssi))
        time.sleep(.25)
        # send reading after any packet received
        rfm9x.send(bytes("got one!/r/n","UTF-8"))

