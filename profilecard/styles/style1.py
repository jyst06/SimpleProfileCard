class Style1:
    def __init__(self):
        self.css = '''
                <!DOCTYPE html>
                <head>
                    <title>{site_title}</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            margin: 0;
                            background-color: {t0};
                        }}
                        .profile-card {{
                            width: 300px;
                            background-color: {t1};
                            border-radius: 10px;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
                            color: {t2};
                            padding: 20px;
                            text-align: center;
                        }}
                        .profile-image {{
                            width: 100px;
                            height: 100px;
                            border-radius: 50%;
                            margin-bottom: 20px;
                            margin-left: auto;
                            margin-right: auto;
                            background-image: url('{profile_pic_link}');
                            background-position: center center;
                            background-size: cover;
                            background-repeat: no-repeat;
                        }}
                        .profile-card h2 {{
                            margin: 0;
                            padding: 0;
                            font-size: 20px;
                            color: {t3};
                        }}
                        .profile-card .id {{
                            color: {t4};
                        }}
                        .profile-card .line {{
                            margin-top: 15px;
                            border-top: 1px solid {t5};
                            padding-top: 10px;
                        }}
                        .profile-card img.badge {{
                            border-radius: 0;
                            width: auto;
                            height: auto;
                        }}
                        .bg{{
                            background-image: url('{background_pic_link}');
                            background-position: center center;
                            background-size: contain;
                            background-repeat: no-repeat;
                        }}
                    </style>
                    '''

        self.profile = '''
                </head>
                <body class="{bg}">
                    <div class="profile-card">
                        <h1>{card_title}</h1>
                        <div class="profile-image"></div>
                        <h2>{profile_name}</h2>
        '''

        self.part_id = '''
                <p class="id">{profile_id}</p>
        '''

        self.badge = '''
                <a{badge_link}><img class="badge" alt="Static Badge" src="https://img.shields.io/badge/{badge_text}-_?style={badge_style}&logo={badge_icon}&logoColor={badge_color}&color={badge_bg_color}"></a>
                '''

        self.info = '''
                <div class="line">
                    <h2>Info</h2><br>
                    <span style="display: block;">{info}</span><br>
                </div>
        '''

        self.contect = '''
                <div class="line">
                    <h2>Contect Me</h2>
                    <p>{contect_text}</p>
                </div>
        '''

        self.end = '''
                    </div>
                </body>
                </html>
        '''

    def __call__(self):
        return self.css, self.profile, self.part_id, self.badge, self.info, self.contect, self.end
