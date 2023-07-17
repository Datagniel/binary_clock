#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes
import os
import pygame
from pygame.locals import NOFRAME, QUIT, MOUSEBUTTONDOWN
import time
import win32con
import win32gui

# Define colors
DARK_RED = (100, 0, 0)
BRIGHT_RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock settings
clock_width = 165
clock_height = 105
bit_radius = 10
bit_padding = 5
bit_color = DARK_RED
activated_color = BRIGHT_RED

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Get the size of the display screen
screen_info = pygame.display.Info()

# Calculate the position to place the window in the bottom right corner
window_pos_x = screen_info.current_w - clock_width
window_pos_y = screen_info.current_h - clock_height

# Set the position of the window
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{window_pos_x},{window_pos_y}"

screen = pygame.display.set_mode((clock_width, clock_height), pygame.NOFRAME)
pygame.display.set_caption("Binary Clock")

# Find the Pygame window handle
hwnd = pygame.display.get_wm_info()["window"]

# Function to set window always on top
def set_window_always_on_top():
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

def draw_bit(x, y, activated):
    color = activated_color if activated else bit_color
    pygame.draw.circle(screen, color, (x, y), bit_radius)

def draw_clock(bits):
    screen.fill(BLACK)
    x = 10
    x += bit_padding
    for idx, column in enumerate(bits):
        y = clock_height - bit_radius - 5 - (len(column) - 1) * (bit_radius * 2 + bit_padding)
        for bit in column:
            draw_bit(x, y, bit)
            y += bit_radius * 2 + bit_padding
        if idx in [1, 3]:
            x += bit_radius * 2 + bit_padding + 5
        else:
            x += bit_radius * 2 + bit_padding

def get_binary_representation(number, num_bits):
    binary = bin(number)[2:]
    binary = binary.zfill(num_bits)
    return [int(bit) for bit in binary]

# Function to handle window dragging
def handle_window_drag():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ctypes.windll.user32.ReleaseCapture()
            HWND = pygame.display.get_wm_info()["window"]
            ctypes.windll.user32.SendMessageW(HWND, 0xA1, 0x2, 0)
        elif event.type == QUIT:
            running = False

# Main loop
running = True
while running:
    handle_window_drag()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    current_time = time.localtime()
    hour_10s = get_binary_representation(current_time.tm_hour // 10, 2)
    hour_1s = get_binary_representation(current_time.tm_hour % 10, 3)
    minute_10s = get_binary_representation(current_time.tm_min // 10, 3)
    minute_1s = get_binary_representation(current_time.tm_min % 10, 4)
    second_10s = get_binary_representation(current_time.tm_sec // 10, 3)
    second_1s = get_binary_representation(current_time.tm_sec % 10, 4)

    bits = [hour_10s, hour_1s, minute_10s, minute_1s, second_10s, second_1s]

    # Set the window always on top each frame
    set_window_always_on_top()

    draw_clock(bits)
    pygame.display.flip()
    clock.tick()  # Update clock

# Quit Pygame
pygame.quit()
