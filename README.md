# colorize-separation
A simple Python script to colorize grayscale separations.

This script takes grayscale images file paths as arguments and tries to determine the color separation by the filenames.

It loads a CSV file containing process and spot color names and its respective RGB values for the colorized representation into two dictionaries: PROCESS_COLORS and SPOT_COLORS.

Than it tries to match the separation name with the keys in the according dictionary to get the RGB values used in the colorization process*.
*Pillow library is required.

Finally, it saves the colorized version as a PNG.
