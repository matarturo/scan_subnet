#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script: ping.py
# Creado por: Arturo Mata < arturo.mata@gmail.com >
# Versión: 1.0.0
# DESCARGO DE RESPONSABILIDAD
# Este programa está diseñado con fines de investigación busqueda de vulnerabilidades en la configuracion de equipos,
# y el autor no asumirá ninguna responsabilidad si se le da cualquier otro uso.
import socket
from datetime import datetime

# Se agrega la dirección IP del dispositivo gateway
net = input("Ingrese la direccion IP del gateway: ")
net1 = net.split('.')
a = '.'

# Se define el rango de direcciones IP que se desea analizar, dependera de la mascara de la red en estudio
net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Ingrese IP inicial: "))
en1 = int(input("Ingrese IP final: "))
en1 = en1 + 1
t1 = datetime.now()

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,135))
   if result == 0:
      return 1
   else :
      return 0

def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      if (scan(addr)):
         print (addr , "Activo")

run1()
t2 = datetime.now()
total = t2 - t1
