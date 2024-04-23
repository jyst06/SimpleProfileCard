# 個人資料卡模組

此模組提供一種簡單的方法來創建和管理適用於 GitHub、YouTube 和 Reddit 等平台的個人資料卡。它包括樣式、類型、主題等自定義選項。您也可以用它來推廣您的頻道等。

## 功能

- 使用預定義的樣式自定義個人資料卡的樣式。
- 設置個人資料卡的類型，如 GitHub、YouTube、Reddit 或自定義。
- 自定義主題為亮色或暗色。
- 添加徽章、背景圖片、個人資料圖片等。

![範例圖](example.png)

## Pip 安裝

要安裝此模組，您可以簡單地使用 "pip" 命令：

``` bash
pip install profilecard
```

## 基本用法

以下是如何使用此模組中的 `Pf` 類：

``` python
from profilecard import *


# 創建一個個人資料卡實例（默認為 False）
profile = Pf(first=False) # 'first' 參數表示是否只在第一次運行


# 更改頁面樣式（默認為樣式 1）
profile.set_style("2") # 有三種樣式 1 - 3


# 設定個人資料卡的類型（必填）
profile.set_type(type='github', link='https://github.com/yourusername') # 它會自動抓取個人資料圖片、姓名和 id 到個人頁面
profile.set_theme('light') #亮色, 暗色（默認為暗色）


# 添加一些徽章，更多圖標在 https://simpleicons.org/
profile.add_badge(icon="github", text="GitHub", link="https://github.com/yourusername")
profile.add_badge(icon="facebook", text="facebook", color="black", bg_color="white")
# 徽章參數：
# icon(必填) : ('github' , 'youtube' , 'facebook' , 'twitter' , 'instagram' , 'reddit' , 'gmail' 等更多...)(更多徽章圖標：https://simpleicons.org/)
# style : ('flat' , 'flat-square' , 'plastic' , 'for-the-badge' , 'social')(默認：'for-the-badge')
# color : (默認：'white')
# bg_color : (默認：'black')
# text : (默認：無)
# link : (默認：無)


# 添加一些信息
profile.add_info("OwO")


# 添加一些聯繫信息
profile.add_contect("我的郵箱：abc@gmail.com")


# 設置背景圖片
profile.set_background_pic(r"https://storage.pixteller.com/designs/designs-images/2019-03-27/05/simple-background-backgrounds-passion-simple-1-5c9b95c3a34f9.png")


# 更改網站標題
profile.set_site_title("我的網站")


# 更改個人資料卡標題
profile.set_card_title("帥哥")


# 打包所有設定
profile.pack()


# 顯示網頁
profile.show()
```

## API 參考

以下是此模組 API 的一些基本方法和參數說明：

### `set_style(style: str)`

設置個人資料卡的樣式。

**參數：**
- `style`: 表示樣式的字符串（'1', '2', '3'）。默認為 '1'。
---

### `set_type(*, type: str, link: str)`

設置個人資料卡的類型

以及選填的個人頁面鏈接。

**參數：**
- `type`: 表示類型的字符串（'github', 'youtube', 'reddit', 'custom'）。
- `link`: 表示個人頁面鏈接的字符串。
---

### `set_pic(link: str)`

設置個人資料圖片及選填的圖片鏈接（僅限自定義類型）。

**參數：**
- `link`: 表示個人資料圖片鏈接的字符串。
---

### `set_name(name: str)`

設置個人名稱（僅限自定義類型）。

**參數：**
- `name`: 表示個人名稱的字符串。
---

### `set_site_title(title: str)`

設置網站標題。

**參數：**
- `title`: 表示網站標題的字符串。
---

### `set_card_title(title: str)`

設置個人資料卡標題。

**參數：**
- `title`: 表示個人資料卡標題的字符串。
---

### `set_theme(theme: str)`

設置個人資料卡的主題。

**參數：**
- `theme`: 表示主題的字符串（"light", "dark"）。
---

### `set_background_pic(link: str)`

設置網站背景圖片。

**參數：**
- `link`: 表示背景圖片鏈接的字符串。
---

### `add_id(id: str)`

添加 ID 部分（僅限自定義類型）。

**參數：**
- `id`: 表示 ID 的字符串。
---

### `add_info(info: str)`

添加信息部分。

**參數：**
- `info`: 表示信息文本的字符串。
---

### `add_contect(contect: str)`

添加聯繫信息部分。

**參數：**
- `contect`: 表示聯繫信息的字符串。
---

### `add_badge(*, icon: str, style: str, color: str, bg_color: str, text: str, link: str)`

添加徽章。

**參數：**
- `icon(必填)` : ('github' , 'youtube' , 'facebook' , 'twitter' , 'instagram' , 'reddit' , 'gmail' 等更多...)(更多徽章圖標：https://simpleicons.org/)
- `style` : ('flat' , 'flat-square' , 'plastic' , 'for-the-badge' , 'social')(默認：'for-the-badge')
- `color` : (默認：'white')
- `bg_color` : (默認：'black')
- `text` : (默認：無)
- `link` : (默認：無)
---

## 函數
#### `pack()`

打包物件。

---

#### `show()`

在瀏覽器中顯示。

---

#### `reset()`

重置配置。

---

## 其他函數
``` python
from profilecard import show_without_repacking
```
#### `show_without_repacking()`

直接在瀏覽器中顯示，無需重新打包。

---

![範例圖](example2.png)
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

![範例圖](example3.png)
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
## 貢獻

歡迎貢獻！請 fork 倉庫並開啟一個包含您更改的 pull 請求。

## 許可證

此項目採用 MIT 許可證授權 - 詳情請見 [LICENSE.md](LICENSE) 文件。

