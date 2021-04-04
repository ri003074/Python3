input_data = {0: "1", 1: "8,192", 2: "2", 3: "10,20"}

dut_pin = {}
print(len(input_data))
for i in range(0, len(input_data), 2):
    dut_pin[input_data[i]] = input_data[i + 1].split(",")

print(dut_pin)
