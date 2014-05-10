#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

db = sqlite3.connect(":memory:")

im = db.cursor()

im.execute("""CREATE TABLE kullanicilar (kullanici_adi, parola)""")

veriler = [
            ("ahmet123", "1234"),
            ("mehmet321", "87654321"),
            ("selin456", "123123123")
          ]

for i in veriler:
	im.execute("""Insert Into kullanicilar Values (?, ?)""", i)

db.commit()

kull = raw_input("Kullanıcı Adınız:")
paro = raw_input("Parolanız:")

im.execute("""Select * From kullanicilar Where kullanici_adi = ? and parola = ?""", (kull, paro))

data = im.fetchone()

if data:
	print u"Programa Hoşgeldinz %s!" %data[0]
else:
	print u"Parola veya kullanıcı adı yanlış!"


if kull.isalnum() and paro.isalnum(): #Sadece harf ve sayı girmesi için
    im.execute("""SELECT * FROM kullanicilar WHERE
    kullanici_adi = '%s' AND parola = '%s'"""%(kull, paro))

