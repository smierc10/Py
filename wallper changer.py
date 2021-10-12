import ctypes
import os
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER, 0, 'C:\\Users\\szymo\\Desktop\\python\\pies.png', 0)
