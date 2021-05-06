# Process the photo

def photo(photo_name):
    from PIL import Image
    photo = Image.open(photo_name)
    
    return print('''
    Successfully loaded image!
    Image size: {w} x {h}'''.format(
    w=photo.width, h=photo.height))

#Pixel matrix:

pixel_matrix = []

def px_matrix(photo_name):
    
    from PIL import Image
    photo = Image.open(photo_name)
    
    width, height = photo.size
    pixel = photo.load()
    
    for h in range(height):
        row = []
        for w in range(width):
            row.append(pixel[w,h])
        pixel_matrix.append(row)
    
    return pixel_matrix

# Bright matrix:

brightness = []

def bright_matrix():
    for rgb_list in pixel_matrix:
        row = []
        for rgb in rgb_list:
            average = sum(rgb)//3 
            row.append(average)
        brightness.append(row)
    
    return brightness

# ASCII mapping:

ascii_letter = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_matrix = []
ascii_ratio = 255 / len(ascii_letter)

def ascii_map():
    for bright_list in brightness:
        row = []
        for bright in bright_list:
            ascii_value = int(bright/ascii_ratio)
            letter = ascii_letter[ascii_value-1]*3
            row.append(letter)
        ascii_matrix.append(row)
    
    return ascii_matrix

# Print ASCII art!:

def ascii_photo():
    for row in ascii_matrix:
        print(''.join(row))

photo('dog.jpeg')
px_matrix('dog.jpeg')
bright_matrix()
ascii_map()
ascii_photo()