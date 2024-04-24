[[English](README.md)|[中文](README_zh.md)]

# 個人資料卡模組

此模組提供了一種簡單的方式來創建簡單的個人名片，並可用連結（如 GitHub、YouTube 和 Reddit）來抓取個人資料導入。它包括風格、類型、主題等定制選項。還可用於個人作品進行綁定名片，於程式啟動自動跳出。

## 特點

- 使用預定義的風格自定義資料卡的樣式。
- 設定資料卡的類型，支持 GitHub、YouTube、Reddit 資料爬取或自定義等。
- 自定義主題，可選亮色或暗色。
- 添加徽章、背景圖片、個人頭像等。

![示例圖片](example.png)

```python
from profilecard import Pf

profile = Pf()

profile.set_style(style="2")

profile.set_type(type="custom")

profile.set_name("James &#128511;") #emoji -> &#128511

profile.set_pic("https://i.pinimg.com/564x/40/86/36/40863654e0c78c453f86539d12390405.jpg")

profile.set_theme(theme="light")

profile.set_site_title(title="Introduce")

profile.set_background_pic("https://www.hdwallpapers.in/download/white_wallpaper_5_4k_hd_white-1920x1080.jpg")

profile.add_badge(icon="discord", text="My discord", color="blue", bg_color="gray")
profile.add_badge(icon="github", text="My GitHub", color="white", link="https://github.com/jyst06", bg_color="gray")
profile.add_badge(icon="youtube", text="My Youtube", color="red", bg_color="gray")
profile.add_info("Some information<br>here &#128511;") #emoji -> &#128511

profile.pack()
profile.show()
profile.reset()
```

![示例圖片](example2.png)

```python
from profilecard import Pf

profile = Pf()

profile.set_type(type="github", link="https://github.com/jyst06")

profile.set_background_pic("https://wallpapercave.com/wp/wp13902559.png")

profile.add_badge(icon="discord", text="My discord", color="blue", style="flat")
profile.add_badge(icon="github", text="My GitHub", color="white", link="https://github.com/jyst06", style="flat")
profile.add_badge(icon="youtube", text="My Youtube", color="red", style="flat")

profile.add_info("Some information<br>here &#128511;")

profile.pack()
profile.show()
profile.reset()
```

![示例圖片](example3.png)

```python
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

## Pip 安裝

要安裝此模組，請使用以下 pip 命令：

```bash
pip install profilecard
```

## 基本用法

以下是如何使用本模組中的 `Pf` 類：

```python
from profilecard import *

# 創建個人資料卡實例（默認為 False）
profile = Pf(first=False)

# 更改頁面風格（默認為風格 1）
profile.set_style("2")  # 有三種風格可選：1、2、3

# 設定個人資料卡類型（必須）
profile.set_type(type='github', link='https://github.com/yourusername')
profile.set_theme('light')  # 選項：亮色、暗色（默認為暗色）

# 添加徽章，更多圖標可在 https://simpleicons.org/ 查看
profile.add_badge(icon="github", text="GitHub", link="https://github.com/yourusername") 
profile.add_badge(icon="facebook", text="facebook", color="black", bg_color="white")

# 徽章參數：
# icon（必需）：可選 'github'、'youtube'、'facebook'、'twitter'、'instagram'、'reddit'、'gmail' 等等...
# style：徽章風格，默認為 'for-the-badge'
# color：文字顏色，默認為 'white'
# bg_color：背景顏色，默認為 'black'
# text：徽章上的文字，默認為 None
# link：徽章關聯的鏈接，默認為 None

# 添加一些信息
profile.add_info("OwO<br>Hello") #<br>當作換行符使用 , 添加emoji可以透過搜尋"HTML emoji code"來查詢對應代碼

# 添加一些聯繫信息
profile.add_contect("我的郵件：abc@gmail.com")

# 設置背景圖片
profile.set_background_pic(r"https://storage.pixteller.com/designs/designs-images/2019-03-27/05/simple-background-backgrounds-passion-simple-1-5c9b95c3a34f9.png")

# 更改網站標題
profile.set_site_title("我的網站")

# 更改資料卡標題
profile.set_card_title("帥哥")

# 打包所有
profile.pack()

# 顯示網站
profile.show()
```

## API 參考

`Pf` 類中提供以下函數：

### `help(profilecard)` 在IDE中取得使用方法

---

### `set_style(style: str)`
設定資料卡的風格。
- **參數**：
  - `style`：一個代表風格的字符串（'1', '2', '3'）。默認為 '1'。

---

### `set_type(type: str, link: str)`
設定資料卡的類型和可選的個

人頁面鏈接。
- **參數**：
  - `type`：一個代表類型的字符串（'github', 'youtube', 'reddit', 'custom'）。
  - `link`：一個代表鏈接的字符串。

---

### `set_theme(theme: str)`
設定卡片的主題。
- **參數**：
  - `theme`：一個代表主題的字符串（"light", "dark"）。

---

### `add_badge(icon: str, style: str, color: str, bg_color: str, text: str, link: str)`
添加一個徽章。
- **參數**：
  - `icon`：必需。從各種圖標中選擇，如 'github', 'youtube' 等。
  - `style`：徽章風格，默認為 'for-the-badge'。
  - `color`：文字顏色，默認為 'white'。
  - `bg_color`：徽章背景色，默認為 'black'。
  - `text`：顯示在徽章上的文字，默認為 None。
  - `link`：與徽章關聯的鏈接，默認為 None。

---

### 還包括其他方法如 `set_pic`, `set_name`, `set_background_pic`, `add_info`, `add_contect`, `set_site_title`, `set_card_title`, `pack`, `show`, 和 `reset`。

---

### init中的其他方法 `reset_profilecard_config()`, `show_without_repacking()`

---

## 貢獻

歡迎貢獻！請分支本倉庫並打開一個帶有您更改的拉取請求。

## 許可證

此項目授予 MIT 許可證 - 詳見 [LICENSE](LICENSE.md) 文件。
