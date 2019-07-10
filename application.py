from imageHandler import ImageHandler

class Application:
    def __init__(self):
        self.configure()


    def configure():
        self.__boxes_count__ = 1
        self.__unselected_box_color = (0, 255, 0)
        self.__selected_box_color = (255, 0, 0)

        with open(config_file, 'r') as configFile:
            for line in configFile:
                try:
                    key, value = line.split(' = ', 1)
                    if key == 'boxes_count':
                        self.__boxes_count__ = int(value)
                    elif key == 'unselected_box_color':
                        self.__unselected_box_color__ = tuple(int(value.split(',',2)))
                    elif key == 'selected_box_color':
                        self.__selected_box_color__ = tuple(int(value.split(',',2)))
                    else:
                        pass
                except:
                    pass
        self__show_config__() 
        self.__image_handler__ = ImageHandler()



    def __show_config__(self):
        print('Boxes Count', self.__boxes_count__)
        print('Unselected Box Color', self.__unselected_box_color__)
        print('Selected Box Color', self.__selected_box_color__)
        return
