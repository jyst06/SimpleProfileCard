from ..styles import Style1, Style2,  Style3
from .valmanager import get_val, get_val_dict, set_val, reset_config
import os
from bs4 import BeautifulSoup
import requests
import re
import json
import webbrowser


#combine html
class Parser:
    def __init__(self):
        self.dark = ['#23272a', '#2C2F33', 'white', 'white', '#99aab5', '#99aab5']
        self.light = ['#f0f0f0', '#ffffff', '#333333', '#333', '#666', '#ccc']


    def parseAll(self, parameters : dict, optionals : dict, badges : dict) -> str:
        #parse theme
        self.style = optionals['style']

        if self.style == '1':
            _style = Style1()
            css, profile, id, badge, info, contect, end = _style()

        elif self.style == '2':
            _style = Style2()
            css, profile, id, badge, info, contect, end = _style()

        elif self.style == '3':
            _style = Style3()
            css, profile, id, badge, info, contect, end = _style()

        else:
            raise ValueError(f"Theme:{self.style} is not supported")

        #parse type
        self.type_parse(parameters['type'], parameters['profile_page_link'], parameters['profile_pic_link'], parameters['profile_name'], optionals['profile_id'])

        #parse options
        self.background_pic = optionals['background_pic_link']
        self.theme = optionals['theme']
        self.site_title = optionals['site_title']
        self.card_title = optionals['card_title']
        self.info = optionals['info']
        self.contect = optionals['contect']

        #parse badges
        if badges['badge0'] == "":
            self.badges = None

        else:
            self.badges = badges

        return self.combine(css, profile, id, badge, info, contect, end)

    def type_parse(self, type, link, profile_pic_link, profile_name, profile_id) -> None:
        if type == 'github':
            self.github_parse(link)

        elif type == 'youtube':
            self.youtube_parse(link)

        elif type == 'reddit':
            self.reddit_parse(link)

        elif type == 'leetcode':
            self.leetcode_parse(link)

        elif type == 'custom':
            self.custom_parse(profile_pic_link, profile_name, profile_id)

        else:
            raise ValueError(f'Type:{type} is not supported')


    def github_parse(self, link) -> None:
        soup = BeautifulSoup(requests.get(link).text, 'html.parser')
        self.profile_pic = soup.find("img").get("src")
        self.profile_name = soup.find("span", itemprop="name").text.strip()
        self.profile_id = soup.find("span", itemprop="additionalName").text.strip()

        if self.profile_pic is None or self.profile_name is None:
            raise ValueError(f'profilecard Error : Invalid link')


    def youtube_parse(self, link) -> None:
        soup = BeautifulSoup(requests.get(link).content, "html.parser")
        data = re.search(r"var ytInitialData = ({.*?});</script>", str(soup)).group(1)
        json_data = json.loads(data)
        self.profile_pic = json_data["header"]["c4TabbedHeaderRenderer"]["avatar"]["thumbnails"][0]["url"]
        self.profile_name = json_data["header"]["c4TabbedHeaderRenderer"]["title"]
        self.profile_id = None


    def reddit_parse(self, link) -> None:
        soup = BeautifulSoup(requests.get(link).text, 'html.parser')
        self.profile_pic = soup.find("img").get("src")
        self.profile_name = soup.find("h1").text.strip()
        self.profile_id = soup.find("p").text.strip()


    def leetcode_parse(self, link) -> None:
        temp = link.split('/')
        if temp[-1]:
            account = temp[-1]
        else:
            account = temp[-2]

        original_string = '{ matchedUser(username: "account") { profile { realName userAvatar } } }'
        query = original_string.replace('account', account)
        data = {
            "query": query,
        }
        res = requests.post(url='https://leetcode.com/graphql/', json=data)
        profile = res.json()["data"]['matchedUser']['profile']
        self.profile_pic = profile['userAvatar']
        self.profile_name = profile['realName']
        self.profile_id = None


    def custom_parse(self, profile_pic_link, profile_name, profile_id) -> None:
        self.profile_pic = profile_pic_link
        self.profile_name = profile_name
        if profile_id:
            self.profile_id = profile_id

        else:
            self.profile_id = None


    def combine(self, css, profile, id, badge, info, contect, end) -> str:
        # format css
        if self.theme == 'dark':
            css_area = css.format(
                site_title=self.site_title, t0=self.dark[0], t1=self.dark[1],
                t2=self.dark[2], t3=self.dark[3], t4=self.dark[4], t5=self.dark[5],
                background_pic_link=self.background_pic, profile_pic_link=self.profile_pic)

        elif self.theme == 'light':
            css_area = css.format(
                site_title=self.site_title, t0=self.light[0], t1=self.light[1],
                t2=self.light[2], t3=self.light[3], t4=self.light[4], t5=self.light[5],
                background_pic_link=self.background_pic, profile_pic_link=self.profile_pic)

        else:
            raise ValueError(f'Theme:{self.theme} is not supported')

        # format profile
        if self.profile_name == "":
            raise ValueError(f'ProfileCard Error : profile name is required')

        if self.background_pic:
            profile_area = profile.format(bg="bg", profile_name=self.profile_name, card_title=self.card_title)

        else:
            profile_area = profile.format(bg="", profile_name=self.profile_name, card_title=self.card_title)

        #format id
        if self.profile_id:
            id_area = id.format(profile_id=self.profile_id)
        else:
            id_area = "<br>"

        #format badge
        if self.badges is None:
            badge_area = ""
        else:
            badge_area = ""
            for key, value in self.badges.items():
                value = value.split(',')
                if value[5] == "":
                    badge_area += badge.format(badge_icon=value[0], badge_style=value[1], badge_color=value[2],
                                               badge_bg_color=value[3], badge_text=value[4],
                                               badge_link="")
                else:
                    badge_area += badge.format(badge_icon=value[0], badge_style=value[1], badge_color=value[2],
                                               badge_bg_color=value[3], badge_text=value[4],
                                               badge_link=f' href="{value[5]}" target = "_blank"')

        #format info
        if self.info:
            info_area = info.format(info=self.info)
        else:
            info_area = ""

        #format contect
        if self.contect:
            contect_area = contect.format(contect_text=self.contect)
        else:
            contect_area = ""

        #end
        end_area = end

        #combine all
        return "\n".join([css_area, profile_area, id_area, badge_area, info_area, contect_area, end_area])


#pack objects into html
class Pack(Parser):
    def __init__(self):
        self._parameters = dict(get_val_dict("Parameters"))
        self._optionals = dict(get_val_dict("Optional"))
        self._badges = dict(get_val_dict("Badge"))

        super().__init__()
        self.text = self.parseAll(self._parameters, self._optionals,  self._badges)

        if self.text:
            self.save()
        else:
            raise ValueError("profilecard Error : Pack failed")


    def save(self):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_name = "profile.html"
        self.file_name = os.path.join(current_folder, file_name)

        with open(self.file_name, 'w') as f:
            f.write(self.text)


    def show(self):
        run = get_val(type="Run", name="first")
        if run == "false":
            webbrowser.open(self.file_name)
        elif run == "true":
            webbrowser.open(self.file_name)
            set_val(type="Run", name="first", val="stop")
        elif run == "stop":
            pass


    def reset(self):
        reset_config()


def show(*, first: bool = False):
    """
    This function is use to show profile card without packing
    """
    if get_val(type="Run", name="first") == "stop" and first == True:
        pass
    else:
        set_val(type="Run", name="first", val=str(first).lower())

    current_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = "profile.html"
    file_name = os.path.join(current_folder, file_name)

    if os.path.exists(file_name) is not True:
        raise ValueError(f"profilecard Error : You need to pack first")

    run = get_val(type="Run", name="first")
    if run == "false":
        webbrowser.open(file_name)
    elif run == "true":
        webbrowser.open(file_name)
        set_val(type="Run", name="first", val="stop")
    elif run == "stop":
        pass


