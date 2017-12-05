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
    image = 'H:/Python_Soft/Diabetic_Retinopathy/new_images/img/1_img.jpg'
    image_mirror = 'H:/Python_Soft/Diabetic_Retinopathy/MirrorImages/1_m_img.jpg'
    rotate(image, 90, 'H:/Python_Soft/Diabetic_Retinopathy/rot90/1_img_90.jpg')
    rotate(image_mirror, 90, 'H:/Python_Soft/Diabetic_Retinopathy/m_rot90/1_m_img_90.jpg')