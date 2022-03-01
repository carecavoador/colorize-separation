from PIL import Image, ImageOps
from csv import reader
from os import path
from sys import argv


CSV_FILE = "colors.csv"

FILES = argv[1:]

PROCESS_COLORS = {}
PANTONE_COLORS = {}

def load_colors_from_csv(file):
    """
    Load RGB values from CSV file into color dictionaries
    """
    with open(CSV_FILE, mode='r', encoding='utf-8-sig') as f:
        
        color_table = reader(f)
        
        for color in color_table:

            # Gets color name from first column
            color_name = color[0].lower()
            
            # Gets RGB values from columns 2, 3 and 4
            rgb = (int(color[1]), int(color[2]), int(color[3]))
            
            # Checks in fifth column if color is "process" or "spot"
            if color[4] == 'process':
                PROCESS_COLORS[color_name] = rgb
            elif color[4] == 'spot':
                PANTONE_COLORS[color_name] = rgb
            else:
                print(f"Impossible to determine if {color_name} is process or spot color.")


def get_color_rgb_value(file_name):
    """
    Returns a touple containing specific color's RGB value from color dictionaries
    """
    # If last word is a process color
    if file_name[-1] in PROCESS_COLORS.keys():
        return PROCESS_COLORS[file_name[-1]]
    
    # If there is "PANTONE" in filename
    elif 'pantone' in file_name:
        idx_pantone = file_name.index('pantone')
        pantone_name = ' '.join(file_name[idx_pantone:])
        if pantone_name in PANTONE_COLORS.keys():
            return PANTONE_COLORS[pantone_name]
        else:
            return False
    else:
        return False


def set_color_to_image(grayscale_image, rgb_value):
    """
    Colorizes a grayscale image with given RGB value
    """
    image = Image.open(grayscale_image)

    colorized = ImageOps.colorize(image, black=rgb_value, white="white")
    
    new_image = path.basename(grayscale_image).split('.')[0] + '.png'
    
    colorized.save(new_image)


def main():
    if __name__ == '__main__':

        load_colors_from_csv(CSV_FILE)

        for img_file in FILES:

            img_file_name = path.basename(img_file).split('.')[0]
            img_file_name = img_file_name.lower()
            img_file_name = img_file_name.split()

            color_rgb = get_color_rgb_value(img_file_name)

            if color_rgb:
                set_color_to_image(img_file, color_rgb)
            else:
                print("Impossible to determine color name from file.")


main()
print("Finished!")
