import sqlite3
import bcrypt



ALLOWED_LANGUAGES_COLUMNS = {"language_id", "language_code", "language_eng_name"}
ALLOWED_LANGUAGE_LEVELS_COLUMNS = {"lang_level_id", "lang_level_name", "lang_level_descr"}
ALLOWED_CONTENT_LENGTHS_COLUMNS = {"content_len_id", "content_len_name", "content_len_text", "content_len_audio", "content_len_video"}
ALLOWED_BLOOM_DEPTHS_COLUMNS = {"bloom_depth_id", "bloom_depth_name", "bloom_depth_descr"}
ALLOWED_TARIFFS_COLUMNS = {"tariff_id", "tariff_name", "price_rub", "price_usd", "price_eur", "tariff_description"}
ALLOWED_USERS_COLUMNS = {"user_id", "user_tg_id", "user_bot_start_date", "tariff_id", "user_payment_date", "user_next_payment_date", "user_registration_date", "user_email", "user_password"}
ALLOWED_USER_SETTINGS_COLUMNS = {"user_id", "main_lang_id", "learn_lang_id", "learn_lang_level_id", "text_types", "interests", "text_tags"}
ALLOWED_TEXTS_COLUMNS = {"text_id", "text_content", "language_id", "lang_level_id", "content_len_id", "text_type", "text_tags"}
ALLOWED_USER_TEXTS_COLUMNS = {"user_id", "text_id", "text_send_date", "text_difficulty_rating", "text_interest_rating"}
ALLOWED_QUESTIONS_COLUMNS = {"question_id", "question_content", "text_id", "bloom_depth_id", "educational_result"}
ALLOWED_USER_QUESTIONS_COLUMNS = {"user_id", "question_id", "question_send_time", "user_response", "user_response_time", "response_correctness", "chat_gpt_response", "chat_gpt_response_time"}



# CRUD for Languages
def insert_language(language_code, language_eng_name=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        c.execute('INSERT INTO Languages (language_code, language_eng_name) VALUES (?,?)', 
                  (language_code, language_eng_name))

def select_language(language_id, column):
    if column in ALLOWED_LANGUAGES_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute('PRAGMA foreign_keys = ON')
            c.execute(f'SELECT {column} FROM Languages WHERE language_id = ?', (language_id,))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_LANGUAGES_COLUMNS}")

def update_language(language_id, column, new_value):
    if column in ALLOWED_LANGUAGES_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute('PRAGMA foreign_keys = ON')
            c.execute(f'UPDATE Languages SET {column} = ? WHERE language_id = ?', (new_value, language_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_LANGUAGES_COLUMNS}")

def delete_language(language_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        c.execute('DELETE FROM Languages WHERE language_id = ?', (language_id,))



# CRUD for LanguageLevels
def insert_lang_level(lang_level_name, lang_level_descr=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        c.execute('INSERT INTO LanguageLevels (lang_level_name, lang_level_descr) VALUES (?,?)', 
                  (lang_level_name, lang_level_descr))

def select_lang_level(lang_level_id, column):
    if column in ALLOWED_LANGUAGE_LEVELS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute('PRAGMA foreign_keys = ON')
            c.execute(f'SELECT {column} FROM LanguageLevels WHERE lang_level_id = ?', (lang_level_id,))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_LANGUAGE_LEVELS_COLUMNS}")

def update_lang_level(lang_level_id, column, new_value):
    if column in ALLOWED_LANGUAGE_LEVELS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute('PRAGMA foreign_keys = ON')
            c.execute(f'UPDATE LanguageLevels SET {column} = ? WHERE lang_level_id = ?', (new_value, lang_level_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_LANGUAGE_LEVELS_COLUMNS}")

def delete_lang_level(lang_level_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        c.execute('DELETE FROM LanguageLevels WHERE lang_level_id = ?', (lang_level_id,))



# CRUD for ContentLengths
def insert_content_len(content_len_name, content_len_text=None, content_len_audio=None, content_len_video=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO ContentLengths (content_len_name, content_len_text, content_len_audio, content_len_video) VALUES (?,?,?,?)', 
                  (content_len_name, content_len_text, content_len_audio, content_len_video))

def select_content_len(content_len_id, column):
    if column in ALLOWED_CONTENT_LENGTHS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'SELECT {column} FROM ContentLengths WHERE content_len_id = ?', (content_len_id,))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_CONTENT_LENGTHS_COLUMNS}")

def update_content_len(content_len_id, column, new_value):
    if column in ALLOWED_CONTENT_LENGTHS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'UPDATE ContentLengths SET {column} = ? WHERE content_len_id = ?', (new_value, content_len_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_CONTENT_LENGTHS_COLUMNS}")

def delete_content_len(content_len_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM ContentLengths WHERE content_len_id = ?', (content_len_id,))



# CRUD for BloomDepths
def insert_bloom_depth(bloom_depth_name, bloom_depth_descr=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO BloomDepths (bloom_depth_name, bloom_depth_descr) VALUES (?,?)', 
                  (bloom_depth_name, bloom_depth_descr))

def select_bloom_depth(bloom_depth_id, column):
    if column in ALLOWED_BLOOM_DEPTHS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'SELECT {column} FROM BloomDepths WHERE bloom_depth_id = ?', (bloom_depth_id,))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_BLOOM_DEPTHS_COLUMNS}")

def update_bloom_depth(bloom_depth_id, column, new_value):
    if column in ALLOWED_BLOOM_DEPTHS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'UPDATE BloomDepths SET {column} = ? WHERE bloom_depth_id = ?', (new_value, bloom_depth_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_BLOOM_DEPTHS_COLUMNS}")

def delete_bloom_depth(bloom_depth_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM BloomDepths WHERE bloom_depth_id = ?', (bloom_depth_id,))



# CRUD for Tariffs
def insert_tariff(tariff_name, price_rub, price_usd, price_eur, tariff_description=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO Tariffs (tariff_name, price_rub, price_usd, price_eur, tariff_description) VALUES (?,?,?,?,?)', 
                  (tariff_name, price_rub, price_usd, price_eur, tariff_description))

def select_tariff(tariff_id, column):
    if column in ALLOWED_TARIFFS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'SELECT {column} FROM Tariffs WHERE tariff_id = ?', (tariff_id,))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_TARIFFS_COLUMNS}")

def update_tariff(tariff_id, column, new_value):
    if column in ALLOWED_TARIFFS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'UPDATE Tariffs SET {column} = ? WHERE tariff_id = ?', (new_value, tariff_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_TARIFFS_COLUMNS}")

def delete_tariff(tariff_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM Tariffs WHERE tariff_id = ?', (tariff_id,))



# CRUD for Users
def insert_user(user_tg_id, user_bot_start_date, tariff_id=None, user_payment_date=None, user_next_payment_date=None, user_registration_date=None, user_email=None, user_password=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
        c.execute('INSERT INTO Users (user_tg_id, user_bot_start_date, tariff_id, user_payment_date, user_next_payment_date, user_registration_date, user_email, user_password) VALUES (?,?,?,?,?,?,?,?)', 
                  (user_tg_id, user_bot_start_date, tariff_id, user_payment_date, user_next_payment_date, user_registration_date, user_email, hashed_password))

def select_user(user_id, column):
    if column in ALLOWED_USERS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'SELECT {column} FROM Users WHERE user_id = ?', (user_id,))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_USERS_COLUMNS}")

def update_user(user_id, column, new_value):
    if column in ALLOWED_USERS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'UPDATE Users SET {column} = ? WHERE user_id = ?', (new_value, user_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_USERS_COLUMNS}")

def delete_user(user_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM Users WHERE user_id = ?', (user_id,))



# CRUD for UserSettings
def insert_user_settings(user_id, main_lang_id=None, learn_lang_id=None, learn_lang_level_id=None, text_types=None, interests=None, text_tags=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO UserSettings (user_id, main_lang_id, learn_lang_id, learn_lang_level_id, text_types, interests, text_tags) VALUES (?,?,?,?,?,?,?)', 
                  (user_id, main_lang_id, learn_lang_id, learn_lang_level_id, text_types, interests, text_tags))

def select_user_settings(user_id, column):
    if column in ALLOWED_USER_SETTINGS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'SELECT {column} FROM UserSettings WHERE user_id = ?', (user_id,))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_USER_SETTINGS_COLUMNS}")

def update_user_settings(user_id, column, new_value):
    if column in ALLOWED_USER_SETTINGS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'UPDATE UserSettings SET {column} = ? WHERE user_id = ?', (new_value, user_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_USER_SETTINGS_COLUMNS}")

def delete_user_settings(user_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM UserSettings WHERE user_id = ?', (user_id,))



# CRUD for Texts
def insert_text(text_content, language_id, lang_level_id, content_len_id=None, text_type=None, text_tags=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO Texts (text_content, language_id, lang_level_id, content_len_id, text_type, text_tags) VALUES (?,?,?,?,?,?)', 
                  (text_content, language_id, lang_level_id, content_len_id, text_type, text_tags))

def select_text(text_id, column):
    if column in ALLOWED_TEXTS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'SELECT {column} FROM Texts WHERE text_id = ?', (text_id,))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_TEXTS_COLUMNS}")

def update_text(text_id, column, new_value):
    if column in ALLOWED_TEXTS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'UPDATE Texts SET {column} = ? WHERE text_id = ?', (new_value, text_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_TEXTS_COLUMNS}")

def delete_text(text_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM Texts WHERE text_id = ?', (text_id,))



# CRUD for UserTexts
def insert_user_text(user_id, text_id, text_send_date=None, text_difficulty_rating=None, text_interest_rating=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO UserTexts (user_id, text_id, text_send_date, text_difficulty_rating, text_interest_rating) VALUES (?,?,?,?,?)', 
                  (user_id, text_id, text_send_date, text_difficulty_rating, text_interest_rating))

def select_user_text(user_id, text_id, column):
    if column in ALLOWED_USER_TEXTS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'SELECT {column} FROM UserTexts WHERE user_id = ? AND text_id = ?', (user_id, text_id))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_USER_TEXTS_COLUMNS}")

def update_user_text(user_id, text_id, column, new_value):
    if column in ALLOWED_USER_TEXTS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'UPDATE UserTexts SET {column} = ? WHERE user_id = ? AND text_id = ?', (new_value, user_id, text_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_USER_TEXTS_COLUMNS}")

def delete_user_text(user_id, text_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM UserTexts WHERE user_id = ? AND text_id = ?', (user_id, text_id))



# CRUD for Questions
def insert_question(question_content, text_id, bloom_depth_id=None, educational_result=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO Questions (question_content, text_id, bloom_depth_id, educational_result) VALUES (?,?,?,?)', 
                  (question_content, text_id, bloom_depth_id, educational_result))

def select_question(question_id, column):
    if column in ALLOWED_QUESTIONS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'SELECT {column} FROM Questions WHERE question_id = ?', (question_id,))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_QUESTIONS_COLUMNS}")

def update_question(question_id, column, new_value):
    if column in ALLOWED_QUESTIONS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'UPDATE Questions SET {column} = ? WHERE question_id = ?', (new_value, question_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_QUESTIONS_COLUMNS}")

def delete_question(question_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM Questions WHERE question_id = ?', (question_id,))



# CRUD for UserQuestions
def insert_user_question(user_id, question_id, question_ask_date=None, question_difficulty_rating=None, question_interest_rating=None):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('INSERT INTO UserQuestions (user_id, question_id, question_ask_date, question_difficulty_rating, question_interest_rating) VALUES (?,?,?,?,?)', 
                  (user_id, question_id, question_ask_date, question_difficulty_rating, question_interest_rating))

def select_user_question(user_id, question_id, column):
    if column in ALLOWED_USER_QUESTIONS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'SELECT {column} FROM UserQuestions WHERE user_id = ? AND question_id = ?', (user_id, question_id))
            result = c.fetchone()
        return result
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_USER_QUESTIONS_COLUMNS}")

def update_user_question(user_id, question_id, column, new_value):
    if column in ALLOWED_USER_QUESTIONS_COLUMNS:
        with sqlite3.connect('language_more_bot.db') as conn:
            c = conn.cursor()
            c.execute(f'UPDATE UserQuestions SET {column} = ? WHERE user_id = ? AND question_id = ?', (new_value, user_id, question_id))
    else:
        raise ValueError(f"Invalid column name. Allowed column names are: {ALLOWED_USER_QUESTIONS_COLUMNS}")

def delete_user_question(user_id, question_id):
    with sqlite3.connect('language_more_bot.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM UserQuestions WHERE user_id = ? AND question_id = ?', (user_id, question_id))
