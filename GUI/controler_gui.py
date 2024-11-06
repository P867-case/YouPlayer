from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from System.Json_Api import Proccesing_file
from kivymd.app import MDApp
from .setting_gui import *
import webbrowser

from kivymd.uix.screen import MDScreen
from kivymd.uix.fitimage import FitImage


class MainManger(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_file = Proccesing_file()
        self.frist = self.data_file.data['app_session']['frist_start']

        if self.frist is True:
            self.ids.global_manager.current = 'welcome'

    def change_image(self, *args):
        self.ids.albom.source = 'Images/UI.png'
        self.ids.albom.reload()

    def change_main_scenes(self, name: str):
        self.ids.screen_manager.transition = FadeTransition(
            duration=fadetrasnsition_time
        )
        self.ids.screen_manager.current = name

    def open_web_pay(self, *args):
        webbrowser.open_new_tab(
            'https://www.tinkoff.ru/rm/cherpakov.artem17/ONiEE52468'
        )
        self.data_file.data['app_session']['frist_start'] = False
        self.data_file.save()
        self.data_file.update()
        self.ids.global_manager.current = 'main'

    def set_new_state(self, *args):
        self.data_file.data['app_session']['frist_start'] = False
        self.data_file.save()
        self.data_file.update()
        self.ids.global_manager.current = 'main'


class application(MDApp):
    def build(self):
        self.theme_cls.theme_style = theme_style
        self.theme_cls.primary_palette = theme_primary_palette
        self.main_widget = MainManger()

        return self.main_widget


if __name__ == '__main__':
    application().run()
