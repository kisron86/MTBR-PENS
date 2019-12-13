import rospy
from std_msgs.msg import String
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
                                         database='pju_its',
                                         user='root',
                                         password='')

    sql_select_Query = "select * from tb_user"
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
        print ('Menunggu Perintah ...')
        global command
        chat_id = msg['chat']['id']
        command = msg['text']
        if command == '/start' or command == '/Kembali' or command == '/Start':
            bot.sendMessage(chat_id, 'Halo Selamat datang Ada yang bisa dibantu?',
                                reply_markup=ReplyKeyboardMarkup(
                                keyboard=[[KeyboardButton(text="/Voltage"), KeyboardButton(text="/Volume")],[KeyboardButton(text="/a"), KeyboardButton(text="/b")]]))
        elif command == '/a':
            for row in records:
                id = row[0]
                nama = row[1]
                alamat = row[3]

            bot.sendMessage(chat_id, alamat)
    bot = telepot.Bot('576188757:AAESFfKu1T7jvZbASG6wpHf0m1WG0-xlOmQ')
    bot.message_loop(handle)
    print ('Menunggu Perintah ...')

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        global command
        chat_id = msg['chat']['id']
        command = msg['text']
        if command == '/start' or command == '/Kembali' or command == '/Start':
            bot.sendMessage(chat_id, 'Halo Selamat datang Ada yang bisa dibantu?',
                                reply_markup=ReplyKeyboardMarkup(
                                keyboard=[[KeyboardButton(text="/Voltage"), KeyboardButton(text="/Volume")],[KeyboardButton(text="/a"), KeyboardButton(text="/b")]]))
        elif command == '/a':
            for row in records:
                id = row[0]
                nama = row[1]
                alamat = row[3]

            bot.sendMessage(chat_id, alamat)
    bot = telepot.Bot('576188757:AAESFfKu1T7jvZbASG6wpHf0m1WG0-xlOmQ')
    bot.message_loop(handle)
    print ('Menunggu Perintah ...')
       # hello_str = "hello world %s" % rospy.get_time()
       # rospy.loginfo(hello_str)
       # pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
