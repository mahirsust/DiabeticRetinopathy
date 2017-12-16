from PIL import Image


def rotate(image_path, degrees_to_rotate, saved_location):
    """
    Rotate the given photo the amount of given degreesk, show it and save it

    @param image_path: The path to the image to edit
    @param degrees_to_rotate: The number of degrees to rotate the image
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(saved_location)
    #rotated_image.show()

    print("Succeeded Rotating 90° Image %s " % image_path)

if __name__ == '__main__':
    image = 'H:/xampp/htdocs/DiabeticRetinopathy/new_images/img/11_left.jpeg'
    image_mirror = 'H:/xampp/htdocs/DiabeticRetinopathy/MirrorImages/11_m_left.jpeg'
    rotate(image, 90, 'H:/xampp/htdocs/DiabeticRetinopathy/rot90/11_left_90.jpeg')
    rotate(image_mirror, 90, 'H:/xampp/htdocs/DiabeticRetinopathy/m_rot90/11_m_left_90.jpeg')