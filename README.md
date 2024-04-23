
# Personal Profile Card Module

This module provides a simple way to create and manage personal profile cards for various platforms like GitHub, YouTube, and Reddit. It includes customization options such as style, type, theme, and more.
You can also use for advertising like your channel ... on your project

## Features

- Customize the style of the profile card with predefined styles.
- Set the type of profile card to platforms like GitHub, YouTube, Reddit, or custom.
- Customize the theme to be either light or dark.
- Add badges, background pictures, profile pictures, and more.

![Example image](example.png)

## Pip Installation

To install this module, you can simply use the "pip" command:

``` bash
pip install profilecard
```

## Basic usage

Here's how you can use the `Pf` class from this module:

``` python
from profilecard import *


# Create a profile card instance (Default is False)
profile = Pf(first=False) # 'first' argument means it only run on first time or not


# Change page style (Default is style 1)
profile.set_style("2") # Three style 1 - 3 


# Set profile type (Required)
profile.set_type(type='github', link='https://github.com/yourusername') # It will automatically crawling profile picture, name and id to the profile page
profile.set_theme('light') #light, dark (Default is dark)


# Add some badges , More icons on https://simpleicons.org/
profile.add_badge(icon="github", text="GitHub", link="https://github.com/yourusername") 
profile.add_badge(icon="facebook", text="facebook", color="black", bg_color="white")
#Badge arguments : 
#icon(Required) : ('github' , 'youtube' , 'facebook' , 'twitter' , 'instagram' , 'reddit' , 'gmail' and more...)(More badge icons : https://simpleicons.org/)
#style : ('flat' , 'flat-square' , 'plastic' , 'for-the-badge' , 'social')(Default : 'for-the-badge')
#color : (Default : 'white')
#bg_color : (Default : 'black')
#text : (Default : None)
#link : (Default : None)


# Add some information
profile.add_info("OwO")


# Add some contect information
profile.add_contect("My mail : abc@gmail.com")


# Set background image
profile.set_background_pic(r"https://storage.pixteller.com/designs/designs-images/2019-03-27/05/simple-background-backgrounds-passion-simple-1-5c9b95c3a34f9.png")


# Change the site title
profile.set_site_title("my site")


# Change profile title
profile.set_card_title("Handsome guy")


# Pack all
profile.pack()


# Display site
profile.show()
```
## API Reference

``` python
from profilecard import Pf
```

#### `set_style(style: str)`

Sets the style of the profile card.

**Parameters:**
- `style`: A string representing the style ('1', '2', '3'). Default is '1'.
---

#### `set_type(*, type: str, link: str)`

Sets the type of profile card and optionally the profile page link.

**Parameters:**
- `type`: A string representing the type ('github', 'youtube', 'reddit', 'custom').
- `link`: A string representing the link to the profile page.
---

#### `set_pic(link: str)`

Sets the profile picture and optionally the profile picture link (Only for custom type).

**Parameters:**
- `link`: A string representing the link to the profile picture.
---

#### `set_name(name: str)`

Sets the profile name (Only for custom type).

**Parameters:**
- `name`: A string representing the profile name.
---

#### `set_site_title(title: str)`

Sets the site title.

**Parameters:**
- `title`: A string representing the site title.
---

#### `set_card_title(title: str)`

Sets the card title.

**Parameters:**
- `title`: A string representing the card title.
---
#### `set_theme(theme: str)`

Sets the theme of the card.

**Parameters:**
- `theme`: A string representing the theme ("light", "dark").
---
#### `set_background_pic(link: str)`

Sets the background of the site.

**Parameters:**
- `link`: A string representing the link to the background picture.
---
#### `add_id(id: str)`

Add the id part (Only for custom type).

**Parameters:**
- `id`: A string representing the id.
---
#### `add_info(info: str)`

Add the information part.

**Parameters:**
- `info`: A string representing the info text.
---
#### `add_contect(contect: str)`

Add the contect information part.

**Parameters:**
- `contect`: A string representing the contect text.
---
#### `add_badge(*, icon: str, style: str, color: str, bg_color: str, text: st, link: str)`

Add the badge.

**Parameters:**
- `icon(Required)` : ('github' , 'youtube' , 'facebook' , 'twitter' , 'instagram' , 'reddit' , 'gmail' and more...)(More badge icons : https://simpleicons.org/)
- `style` : ('flat' , 'flat-square' , 'plastic' , 'for-the-badge' , 'social')(Default : 'for-the-badge')
- `color` : (Default : 'white')
- `bg_color` : (Default : 'black')
- `text` : (Default : None)
- `link` : (Default : None)
---

## Functions
#### `pack()`

Pack the objects.

---

#### `show()`

Display on browser.

---

#### `reset()`

Resets config.

---

## Other Functions
``` python
from profilecard import show_without_repacking
```
#### `show_without_repacking()`

Display on browser without packing again.

---

![Example image](example2.png)
``` python
from profilecard import Pf

root = Pf(first=False)
root.set_style("1")
root.set_type(type="github", link="https://github.com/jyst06")
root.add_badge(icon="github", text="GitHub", link="https://github.com/jyst06", bg_color="white", color="black")

root.set_theme("light")
root.add_info("Hello")
root.set_card_title("About Me")
root.set_site_title("my site")
root.add_contect("Nope :(")
root.set_background_pic(r"https://i.pinimg.com/564x/f6/0e/23/f60e2340570829c9f4dba61554329dac.jpg")
root.pack()
root.show()
root.reset()
```

---

![Example image](example3.png)
``` python
from profilecard import Pf

root = Pf(first=False)
root.set_style("2")
root.set_type(type="custom")
root.add_id("jyst06")
root.set_name("James")
root.set_pic("https://i.pinimg.com/564x/59/dc/8d/59dc8d6797b835e746dd99a2df7dcedd.jpg")

root.add_badge(icon="github", text="GitHub", link="https://github.com/jyst06", bg_color="white", color="black")

root.set_theme("light")
root.add_info("Hello")
root.set_card_title("About Me")
root.set_site_title("my site")
root.add_contect("Nope :(")
root.set_background_pic(r"https://images6.alphacoders.com/133/1330710.png")
root.pack()
root.show()
root.reset()
```

---
## Contributing

Contributions are welcome! Please fork the repository and open a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

