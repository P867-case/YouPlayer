from GUI import controler_gui
from System.Json_Api import Proccesing_file
import platform
import getpass

os = platform.system()
file_settings = Proccesing_file()

if os == 'Linux':
    file_settings.data['default_path'] = [
        f'/home/{getpass.getuser()}/Загрузки',
        f"/home/{getpass.getuser()}/Музыка"
    ]
elif os == 'Windwos':
    file_settings.data['default_path'] = [
        f"C:\\Users\\{getpass.getuser()}\\Music",
        f"C:\\Users\\{getpass.getuser()}\\Downloads"
    ]

file_settings.save()

controler_gui.application().run()
