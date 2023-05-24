import sqlite3



def setup_database():
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')


        try:
            c.execute('''
                CREATE TABLE Languages (
                    language_id INTEGER PRIMARY KEY,
                    language_code TEXT NOT NULL,
                    language_eng_name TEXT
                )
            ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        try:
            c.execute('''
                CREATE TABLE LanguageLevels (
                    lang_level_id INTEGER PRIMARY KEY,
                    lang_level_name TEXT NOT NULL,
                    lang_level_descr TEXT
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        try:
            c.execute('''
                CREATE TABLE ContentLengths (
                    content_len_id INTEGER PRIMARY KEY,
                    content_len_name TEXT NOT NULL,
                    content_len_text TEXT, 
                    content_len_audio TEXT,
                    content_len_video TEXT
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        try:
            c.execute('''
                CREATE TABLE BloomDepths (
                    bloom_depth_id INTEGER PRIMARY KEY,
                    bloom_depth_name TEXT NOT NULL,
                    bloom_depth_descr TEXT
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        try:
            c.execute('''
                CREATE TABLE Tariffs (
                    tariff_id INTEGER PRIMARY KEY,
                    tariff_name TEXT NOT NULL,
                    price_rub FLOAT NOT NULL,
                    price_usd FLOAT NOT NULL,
                    price_eur FLOAT NOT NULL,
                    tariff_description TEXT
                )
            ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        try:
            c.execute('''
                CREATE TABLE Users (
                    user_id INTEGER PRIMARY KEY,
                    user_tg_id TEXT NOT NULL,
                    user_bot_start_date TEXT NOT NULL,
                    tariff_id INTEGER,
                    user_payment_date TEXT,
                    user_next_payment_date TEXT,
                    user_registration_date TEXT,
                    user_email TEXT,
                    user_password BLOB,
                    FOREIGN KEY(tariff_id) REFERENCES Tariffs(tariff_id)
                )
            ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        try:
            c.execute('''
                CREATE TABLE UserSettings (
                    user_id INTEGER PRIMARY KEY,
                    main_lang_id INTEGER,
                    learn_lang_id INTEGER,
                    learn_lang_level_id INTEGER,
                    text_types TEXT,
                    interests TEXT,
                    text_tags TEXT,
                    FOREIGN KEY(user_id) REFERENCES Users(user_id),
                    FOREIGN KEY(main_lang_id) REFERENCES Languages(language_id),
                    FOREIGN KEY(learn_lang_id) REFERENCES Languages(language_id),
                    FOREIGN KEY(learn_lang_level_id) REFERENCES Languages(lang_level_id)
                )
            ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        try:
            c.execute('''
                CREATE TABLE Texts (
                    text_id INTEGER PRIMARY KEY,
                    text_content TEXT NOT NULL,
                    language_id INTEGER NOT NULL,
                    lang_level_id INTEGER NOT NULL,
                    content_len_id TEXT,
                    text_type TEXT,
                    text_tags TEXT,
                    FOREIGN KEY(language_id) REFERENCES Languages(language_id),
                    FOREIGN KEY(lang_level_id) REFERENCES LanguageLevels(lang_level_id),
                    FOREIGN KEY(content_len_id) REFERENCES ContentLengths(content_len_id)
                )
            ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        try:
            c.execute('''
                CREATE TABLE UserTexts (
                    user_id INTEGER,
                    text_id INTEGER,
                    text_send_date TEXT,
                    text_difficulty_rating INTEGER,
                    text_interest_rating INTEGER,
                    FOREIGN KEY(user_id) REFERENCES Users(user_id),
                    FOREIGN KEY(text_id) REFERENCES Texts(text_id)
                    PRIMARY KEY(user_id, text_id)
                )
            ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        try:
            c.execute('''
                CREATE TABLE Questions (
                    question_id INTEGER PRIMARY KEY,
                    question_content TEXT NOT NULL,
                    text_id INTEGER NOT NULL,
                    bloom_depth_id INTEGER,
                    educational_result TEXT,
                    FOREIGN KEY(text_id) REFERENCES Texts(text_id),
                    FOREIGN KEY(bloom_depth_id) REFERENCES BloomDepth(bloom_depth_id)
                )
            ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        try:
            c.execute('''
                CREATE TABLE UserQuestions (
                    user_id INTEGER,
                    question_id INTEGER,
                    question_send_time TEXT,
                    user_response TEXT,
                    user_response_time TEXT,
                    response_correctness TEXT,
                    chat_gpt_response TEXT,
                    chat_gpt_response_time TEXT,
                    FOREIGN KEY(user_id) REFERENCES Users(user_id),
                    FOREIGN KEY(question_id) REFERENCES Questions(question_id)
                    PRIMARY KEY(user_id, question_id)
                )
            ''')
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")


        conn.commit()



if __name__ == "__main__":
    setup_database()
