# -*- coding: utf8 -*-
import telebot
from telebot import types
import random
import os

bot=telebot.TeleBot("6") #ip_telegramBot by FatherBot

fall = {}   # user_data

list_of_heroes = os.listdir(path="C:/") #path to images

stol1_pers1 = None 
stol1_pers2 = None
stol1_pers3 = None

stol_mar20 = 0
stol_mar30 = 0
stol_mar40 = 0

stol_mar1 = []
stol_mar2 = []
stol_mar3 = []

@bot.message_handler(commands=['start'])    
def send_welcome(message):
  if message.from_user.username:
    mood = message.from_user.username
  else:
    mood = str(message.from_user.first_name) + ' '
  text = f"Привет, {mood}!"

  keyboard = types.InlineKeyboardMarkup()
  callback_button1 = types.InlineKeyboardButton(text="MARVEL", callback_data="1marvel")
  keyboard.add(callback_button1)
  callback_button2 = types.InlineKeyboardButton(text="DC Comics", callback_data="1dc")
  keyboard.add(callback_button2)
  bot.send_message(message.chat.id, text + "\n\n" + "Это игра под названием \"Угадай Кто?\"! Здесь ты играя вместе с друзьями будешь угадывать одного персонажа среди 30-и! \n\nЧтобы начать играть, просто выбери тематику!", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def longname1(call):
  global fall
  global stol_mar20
  global stol_mar30
  global stol_mar40

  if call.message.chat.id in fall:
    pass
  else:
    fall[call.message.chat.id] = [None, 0, 0, 0, [], None, 0, None, [], None, 0, None]

  if call.data[0] == "1":
    fall[call.message.chat.id][0] = call.data
    destroy(call)
    longname1(call)
  elif call.data in ["20", "30", "40"]:
    if call.data == "20":
      stol_mar20 = stol_mar20 + 1
    if call.data == "30":
      stol_mar30 = stol_mar30 + 1
    if call.data == "40":
      stol_mar40 = stol_mar40 + 1
    fall[call.message.chat.id][1] = call.data
    destroy(call)
    longname2(call)
  elif call.data == "200":
    fall[call.message.chat.id][2] = call.data
    destroy(call)
    boter(call) 

def destroy(call):
  bot.delete_message(call.message.chat.id, call.message.message_id)

def longname1(call):
  keyboard1 = types.InlineKeyboardMarkup()
  callback_button3 = types.InlineKeyboardButton(text="Стол №1", callback_data=20)
  keyboard1.add(callback_button3)
  callback_button4 = types.InlineKeyboardButton(text="Стол №2", callback_data=30)
  keyboard1.add(callback_button4)
  callback_button5 = types.InlineKeyboardButton(text="Стол №3", callback_data=40)
  keyboard1.add(callback_button5)
  bot.send_message(call.message.chat.id, "А теперь стол, где тебя ждут друзья.", reply_markup=keyboard1)

def longname2(call):
  keyboard2 = types.InlineKeyboardMarkup()
  callback_button6 = types.InlineKeyboardButton(text="Готов!", callback_data=200)
  keyboard2.add(callback_button6)
  bot.send_message(call.message.chat.id, "Ну что, готов?", reply_markup=keyboard2)

def boter(call):    #game
  list_pers(call)
  while fall[call.message.chat.id][10] < 7:
    if fall[call.message.chat.id][4][fall[call.message.chat.id][10]] == fall[call.message.chat.id][11]:
      fall[call.message.chat.id][10] = fall[call.message.chat.id][10] + 1
      continue
    else:  
      bot.send_photo(call.message.chat.id, open("C:/" + fall[call.message.chat.id][4][fall[call.message.chat.id][10]], "rb")) #path to images
      fall[call.message.chat.id][10] = fall[call.message.chat.id][10] + 1
  bot.send_message(call.message.chat.id, "Это твой персонаж:")
  bot.send_photo(call.message.chat.id, open("C:/" + fall[call.message.chat.id][11], "rb")) #path to images

def list_pers(call):
  global list_of_heroes

  global stol_mar20
  global stol_mar30
  global stol_mar40

  global stol_mar1
  global stol_mar2
  global stol_mar3

  global stol1_pers1
  global stol1_pers2
  global stol1_pers3

  if stol_mar20 == 1:
    posrednik_schet = 0
    while posrednik_schet < 7:
      posrednik = random.choice(list_of_heroes)
      if posrednik in stol_mar1:
        pass
      else:
        stol_mar1.append(posrednik)
        posrednik_schet = posrednik_schet + 1
    fall[call.message.chat.id][4] = stol_mar1
  else:
    fall[call.message.chat.id][4] = stol_mar1

  if stol_mar20 == 1:
    stol1_pers1 = random.choice(stol_mar1)
    stol1_pers2 = random.choice(stol_mar1)
    while stol1_pers2 == stol1_pers1:
      stol1_pers2 = random.choice(stol_mar1)
      if stol1_pers2 != stol1_pers1:
        break
    stol1_pers3 = random.choice(stol_mar1)
    while stol1_pers3 == stol1_pers1 or stol1_pers2:
      stol1_pers3 = random.choice(stol_mar1)
      if stol1_pers3 != stol1_pers1:
        if stol1_pers3 != stol1_pers2:
          break
  else:
    pass  

  if stol_mar20 == 1:
    fall[call.message.chat.id][11] = stol1_pers1
  elif stol_mar20 == 2:
    fall[call.message.chat.id][11] = stol1_pers2
  elif stol_mar20 == 3:
    fall[call.message.chat.id][11] = stol1_pers3

bot.polling()


