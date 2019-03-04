#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:17:54 2018

@author: nils
"""



class MyGraphicsWindow():
    
    pg = __import__('pyqtgraph')
    pyqt = __import__('PyQt5')
    QtCore = pyqt.QtCore
    
    class CustomGraphicsWindow(pg.GraphicsWindow):
        ##	Function closeEvent
        #	This overrides the closeEvent function in the base class. This function is invoked automatically by QTGui when the window closes.
        #	@param ev This is the event object (i.e. window close). 
        def closeEvent(self, ev):
            ev.accept()        
    
    def __init__(self, title = 'Custom PyQtGraph GraphicsWindow'):
        
        # define Figure and Plot for other functions
        self.ViewPort = self.CustomGraphicsWindow(title=title)
        self.ViewPort.resize(400,400)
        self.ViewPort.setBackground(None)
        
        self.Graph = self.ViewPort.addPlot(title='',
#                                         labels={'left': ('Intensity', 'counts'), 
#                                                 'bottom': ('Wavelength','nm')}
                                                 )
        self.Graph.enableAutoRange('xy', True)
        
        # init timer for data refresh
        self.timer = self.QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(200)
    
    def start(self):
        if self.timer.isActive():
            self.timer.timeout.connect(self.update)
        else:
            self.timer.timeout.connect(self.update)
            self.timer.start(200)

    def update(self): 
        pass
 
    def close(self):
        #self.interrupt()         
        self.timer.stop()