#!/usr/bin/env python
import rospy

from std_msgs.msg import Int32
from random import randint

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


#define the random_number Publisher
def random_number_publisher():
    rospy.init_node('random_number')
    pub=rospy.Publisher('rand_no', Int32, queue_size=10)
    rate= rospy.Rate(2)
#//generate a random number at every 2 seconds
    while not rospy.is_shutdown():
        #random_msg=randint(0,5000)
        #rospy.loginfo(random_msg)
        #pub.publish(random_msg)
        rate.sleep()

if __name__=='__main__':
    try:
        connection = mysql.connector.connect(host='localhost',
                                                 database='trash',
                                                 user='root',
                                                 password='Qwerty123#')
        sql_select_Query = "select * from data_sensor"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        #random_number_publisher()
    except rospy.ROSInterruptException:
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
                                keyboard=[[KeyboardButton(text="/Voltage"), KeyboardButton(text="/Volume")],[KeyboardButton(text="/a"), KeyboardButton(text="/b")]]))
        elif command == '/Voltage':
            for row in records:
                id = row[0]
                nama = row[1]
                alamat = row[3]

    bot.sendMessage(chat_id, alamat)
    bot = telepot.Bot('576188757:AAESFfKu1T7jvZbASG6wpHf0m1WG0-xlOmQ')
    bot.message_loop(handle)
    print ('Menunggu Perintah ...')
    while 1:
        time.sleep(10)
    pass
