import psycopg2
from threading import Lock
from helper import Helper
import requests
import re

helper = Helper()
config = helper.get_config()

class DbHandler:
    def __init__(self, dbname=config['DATABASE']['DB_NAME'], user=config['DATABASE']['USER'], password=config['DATABASE']['PASSWORD'], host=config['DATABASE']['HOST'], port=config['DATABASE']['PORT']):
        self.conn_details = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port,
        }
        self.conn = psycopg2.connect(**self.conn_details)
        self.conn.autocommit = True

    def get_html_content(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT html_content FROM crawldb.page WHERE id=%s", (id,))
        result = cur.fetchone()
        if result is None: return result
        else: return result[0]

    def get_url(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT url FROM crawldb.page WHERE id=%s", (id,))
        result = cur.fetchone()
        if result is None: return result
        else: return result[0]
    
    def update_cleaned_content(self, page_id, cleaned_content):
        """Update the database with cleaned content"""
        cur = self.conn.cursor()
        cur.execute("""
            UPDATE crawldb.page 
            SET cleaned_content = %s 
            WHERE id = %s
            """, (cleaned_content, page_id))
        self.conn.commit()
        return cur.rowcount

    def get_cleaned_content(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT cleaned_content FROM crawldb.page WHERE id=%s", (id,))
        result = cur.fetchone()
        if result is None: return result
        else: return result[0]

    def clear_page_segment(self):
        cur = self.conn.cursor()
        cur.execute("TRUNCATE TABLE crawldb.page_segment RESTART IDENTITY CASCADE;")

    def insert_page_segment(self, page_id, page_segment, segment_type, embedding):
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO crawldb.page_segment 
            (page_id, page_segment, segment_type, embedding) 
            VALUES (%s, %s, %s, %s)
            """, 
            (page_id, page_segment, segment_type, embedding))
        self.conn.commit()
        return cur.rowcount