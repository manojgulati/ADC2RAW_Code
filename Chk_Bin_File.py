# Chk_Bin_File


for i in range(256):
    with open("test.raw", "ab") as f:
        f.write(bytes([i]))