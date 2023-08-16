create_history = """CREATE TABLE IF NOT EXISTS media (domain TEXT,
                                               url_path TEXT,
                                               album_path TEXT,
                                               referer TEXT,
                                               original_filename TEXT,
                                               completed INTEGER NOT NULL,
                                               PRIMARY KEY (url_path, original_filename)
                                               );"""

create_temp = """CREATE TABLE IF NOT EXISTS temp (downloaded_filename TEXT);"""

create_cache = """CREATE TABLE IF NOT EXISTS cache (url_path TEXT, post_data BLOB, PRIMARY KEY (url_path));"""
