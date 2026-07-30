import serial
import csv
import os
import sys
from serial.tools import list_ports

# ==========================
# User Inputs
# ==========================

port = input("Enter COM Port (e.g., COM5): ").strip()
label = input("Enter Activity Label (Idle/Pitch/Roll/Yaw/Shake): ").strip()
num_samples = int(input("Enter Number of Samples to Record: "))

baudrate = 115200
filename = r"D:\TinyML_Workshop-main\TinyML_Workshop_PGR\TinyML_PGR\Data_Logger\dataset.csv"

# ==========================
# Open Serial Port
# ==========================

try:
    ser = serial.Serial(port, baudrate, timeout=1)
except serial.SerialException as exc:
    available_ports = [p.device for p in list_ports.comports()]
    print(f"\nCould not open port {port}: {exc}")
    print("This usually means the port is already in use by another program,")
    print("the device is not connected, or Windows blocked access to the COM port.")
    if available_ports:
        print(f"Available ports: {', '.join(available_ports)}")
    else:
        print("No COM ports were detected.")
    print("Close any serial monitor or other app using the port and try again.")
    sys.exit(1)

# ==========================
# Create CSV if Needed
# ==========================

file_exists = os.path.isfile(filename)

with open(filename, "a", newline="") as csvfile:

    writer = csv.writer(csvfile)

    if not file_exists:
        writer.writerow([
            "Ax",
            "Ay",
            "Az",
            "Gx",
            "Gy",
            "Gz",
            "Label"
        ])

    print("\nRecording Started...\n")

    count = 0

    while count < num_samples:

        line = ser.readline().decode().strip()

        values = line.split(",")

        if len(values) == 6:

            values.append(label)

            writer.writerow(values)

            count += 1

            print(f"Sample {count}/{num_samples}")

print("\nRecording Completed.")

ser.close()