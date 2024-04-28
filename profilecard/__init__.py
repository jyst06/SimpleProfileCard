__version__ = "1.0.8"

from .simple import Pack, show
from .simple import set_val, get_val, reset_config as rc


class Pf:
    """
    This class is use to setup a personal profile card
    """
    def __init__(self, *, first : bool = False):
        self.style = "1"
        self.type = None
        self.link = None
        self.pic = None
        self.name = None
        self.stitle = 'About Author'
        self.ctitle = 'About Me'
        self.theme = 'dark'
        self.bg = None
        self.info = None
        self.contect = None
        self.badge = None

        self.badge_counter = 0

        if get_val(type="Run", name="first") == "stop" and first == True:
            pass
        else:
            set_val(type="Run", name="first", val=str(first).lower())


    def set_style(self, style : str = "1"):
        """
        This function is use to set the style of profile card
        ('1' , '2' , '3')
        (Default : '1')
        """
        set_val(type='Optional', name="style", val=style)

        self.style = style

        return f"Style:{self.style}"


    def set_type(self, *, type : str, link : str = ""):
        """
        This function is use to set the type of profile card
        type : support -> ('github' , 'youtube' , 'reddit' , 'custom')
        link : ('LINK OF PROFILE PAGE')
        """
        if type == 'custom':
            set_val(type='Parameters', name="type", val=type)

        elif type in ['github', 'youtube', 'reddit', 'leetcode']:
            set_val(type='Parameters', name="type", val=type)
            set_val(type='Parameters', name="profile_page_link", val=link)

        else:
            raise ValueError(f'ProfileCard Error : Invalid type "{type}"')

        self.type = type
        self.link = link

        return f"Type:{self.type} Link:{self.link}"


    def set_pic(self, link : str):
        """
        This function is use to set the profile picture for custom site
        (Default : 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
        """
        set_val(type='Parameters', name="profile_pic_link", val=link)

        self.pic = link

        return f"Pic:{self.pic}"


    def set_name(self, name : str):
        """
        This function is use to set the name for custom site
        """
        set_val(type='Parameters', name="profile_name", val=name)

        self.name = name

        return f"Name:{self.name}"


    def set_site_title(self, title : str):
        """
        This function is use to set the title
        (Default : 'About Author')
        """
        set_val(type='Optional', name="site_title", val=title)

        self.stitle = title

        return f"Site Title:{self.stitle}"


    def set_card_title(self, title : str):
        """
        This function is use to set the title
        (Default : 'About Me')
        """
        set_val(type='Optional', name="card_title", val=title)

        self.ctitle = title

        return f"Card Title:{self.ctitle}"


    def set_theme(self, theme : str):
        """
        This function is use to set the theme
        (light , dark)
        """
        set_val(type='Optional', name="theme", val=theme)

        self.theme = theme

        return f"Theme:{self.theme}"


    def set_background_pic(self, link : str):
        """
        This function is use to set the background picture
        (Default : None)
        """
        set_val(type='Optional', name="background_pic_link", val=link)

        self.bg = link

        return f"Background Pic:{self.bg}"


    def add_id(self, id : str = ""):
        """
        This function is use to add the id text
        (Default : "")
        """
        set_val(type='Optional', name="profile_id", val=id)

        self.id = id

        return f"ID:{self.id}"


    def add_info(self, info : str):
        """
        This function is use to add the info text
        (Default : None)
        """
        set_val(type='Optional', name="info", val=info)

        self.info = info

        return f"Info:{self.info}"


    def add_contect(self, contect : str):
        """
        This function is use to add the contect text
        (Default : None)
        """
        set_val(type='Optional', name="contect", val=contect)

        self.contect = contect

        return f"Contect:{self.contect}"


    def add_badge(self, *, icon : str, style : str = "for-the-badge", color : str = "white", bg_color : str = "black", text : str = "_", link : str = ""):
        """
        This function is use to add the badge
        icon(Required) : ('github' , 'youtube' , 'facebook' , 'twitter' , 'instagram' , 'reddit' , 'gmail' and more...)(More badge icons : https://simpleicons.org/)
        style : ('flat' , 'flat-square' , 'plastic' , 'for-the-badge' , 'social')(Default : 'for-the-badge')
        color : (Default : 'white')
        bg_color : (Default : 'black')
        text : (Default : None)
        link : (Default : None)
        """

        if icon:
            set_val(type='Badge', name=f"badge{self.badge_counter}",
                    val=f"{icon},{style},{color},{bg_color},{text},{link}")

            self.badge_counter += 1
            self.badge = f"Badge:{icon},{style},{color},{bg_color},{text},{link}"

            return f"Badge:{self.badge}"

        else:
            raise ValueError("ProfileCard Error : badge icon are required")


    def pack(self):
        """
        This function is use to pack the profile card
        """
        self.pack = Pack()


    def show(self):
        """
        This function is use to show the profile card
        """
        self.pack.show()


    def reset(self):
        """
        This function is use to reset the config file
        """
        self.pack.reset()


def reset_profilecard_config():
    """
    This function is use to reset the config file
    """
    rc()


def show_without_repacking(*, first : bool = False):
    """
    This function is use to show the profile card without repacking
    """
    show(first=first)
