from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from .setting_gui import *
from System.Json_Api import Proccesing_file


class MainManger(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_file = Proccesing_file()
        self.frist = self.data_file.data['app_session']['frist_start']

        if self.frist == True:
            self.ids.global_manager.current = 'welcome'


class application(MDApp):
    def build(self):
        self.theme_cls.theme_style = theme_style
        self.theme_cls.primary_palette = theme_primary_palette
        self.main_widget = MainManger()

        return self.main_widget


if __name__ == '__main__':
    application().run()
