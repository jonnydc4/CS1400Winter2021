def grayscale2(image):
    """Converts an image to grayscale using the crude average
    of the r, g, and b"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            ave = (r + g + b)// 3
            image.setPixel(x, y, (ave, ave, ave))