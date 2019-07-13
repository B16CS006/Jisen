from imageHandler import ImageHandler


class Application:
    def __init__(self, database_dir='database'):
        self.__database__ = database_dir
        self.__image_handler__ = ImageHandler(database_dir='database')
        self._configure()

    def _configure(self, config_file='jisen.config'):
        with open(config_file, 'r') as configFile:
            for line in configFile:
                try:
                    key, value = line.split(' = ', 1)
                    if key == 'boxes_count':
                        __boxes_count__ = int(value)
                    elif key == 'unselected_box_color':
                        __unselected_box_color__ = tuple([int(element) for element in value.split(',', 2)])
                    elif key == 'selected_box_color':
                        __selected_box_color__ = tuple([int(element) for element in value.split(',', 2)])
                    elif key == 'boxes':
                        value = [box_value for box_value in value.split(',')]
                        __boxes__ = []
                        for box_value in value:
                            __boxes__.append([int(element) for element in box_value.split(';', 3)])
                    else:
                        pass
                except:
                    pass
        self.__image_handler__.setBoxes([])
        self.__image_handler__.set_selected_box_color(__selected_box_color__)
        self.__image_handler__.set_unselected_box_color(__unselected_box_color__)
        for i in range(__boxes_count__):
            self.__image_handler__.addBox(__boxes__[i])
        self.values = None
        self._show_config()

    def _reset_config_file(self, config_file='jisen.config'):
        with open(config_file, 'w') as configFile:
            configFile.writelines([
                'boxes_count = 2\n',
                'unselected_box_color = 0,255,0\n',
                'selected_box_color = 255,0,0\n'
            ])
        configFile.close()
        self._configure(config_file)
        return

    def _show_config(self):
        print('Boxes Count', self.__image_handler__.boxCount())
        print('Unselected Box Color', self.__image_handler__.__unselected_box_color__)
        print('Selected Box Color', self.__image_handler__.__selected_box_color__)
        return

    def _read_image_(self):
        self.values = []
        for i in range(self.__image_handler__.boxCount()):
            self.values.append(self.__image_handler__.read_image(i))
        # print(self.values)
