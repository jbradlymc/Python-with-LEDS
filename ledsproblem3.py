LED0 = 1 << 0  # 00000001
LED1 = 1 << 1  # 00000010
LED2 = 1 << 2  # 00000100
LED3 = 1 << 3  # 00001000
LED4 = 1 << 4  # 00010000
LED5 = 1 << 5  # 00100000
LED6 = 1 << 6  # 01000000
LED7 = 1 << 7  # 10000000

leds = 0

for i in range(256):
    print(bin(leds))
    # Increment leds by 1 using bitwise operations
    carry = 1

    for j in range(8):
        if carry == 0:
            break
        if leds & (1 << j):
            leds &= ~(1 << j)  # Turn off the bit
        else:
            leds |= (1 << j)   # Turn on the bit
            carry = 0
