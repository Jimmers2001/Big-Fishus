from PyQt5.QtWidgets import *
from PyQt5 import *
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def Hide_Main_Menu(self):
        self.PLAY.hide()
        self.STATS.hide()
        self.SETTINGS.hide()
        self.QUIT.hide()
        self.TITLE.hide()

    def Show_Main_Menu(self):
        self.PLAY.show()
        self.STATS.show()
        self.SETTINGS.show()
        self.QUIT.show()
        self.TITLE.show()

    def Hide_Statistics_Menu(self):
        self.STATISTICS_TITLE.hide()
        self.RETURN_TO_MAIN_MENU_STATISTICS.hide()

    def Show_Statistics_Menu(self):
        self.STATISTICS_TITLE.show()
        self.RETURN_TO_MAIN_MENU_STATISTICS.show()

    def Hide_Settings_Menu(self):
        self.PLAY.hide()
        self.STATS.hide()
        self.SETTINGS.hide()
        self.QUIT.hide()
        self.TITLE.hide()

    def Show_Settings_Menu(self):
        self.PLAY.show()
        self.STATS.show()
        self.SETTINGS.show()
        self.QUIT.show()

    def QUIT_GAME(self):
        sys.exit()

    def MENU_SETTINGS(self):
        print("u clikced sett")

    def MENU_STATS(self):
        self.Hide_Main_Menu()
        self.Show_Statistics_Menu()

    def STATS_MENU(self):
        self.Hide_Statistics_Menu()
        self.Show_Main_Menu()

    def PLAY_GAME(self):
        print("u clc pay")

    def define_Main_menu_buttons(self):

        #Quit button
        self.PLAY = QPushButton(self)
        self.PLAY.move(500,350)
        self.PLAY.resize(200,50)
        self.PLAY.setText("SWIM")
        self.PLAY.clicked.connect(self.PLAY_GAME)

        #Quit button
        self.STATS = QPushButton(self)
        self.STATS.move(500,400)
        self.STATS.resize(200,50)
        self.STATS.setText("Statistics")
        self.STATS.clicked.connect(self.MENU_STATS)

        #Quit button
        self.SETTINGS = QPushButton(self)
        self.SETTINGS.move(500,450)
        self.SETTINGS.resize(200,50)
        self.SETTINGS.setText("Settings")
        self.SETTINGS.clicked.connect(self.MENU_SETTINGS)

        #Quit button
        self.QUIT = QPushButton(self)
        self.QUIT.move(500,500)
        self.QUIT.resize(200,50)
        self.QUIT.setText("Sleep with the fishes")
        self.QUIT.clicked.connect(self.QUIT_GAME)

    def define_Main_menu_labels(self):

        #title
        self.TITLE = QLabel(self)
        self.TITLE.setText("BIG FISHUS")
        self.TITLE.move(350,30)
        self.TITLE.setFont(QtGui.QFont("Times", 64, QtGui.QFont.Bold))
        self.TITLE.adjustSize()

    def define_Statistics_buttons(self):
        self.RETURN_TO_MAIN_MENU_STATISTICS = QPushButton(self)
        self.RETURN_TO_MAIN_MENU_STATISTICS.move(500,450)
        self.RETURN_TO_MAIN_MENU_STATISTICS.resize(200,50)
        self.RETURN_TO_MAIN_MENU_STATISTICS.setText("Return to Main Menu")
        self.RETURN_TO_MAIN_MENU_STATISTICS.clicked.connect(self.STATS_MENU)
        self.RETURN_TO_MAIN_MENU_STATISTICS.hide()

    def define_Statistics_labels(self):
        self.STATISTICS_TITLE = QLabel(self)
        self.STATISTICS_TITLE.setText("STATISTICS")
        self.STATISTICS_TITLE.move(350,30)
        self.STATISTICS_TITLE.setFont(QtGui.QFont("Times", 64, QtGui.QFont.Bold))
        self.STATISTICS_TITLE.adjustSize()
        self.STATISTICS_TITLE.hide()


    def initUI(self):

        self.showMaximized()
        self.show()
        self.setWindowTitle("Big Fishus") 

        self.define_Main_menu_buttons()
        self.define_Main_menu_labels()

        self.define_Statistics_buttons() 
        self.define_Statistics_labels() #mostly this
        self.Show_Main_Menu()

        

        # self.define_Settings_buttons() #volume, other buttons/labels
        # self.define_Settings_labels()

        # self.define_Pause_buttons() #return to main menu, restart, etc.
        # self.define_Pause_labels()

    '''
    TITLE OF GAME (BIG FISHUS) in big text
    #TODO: fish being chased by bigger fish consistently, chasing a smaller fish
    PLAY BUTTON - move onto a clear canvas
    SETTINGS BUTTON (volume ofc) move to a different window, with a volume
    scrubber and a number that represents the volume
    STATS BUTTON:
        #number of fish eaten.
        #deaths.
    QUIT BUTTON
    '''


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()