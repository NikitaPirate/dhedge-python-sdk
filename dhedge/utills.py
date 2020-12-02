def strTo32HexString(string_key):
    bytes_key = string_key.encode()
    hex_key = bytes_key.hex()
    hex_key32 = '0x' + hex_key + (64 - len(hex_key)) * '0'
    return hex_key32


def parseBytes32String(key):
    result = bytes.fromhex(str(key)[2:])
    result = result.decode('utf-8').rstrip('\x00')
    return result


def toEther(number):
    return round(number / 1000000000000000000, 3)
