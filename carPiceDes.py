#!/usr/bin/env/python
# -*- coding: utf-8 -*-

##########################################                                    #
#            carPiceDes v0.1b            #                                     
#      Sábado 22 de Febrero 2014         #
#            @Hiram Zúñiga               #
#          hiramhzr at gmail.com         #
##########################################

"""
The program controls a car with a piface
How to use:
Use arrow keys to move the car forward, back, turn left and right
Use d key for put the front wheels straight
Use p key for stop the car
"""

import wx
import pifacedigitalio as piface

#-----main class-----
class carPiceDes(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "carPice", size=(350, 170))
#-----build interface-----
        panel = wx.Panel(self, wx.ID_ANY)
        vbox = wx.BoxSizer(wx.VERTICAL)     
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        sis = "Control de coche Raspberry pi + Piface"
        sis = wx.StaticText(self, -1, sis, (20, 100))
        sis.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD, 0, ""))
        hbox.Add(sis, proportion=1, flag=wx.TOP | wx.LEFT, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn = wx.Button(self, label="Encender")
        self.btn.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
        start_image = wx.Image('data/off.png')
        start_image.Rescale(50, 50)
        image = wx.BitmapFromImage(start_image)
        self.status = wx.StaticBitmap(self, -1, image,
            wx.DefaultPosition, style=wx.BITMAP_TYPE_PNG)
        self.status.SetToolTipString("Encender coche")
        self.cocheEstado = "Estacionado"
        self.cocheEstado = wx.StaticText(self, -1, self.cocheEstado, (20, 100))
        self.cocheEstado.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD, 0, ""))
        hbox2.Add(self.btn, wx.LEFT, border=20)
        hbox2.Add(self.status, flag=wx.LEFT, border=35)
        hbox2.Add(self.cocheEstado, flag=wx.LEFT, border=15)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.apagar = wx.Button(self, label="Apagar")
        self.apagar.Bind(wx.EVT_KEY_DOWN, self.onOff)
        self.cocheEstadoVuelta = ""
        self.cocheEstadoVuelta = wx.StaticText(self, -1, self.cocheEstadoVuelta, (20, 100))
        self.cocheEstadoVuelta.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD, 0, ""))
        hbox3.Add(self.apagar, wx.TOP, border=45)
        hbox3.Add(self.cocheEstadoVuelta, flag=wx.LEFT, border=100)

        vbox.Add(hbox, flag=wx.LEFT|wx.TOP , border=15)    
        vbox.Add(hbox2, flag=wx.LEFT|wx.TOP , border=25)
        vbox.Add(hbox3, flag=wx.LEFT , border=25)
        vbox.Add((-1, 10))
        panel.SetSizer(vbox)    
#-----method when the car turn off -----
    def onOff(self, event):
        start_image = wx.Image('data/off.png')
        start_image.Rescale(50, 50)
        image = wx.BitmapFromImage(start_image)
        self.status.SetBitmap(image)
        self.cocheEstado.SetLabel("Estacionado")
        self.cocheEstadoVuelta.SetLabel("")
        piface.digital_write(0,0)
        piface.digital_write(1,0)
        piface.digital_write(2,0)
        piface.digital_write(3,0)
#-----method when the car turn on ----- 
    def onKeyPress(self, event):
        start_image = wx.Image('data/on.png')
        start_image.Rescale(50, 50)
        image = wx.BitmapFromImage(start_image)
        self.status.SetBitmap(image)
        keycode = event.GetKeyCode()
        print keycode
        if keycode == wx.WXK_UP:
            self.cocheEstado.SetLabel("Adelante")
            piface.digital_write(2,1)
            piface.digital_write(3,0)
        if keycode == wx.WXK_DOWN:
            self.cocheEstado.SetLabel("Atrás")
            piface.digital_write(2,0)
            piface.digital_write(3,1)
        if keycode == wx.WXK_LEFT:
            self.cocheEstadoVuelta.SetLabel("Vuelta Izquierda")
            piface.digital_write(0,1)
            piface.digital_write(1,0)
        if keycode == wx.WXK_RIGHT:
            self.cocheEstadoVuelta.SetLabel("Vuelta Derecha")
            piface.digital_write(0,0)
            piface.digital_write(1,1)
        if keycode == 68:
            self.cocheEstadoVuelta.SetLabel("llantas derechas")
            piface.digital_write(0,0)
            piface.digital_write(1,0)
        if keycode == 80:
            self.cocheEstado.SetLabel("Semaforo en rojo")
            piface.digital_write(2,0)
            piface.digital_write(3,0) 
        if (keycode != 314 and keycode != 315 and keycode != 316 
            and keycode != 317 and keycode != 68 and keycode != 80):
            print "No la tengo registrada"
        event.Skip()
 
# Run the program
if __name__ == "__main__":
    piface.init()
    app = wx.PySimpleApp()
    frame = carPiceDes()
    frame.Center()
    frame.Show()
    app.MainLoop()
