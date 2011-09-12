import af

WndInfo = None

from PyQt4 import QtGui

def showInfo( tray = None):
   renders = af.Cmd().renderGetLocal()

   if len( renders) == 0:
      if tray is not None: tray.showMessage('Render information:', 'No local render client founded.')
      return

   global WndInfo

   WndInfo = QtGui.QTextEdit()
   msg = ''
   for rinfo in renders:
      msg += rinfo['info']
      msg += rinfo['resources']
   WndInfo.setPlainText( msg)
   WndInfo.setReadOnly( True)
   WndInfo.resize( WndInfo.viewport().size())
   WndInfo.setWindowTitle('AFANASY Render Information:')
   WndInfo.show()

def exit(        text = '(keeper)'): cmd = af.Cmd().renderExit( text)
def exittalk(    text = '(keeper)'): cmd = af.Cmd().talkExit( text)
def exitmonitor( text = '(keeper)'): cmd = af.Cmd().monitorExit( text)
