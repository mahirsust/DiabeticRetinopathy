from PIL import Image


def flip_image(image_path, saved_location):
    """
    Flip or mirror the image

    @param image_path: The path to the image to edit
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)
    #rotated_image.show()
    print("Succeeded Mirroring Image %s " % image_path)

if __name__ == '__main__':
    image = 'H:/Python_Soft/Diabetic_Retinopathy/new_images/img/1_img.jpg'
    flip_image(image, 'H:/Python_Soft/Diabetic_Retinopathy/MirrorImages/1_m_img.jpg')