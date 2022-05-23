def int32_to_ip(int32):
    ip4 = int32 & 255
    ip3 = ((int32 >> 8) & 255)
    ip2 = ((int32 >> 16) & 255)
    ip1 = ((int32 >> 24) & 255)
    ip = f"{ip1}.{ip2}.{ip3}.{ip4}"
    return ip

print(int32_to_ip(2154959208))
print(int32_to_ip(0))
print(int32_to_ip(2149583361))

# Using bitwise operations in python in order to translate the ip