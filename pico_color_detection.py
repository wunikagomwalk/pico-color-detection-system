from machine import Pin, I2C
from time import sleep_ms, sleep_us, ticks_us, ticks_diff

# =========================================================
# COLOR SENSOR SETUP
# =========================================================

S0 = Pin(2, Pin.OUT)
S1 = Pin(3, Pin.OUT)
S2 = Pin(4, Pin.OUT)
S3 = Pin(5, Pin.OUT)
OUT = Pin(6, Pin.IN)

# 20% frequency scaling
S0.value(1)
S1.value(0)


# =========================================================
# I2C LCD SETUP
# =========================================================

i2c = I2C(
    0,
    sda=Pin(16),
    scl=Pin(17),
    freq=100000
)

LCD_ADDR = 0x27   # CHANGE THIS if scanner showed another address

# PCF8574 bit assignments
LCD_RS = 0x01
LCD_EN = 0x04
LCD_BACKLIGHT = 0x08


def lcd_write_raw(data):
    i2c.writeto(LCD_ADDR, bytes([data | LCD_BACKLIGHT]))


def lcd_pulse(data):
    lcd_write_raw(data | LCD_EN)
    sleep_us(1)

    lcd_write_raw(data & ~LCD_EN)
    sleep_us(50)


def lcd_write_nibble(nibble, rs=0):
    data = (nibble & 0x0F) << 4

    if rs:
        data |= LCD_RS

    lcd_pulse(data)


def lcd_command(cmd):
    lcd_write_nibble(cmd >> 4, 0)
    lcd_write_nibble(cmd & 0x0F, 0)

    if cmd == 0x01:
        sleep_ms(2)


def lcd_char(char):
    value = ord(char)

    lcd_write_nibble(value >> 4, 1)
    lcd_write_nibble(value & 0x0F, 1)


def lcd_text(text):
    for char in text:
        lcd_char(char)


def lcd_clear():
    lcd_command(0x01)
    sleep_ms(2)


def lcd_second_line():
    lcd_command(0xC0)


def lcd_init():

    sleep_ms(50)

    lcd_write_nibble(0x03)
    sleep_ms(5)

    lcd_write_nibble(0x03)
    sleep_us(150)

    lcd_write_nibble(0x03)
    sleep_us(150)

    lcd_write_nibble(0x02)

    # 4-bit mode, 2 lines
    lcd_command(0x28)

    # Display on, cursor off
    lcd_command(0x0C)

    # Clear display
    lcd_command(0x01)

    # Cursor moves right
    lcd_command(0x06)

    sleep_ms(5)


# =========================================================
# COLOR SENSOR FUNCTIONS
# =========================================================

def measure_frequency():

    while OUT.value() == 1:
        pass

    while OUT.value() == 0:
        pass

    start = ticks_us()

    for i in range(20):

        while OUT.value() == 1:
            pass

        while OUT.value() == 0:
            pass

    end = ticks_us()

    elapsed = ticks_diff(end, start)

    if elapsed <= 0:
        return 0

    return int(20 * 1000000 / elapsed)


def read_channel(s2, s3):

    S2.value(s2)
    S3.value(s3)

    sleep_ms(100)

    total = 0

    for i in range(5):
        total += measure_frequency()
        sleep_ms(20)

    return total // 5


def read_red():
    return read_channel(0, 0)


def read_green():
    return read_channel(1, 1)


def read_blue():
    return read_channel(0, 1)


# =========================================================
# COLOR CLASSIFICATION
# =========================================================

def detect_color(r, g, b):

    if r > g and r > b:
        return "RED"

    elif g > r and g > b:
        return "GREEN"

    elif b > r and b > g:
        return "BLUE"

    else:
        return "UNKNOWN"


# =========================================================
# START LCD
# =========================================================

lcd_init()

lcd_clear()
lcd_text("Color Sensor")
lcd_second_line()
lcd_text("Starting...")

sleep_ms(1500)


# =========================================================
# MAIN LOOP
# =========================================================

while True:

    red = read_red()
    green = read_green()
    blue = read_blue()

    color = detect_color(red, green, blue)

    # THONNY OUTPUT
    print("----------------------")
    print("R:", red)
    print("G:", green)
    print("B:", blue)
    print("Detected:", color)
    print("----------------------")

    # LCD OUTPUT
    lcd_clear()

    lcd_text("Detected Color:")

    lcd_second_line()
    lcd_text(color)

    sleep_ms(1000)