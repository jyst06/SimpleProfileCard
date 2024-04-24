import configparser
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
file_name = "config.ini"
file_name = os.path.join(current_folder, file_name)

#use to get config value
def get_val(*, type : str, name : str):
    config = configparser.ConfigParser()
    config.read(file_name)

    return config[type][name]

#use to set config value
def set_val(*, type : str, name : str, val : str):
    config = configparser.ConfigParser()
    config.read(file_name)
    config.set(type, name, val)
    with open(file_name, 'w') as configfile:
        config.write(configfile)

#use to get config dict
def get_val_dict(type : str):
    config = configparser.ConfigParser()
    config.read(file_name)
    return config[type]


def reset_config():
    config = configparser.ConfigParser()

    config['Run'] = {
        'first': 'false'
    }
    config['Parameters'] = {
        'type': '',
        'profile_page_link': '',
        'profile_pic_link': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png',
        'profile_name': ''
    }
    config['Optional'] = {
        'style': "1",
        'theme': 'dark',
        'site_title': 'About Author',
        'card_title': 'About Me',
        'background_pic_link': '',
        'profile_id': '',
        'info': '',
        'contect': ''
    }
    config['Badge'] = {
        'badge0': ''
    }

    with open(file_name, 'w') as configfile:
        config.write(configfile)

    print("Configuration reset to default values.")


if __name__ == '__main__':
    a = "1"
    set_val(type="Optional", name="style", val=a)