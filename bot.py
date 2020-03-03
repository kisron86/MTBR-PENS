import sys
import time
import random
import datetime
import telepot
import os
import random
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='trash',
                                         user='phpmyadmin',
                                         password='1234')

    sql_select_Query = "select * from data_sensor"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

def handle(msg):
    global command
    chat_id = msg['chat']['id']
    command = msg['text']   
    if command == '/start' or command == '/Kembali' or command == '/Start':
        bot.sendMessage(chat_id, 'Halo Selamat datang Ada yang bisa dibantu?',
                       reply_markup=ReplyKeyboardMarkup(
                       keyboard=[[KeyboardButton(text="/Voltage Motor"), KeyboardButton(text="/Voltage PC")],[KeyboardButton(text="/Volume"), KeyboardButton(text="/Power Off")]]))
    elif command == '/Volume':
        for row in records:
            id = row[0]
            nama = row[1]
            alamat = row[3]

        bot.sendMessage(chat_id, alamat)                            
bot = telepot.Bot('465769589:AAFg10QLqp7XKf_2DpGgTfCWPzCtiOe0Yus')
bot.message_loop(handle)
print ('Menunggu Perintah ...')

while 1:
	time.sleep(10)
