print("*****************************************")
print("Welcome to CRC (Cycle Redundancy Check) Machine")  # by Om Hinge 52 SECA
print("*****************************************")
data = input("Enter the data bits:")
gen = input("Enter the generator bits:")
print("*****************************************")
print("The data bits are:", data)
print("The generator bits are:", gen)
print("*****************************************")
data += "0" * (len(gen) - 1)
data_list = list(data)
gen_list = list(gen)
for i in range(len(data) - len(gen) + 1):
    if data_list[i] == "1":
        for j in range(len(gen)):
            data_list[i+j] = str(int(data_list[i+j]) ^ int(gen_list[j]))
rem = "".join(data_list[-(len(gen) - 1):])
print("The remainder bits are:", rem)
print("*****************************************")
transmitted_data = data[:-len(gen)+1] + rem
print("The transmitted data bits are:", transmitted_data)
print("*****************************************")
received_data = input("Enter the received data bits:")
print("*****************************************")
received_list = list(received_data)
for i in range(len(received_data) - len(gen) + 1):
    if received_list[i] == "1":
        for j in range(len(gen)):
            received_list[i+j] = str(int(received_list[i+j]) ^ int(gen_list[j]))
rem_received = "".join(received_list[-(len(gen) - 1):])
print("The remainder bits are:", rem_received)
print("*****************************************")
if "1" in received_list:
    print("The received data bits are incorrect")
else:
    print("The received data bits are correct")
print("*****************************************")
