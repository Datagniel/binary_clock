# Binary Clock

![Binary Clock](pictures/clock.png)

This Python script displays a binary clock with little red circles representing the bits. The circles become bright red when activated. The clock displays the time in binary format, with columns representing 10s of hours, 1s of hours, 10s of minutes, 1s of minutes, 10s of seconds, and 1s of seconds.

## Features

- Displays a binary clock with red circles
- Real-time synchronization with the system clock
- Customizable colors and appearance

## Requirements

- Python 3.x
- Pygame library (install with `conda install -c conda-forge pygame` or `pip install pygame`)
- Pywin32 library (install with `conda install -c conda-forge pywin32` or `pip install pywin32`)
- ctypes library (included in Python standard library)

## Usage

1. Clone the repository or download the `binary_clock.py` file.
2. Install the Pygame library if not already installed.
3. Install the Pywin32 library if not already installed.
4. Run the script: `python binary_clock.py`.

## Customization

You can customize the appearance of the clock by modifying the variables in the script. Adjust the colors, sizes, or other settings to suit your preferences.

## Screenshots

![Screenshot 1](pictures/screenshot1.png)

![Screenshot 2](pictures/screenshot2.png)

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to fork, modify, and distribute the code. Contributions are welcome!

## Acknowledgements

- This script was inspired by [Scott's Binary Clock](https://www.sb-software.com/binaryclock/binclock.html).