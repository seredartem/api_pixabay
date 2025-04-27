from class_image_system import Image_system

image_system = Image_system()
stop = False
image_system.load_settings()


while stop == False:
    print('1 - Install image')
    print('2 - Settings')
    print('3 - Exit')
    
    action = int(input('Enter num: '))

    if action == 1:
        image = None
        print('1 - Enter name picture')
        print('2 - Take next picture')
        action_1 = int(input('Enter num: '))
        if action_1 == 1:
            image_name = input('Enter name of picture: ')
            image = image_name
            image_system.response_image(image_name,image_system.folder_path, image_system.image_type, image_system.page, image_system.quantity)

        elif action_1 == 2:
            image_system.page += 1
            image_system.response_image(image_name,image_system.folder_path, image_system.image_type, image_system.page, image_system.quantity)

    elif action == 2:
        print('1 - Edit folder')
        print('2 - Enter how much picture(default -> 1)')
        action_2 = int(input('Enter num: '))
        if action_2 == 1:
            new_folder = input('Enter path to folder: ')
            image_system.folder_path = new_folder
        elif action_2 == 2:
            quantity = int(input('Enter how much picture: '))
            image_system.quantity = quantity

    elif action == 3:
        image_system.save_settings()
        stop = True