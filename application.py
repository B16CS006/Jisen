from imageHandler import ImageHandler


class Application:
    def __init__(self, database_dir='database'):
        self.image_handler = ImageHandler(database_dir=database_dir)
        self._configure()

    # noinspection PyBroadException
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
        self.image_handler.boxes = []
        self.image_handler.selected_box_color = __selected_box_color__
        self.image_handler.unselected_box_color = __unselected_box_color__

        for i in range(__boxes_count__):
            self.image_handler.addBox(__boxes__[i])

        self.values = None
        self._show_config()

    @property
    def image_handler(self):
        return self._image_handler

    @image_handler.setter
    def image_handler(self, image_handler):
        if isinstance(image_handler, ImageHandler):
            self._image_handler = image_handler

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        if isinstance(values, list):
            self._values = values

    def _reset_config_file(self, config_file='jisen.config'):
        with open(config_file, 'w') as configFile:
            configFile.writelines([
                'boxes_count = 2\n',
                'unselected_box_color = 0,255,0\n',
                'selected_box_color = 255,0,0\n',
                'boxes = 117;237;80;25,117;262;100;25\n'
            ])
        configFile.close()
        self._configure(config_file)
        return

    def _show_config(self):
        print('Boxes Count', self.image_handler.boxCount())
        print('Unselected Box Color', self.image_handler.unselected_box_color)
        print('Selected Box Color', self.image_handler.selected_box_color)
        return

    def _read_image_(self):
        self.values = []
        for i in range(self.image_handler.boxCount()):
            self.values.append(self.image_handler.read_image(i))
        # print(self.values)
