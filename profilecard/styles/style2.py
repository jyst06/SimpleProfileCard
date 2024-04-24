class Style2:
    def __init__(self):
        self.css = '''
                <!DOCTYPE html>
                <head>
                    <title>{site_title}</title>
                    <style>
                        body {{
                            font-family: 'Helvetica Neue', sans-serif;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            margin: 0;
                            background-image: url('{background_pic_link}');
                            background-position: center center;
                            background-size: cover;
                            background-repeat: no-repeat;
                            background-color: {t0};
                        }}
                        .profile-card {{
                            display: flex;
                            width: 600px;
                            background-color: {t1};
                            border-radius: 15px;
                            box-shadow: 0 5px 20px rgba(0,0,0,0.25);
                            color: {t2};
                            overflow: hidden;
                        }}
                        .profile-image {{
                            background-image: url('{profile_pic_link}');
                            background-position: center center;
                            background-size: cover;
                            background-repeat: no-repeat;
                            width: 40%; /* Adjusted for aspect ratio */
                            height: auto;
                            min-height: 100%; /* Ensure it covers vertically */
                            box-sizing: border-box;
                            display: flex;
                            align-items: center; /* Center content vertically */
                            justify-content: center; /* Center content horizontally */
                            border-right: 2px solid {t5}; /* Stylish right border */
                        }}
                        .profile-info {{
                            width: 60%;
                            padding: 20px;
                            text-align: left;
                        }}
                        .profile-info h1, .profile-info h2 {{
                            margin-top: 0;
                        }}
                        .profile-info h1 {{
                            color: {t3};
                            padding-bottom: 10px;
                            border-bottom: 2px solid {t5};
                        }}
                        .profile-info .id {{
                            color: {t4};
                        }}
                        .profile-info .line {{
                            margin-top: 10px;
                            border-top: 2px solid {t5};
                            padding-top: 10px;
                        }}
                        .profile-info img.badge {{
                            width: auto;
                            height: auto;
                        }}
                    </style>
                    '''

        self.profile = '''
                </head>
                <body class="bg">
                    <div class="profile-card">
                        <div class="profile-image"></div>
                        <div class="profile-info">
                            <h1>{card_title}</h1>
                            <h2>{profile_name}</h2>
        '''

        self.part_id = '''
                            <p class="id">{profile_id}</p>
        '''

        self.badge = '''
                            <a{badge_link}><img class="badge" alt="Badge" src="https://img.shields.io/badge/{badge_text}-_?style={badge_style}&logo={badge_icon}&logoColor={badge_color}&color={badge_bg_color}"></a>
        '''

        self.info = '''
                            <div class="line">
                                <h2>Info</h2>
                                <span style="display: block;">{info}</span>
                            </div>
        '''

        self.contect = '''
                            <div class="line">
                                <h2>Contact Me</h2>
                                <p>{contect_text}</p>
                            </div>
        '''

        self.end = '''
                        </div>
                    </div>
                </body>
                </html>
        '''

    def __call__(self):
        return self.css, self.profile, self.part_id, self.badge, self.info, self.contect, self.end
