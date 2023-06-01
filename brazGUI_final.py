import sys
sys.path.append('/Users/joerg/repos/werdernas')
import os
from pathlib import Path
from typing import Optional
from PySide2.QtGui import QPixmap, QColor, QPalette, QBrush
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QThread
from PySide2.QtCore import Signal as pyqtSignal
import os, subprocess, sys
from MultiComboBox import MultiComboBox
from connectToWerderNas import Main_WERDERNAS
from qt_material import apply_stylesheet
from PySide2.QtGui import QFontDatabase


extra1 = {
    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',
    'mycolor1': '#ffd22b',

    # Font
    # 'font': 'Times',
    'font_size': '12px',
    'line_height': '13px',
    'font_family': 'Roboto',
    # Density scale
    'density_scale': '-3',

    # # palette
    # "primary": "#3b7a9b",  # Primärfarbe
    # "secondary": "#5b5b5b",  # Sekundärfarbe
    # "warning": "#d1a11d",  # Warnfarbe
    # "danger": "#b51a39",  # Gefahrenfarbe
    # "info": "#1a84b5",  # Informationsfarbe
    # "success": "#3db54a",  # Erfolgsfarbe
    # "dark": "#1d1d1d",  # Dunkle Farbe
    # "light": "#f5f5f5",  # Helle Farbe
    # "background": "#222222",  # Hintergrundfarbe
    # environ:
    'pyside2_dev': True,
    'linux': True,
}
extra2 = {
    'font_family': 'Raleway',
}


# apply_stylesheet(app, theme="dark_amber.xml", extra=palette)


os.environ['QT_MAC_WANTS_LAYER'] = '1'

from PySide2.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QTableView,
    QMainWindow, QWidget, QPushButton, QComboBox, QLabel, QListWidget, QTableWidget,
    QFileDialog, QFrame, QMessageBox, QTableWidgetItem, QStyle, QPlainTextEdit, QCheckBox,
    QScrollArea, QHeaderView
)
from PySide2.QtGui import QFont
#from emat_mfl_combined.applications.pdw_upload.analysis_tools.path2proj import Path2ProjAnomaliesGeneral
import pathlib
import os
import pandas as pd
from tabulate import tabulate
from qt_material import QtStyleTools

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class BrazzersManualMainWindow(QWidget):
        
    # def __init__(self, x_pos_parent_window, y_pos_parent_window, width_parent_window):
    #     super().__init__()

    #     self.x_pos_parent_window = x_pos_parent_window
    #     self.y_pos_parent_window = y_pos_parent_window
    #     self.width_parent_window = width_parent_window
    #     self.init_ui()
    def __init__(self):
        super().__init__()
        self.init_ui() 


    def init_ui(self) -> None:

        self.setWindowTitle("BRAZZERS - Manual Edition V0.5!")
        self.resize(1500, 1000)
        self.move(200, 0) #widht, height
        
        
        ### Define the layout ####
        
        # Create the complete layout
        self.complete_layout = QVBoxLayout()

        # Layout for brazzers_label and Site_picture
        self.brazzers_logo_site_logo_layout = QHBoxLayout()

        # Define label for brazzers_logo and site_logo. Fir st step: Default png-picture!
        self.lbl_brazzers_logo = QLabel()
        #self.lbl_brazzers_logo.setStyleSheet("font-size: 18px;" "color: rgb(44, 44, 126);")
        
        self.pixmap_brazzers = QPixmap("/Users/joerg/repos/braz/braz_manual_edition/brazzers.png")
        # self.pixmap_brazzers = QPixmap('/Users/joerg/repos/braz/site_pictures/big_tits_in_sports.png')
        # self.scaled_brazzers = self.pixmap_brazzers.scaled(self.lbl_brazzers_logo.size() / 6, QtCore.Qt.KeepAspectRatio)
        # self.lbl_brazzers_logo.setPixmap(self.scaled_brazzers)
        # self.lbl_brazzers_logo.setScaledContents(False)

        #% Setting the values for the site_logo 
        self.lbl_site_logo = QLabel("Placeholder!!!!")
        pixmap = QPixmap("/Users/joerg/repos/braz/braz_manual_edition/zz_series.jpg")
        # default_site_pic_path = Path(r"/Users/joerg/repos/braz/braz_manual_edition/zz_series.jpg")
        # # site_pic_path = '/Users/joerg/repos/braz/site_pictures/big_tits_in_sports.png'
        # self.pixmap = QPixmap(str(default_site_pic_path))

        scaled = pixmap.scaled(self.lbl_site_logo.size() / 10, QtCore.Qt.KeepAspectRatio)
        self.lbl_site_logo.setPixmap(scaled)
        self.lbl_site_logo.setScaledContents(False)
        # self.lbl_site_logo.hide()
    

        #% Fill the brazzers_and_site_logo_layout
        self.brazzers_logo_site_logo_layout.addWidget(self.lbl_brazzers_logo)
        self.brazzers_logo_site_logo_layout.addStretch(1)
        self.brazzers_logo_site_logo_layout.addWidget(self.lbl_site_logo)

        #% Setting up the QTaable and the control buttons or comboboxes

        #% First: Define QHBoxLayout, so that the alignment of the 
        #% table and the comboboxes are horizontal



        self.brazzers_table_and_comboxes_layout = QHBoxLayout()
        # self.brazzers_table_and_comboxes_layout.setContentsMargins(0, 0, 0, 0)
        #% QTable-Layout 
        self.brazzers_table_layout = QVBoxLayout()
        self.brazzers_table = QTableWidget()
        
        self.brazzers_table.setColumnCount(15)
        self.brazzers_table.setHorizontalHeaderLabels(["Nr.", "Site", "PS1", "PS2", "PS3", "Title",
                                                      "PS4", "PS5", "PS6", "PS7", "PS8", "PS9",
                                                      "PS10", "loc", "link"])


        header = self.brazzers_table.horizontalHeader()
        # header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        self.brazzers_table.resize(100, 500)
        #% Define the function which his executed, when cell was clicked !
        self.brazzers_table.cellClicked.connect(self.cell_was_clicked)

        self.brazzers_table_layout.addWidget(self.brazzers_table)

        #% ComboBoxes_layout
        self.comboboxes_complete_layout = QVBoxLayout()
        
        #% Layout for the site
        self.site_layout = QHBoxLayout()
        # self.site_layout.addSpacing(300)
        # self.site_layout.setAlignment(Qsortedt.AlignLeft)
        self.site_label = QLabel("SITE: ")
        self.site_label.setFont(QFont('Roboto', 13))
        self.site_label.setStyleSheet("color: rgb(255,210,43);font-weight: bold;")
        self.combobox_site = QComboBox()
        self.combobox_site.setFixedWidth(335)
        
        self.site_layout.addWidget(self.site_label)
        self.site_layout.addWidget(self.combobox_site)


        #% Layout for the TopPS, NEW: MultiCombobox
        self.TopPS_layout = QHBoxLayout()
        # self.TopPS_layout.addSpacing(300)
        # self.PS1_layout.setAlignment(Qt.AlignLeft)
        self.TopPS_label = QLabel("TOP PS: ")
        self.TopPS_label.setFont(QFont('Roboto', 13))
        self.TopPS_label.setStyleSheet("color: rgb(255,210,43);font-weight: bold;")
        self.combobox_TopPS = MultiComboBox()
        self.btn_filter_TopPS = QPushButton("Filter Top PS")
        self.btn_filter_TopPS.setFixedWidth(120)
        self.btn_filter_TopPS.clicked.connect(self.filter_and_show_TopPS)
        self.TopPS_layout.addWidget(self.TopPS_label)
        self.TopPS_layout.addWidget(self.btn_filter_TopPS)
        self.TopPS_layout.addWidget(self.combobox_TopPS)
        # self.btn_TopPS = QPushButton("== ALL Top PS ==")
        # self.btn_TopPS.clicked.connect(self.show_TopPSFilterFrame)
        
        # self.TopPS_layout.stretch(1)
        
        # self.TopPS_layout.addWidget(self.btn_TopPS)

        self.TopPS = ['All_TopPS', 'Abbey Brooks', 'Abbie Cat', 'Alena Croft', 'Aletta Ocean', 'Alexis Ford', 
            'Angel Wicky', 'Angela White', 'Armani Black', 'Ava Addams', 'Bridgette B', 'Britney Shannon', 'Carmella Bing', 'Cathy Heaven', 'Chessie Kay', 'Christie Stevens', 'Claire Dames', 'Corinna Blake', 'Dee Williams', 'Diamond Foxxx', 'Donna Bell', 'Ella Hughes', 'Emma Butt', 'Eva Karera', 'Eva Notty', 'Harmony Reigns', 'Holly Halston', 'Jasmine Jae', 'Jayden Jaymes', 'Jenna Presley', 'Jessica Moore', 'Jillian Janson', 'Julia Ann', 'Katie Kox', 'Kelly Divine', 'Kendra Lust', 'Kiara Mia', 'Krissy Lynn', 'Leigh Darby', 'Madison Ivy', 'Marsha May', 'Memphis Monroe', 'Nicolette Shea', 'Nikki Benz', 'Noelle Easton', 'Peta Jensen', 'Rebeca Linares', 'Rebecca More', 'Riley Evans', 'Roberta Gemma', 'Romi Rain', 'Sarah Jessie', 'Sensual Jane', 'Shyla Stylez', 'Sienna West', 'Sophie Dee', 'Stella Cox', 
            'Syren De Mer', 'Tarra White', 'Tory Lane', 'Velicity Von', 'Veronica Avluv', 'Yasmin Scott']
        self.combobox_TopPS.addItems(self.TopPS)
        self.combobox_TopPS.setFixedWidth(200)
        #% Layout for the PS1
        self.PS1_layout = QHBoxLayout()
        # self.PS1_layout.setAlignment(Qt.AlignLeft)
        self.PS1_label = QLabel("PS1: ")
        self.PS1_label.setFont(QFont('Roboto', 13))
        self.PS1_label.setStyleSheet("color: rgb(255,210,43);font-weight: bold;")
        self.combobox_PS1 = QComboBox()
        self.combobox_PS1.setFixedWidth(335)
        self.PS1_layout.addWidget(self.PS1_label)
        self.PS1_layout.addWidget(self.combobox_PS1)

        #% Layout for the PS2
        self.PS2_layout = QHBoxLayout()
        self.PS2_label = QLabel("PS2: ")
        self.PS2_label.setFont(QFont('Roboto', 13))
        self.PS2_label.setStyleSheet("color: rgb(255,210,43);font-weight: bold;")
        # self.PS2_layout.setAlignment(Qt.AlignLeft)
        self.combobox_PS2 = QComboBox()
        self.combobox_PS2.setFixedWidth(335)
        self.PS2_layout.addWidget(self.PS2_label)
        # self.PS2_layout.stretch(1)
        self.PS2_layout.addWidget(self.combobox_PS2)

        #% Layout for the Title
        self.title_layout = QHBoxLayout()
        self.title_label = QLabel("Title: ")
        self.title_label.setFont(QFont('Roboto', 13))
        self.title_label.setStyleSheet("color: rgb(255,210,43);font-weight: bold;")
        # self.title_layout.setAlignment(Qt.AlignLeft)
        self.combobox_title = QComboBox()
        self.combobox_title.setFixedWidth(335)
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.combobox_title)

        #% Layout for load_and_play_buttons
        self.load_play_and_close_button_layout = QHBoxLayout()
        # self.load_play_and_close_button_layout.addSpacing(300)
        self.load_button = QPushButton("Load csv-file")
        # self.load_button.setProperty('class', 'success')
        self.load_button.setFixedWidth(120)
        self.load_button.clicked.connect(self.load_csv_file)
        self.play_button = QPushButton("Play file")
        self.play_button.setProperty('class', 'danger')
        self.play_button.setFixedWidth(120)
        self.play_button.clicked.connect(self.play_file)
        self.close_button = QPushButton("Close APP")
        self.close_button.setFixedWidth(120)
        self.close_button.clicked.connect(self.close)
        self.connect_to_werderNAS_button = QPushButton("Connect")
        self.connect_to_werderNAS_button.setFixedWidth(120)
        self.connect_to_werderNAS_button.clicked.connect(self.connect_to_WerderNAS)
        self.btn_change_theme = QPushButton("Change Theme")
        self.btn_change_theme.setFixedWidth(120)
        self.combobox_change_theme = QComboBox()
        self.combobox_change_theme.setFixedWidth(200)
        self.combobox_change_theme.setStyleSheet('color: rgb(255, 255, 255);')
    
        #% Filling the ComboBox "change_theme"
        #% home directory of the themes: 
        #% /Users/joerg/opt/anaconda3/envs/pyside2_dev/lib/python3.10/site-packages/qt_material/themes
    
        themes_folder = Path(r"/Users/joerg/opt/anaconda3/envs/pyside2_dev/lib/python3.10/site-packages/qt_material/themes")

        lst_themes = []
        for single_theme in themes_folder.iterdir():
            
            lst_themes.append(single_theme.name)
        
        for lf_themes in lst_themes:
            self.combobox_change_theme.addItem(lf_themes)
        
        # self.combobox_change_theme.currentTextChanged.connect(self.theme_changed)
        # self.btn_searchDF = QPushButton("Search DF")
        # self.btn_searchDF.clicked.connect(self.searchDF)

        self.load_play_and_close_button_layout.addWidget(self.load_button)
        self.load_play_and_close_button_layout.addWidget(self.play_button)
        self.load_play_and_close_button_layout.addWidget(self.close_button)
        self.load_play_and_close_button_layout.addWidget(self.connect_to_werderNAS_button)
        self.load_play_and_close_button_layout.addWidget(self.combobox_change_theme)
        # self.load_play_and_close_button_layout.addWidget(self.btn_searchDF)

        #% Layout for Search the DF
        self.search_df_layout = QHBoxLayout()
        self.lbl_searchDF = QLabel("Search DF")
        # self.btn_searchDF.clicked.connect(self.searchDF)
        self.search_textbox = QLineEdit()
        self.search_textbox.returnPressed.connect(self.searchDF)
        self.search_df_layout.addWidget(self.lbl_searchDF)
        self.search_df_layout.addWidget(self.search_textbox)
        
        #% Layout for summary of the filtering:
        self.summary_layout = QGridLayout()
        self.lbl_selected_ps = QLabel("Selected PS")
        self.lbl_ctn_selected_ps = QLabel("Ctn:")
        self.txt_selected_ps = QLabel("")
        self.txt_ctn_selected_ps = QLabel("")


        self.summary_layout.addWidget(self.lbl_selected_ps, 0, 0)
        self.summary_layout.addWidget(self.lbl_ctn_selected_ps, 1, 0)
        self.summary_layout.addWidget(self.txt_selected_ps, 0, 1)
        self.summary_layout.addWidget(self.txt_ctn_selected_ps, 1, 1)


        #% Layout for the Output of the (possible) terminal statements...
        self.text_statements_layout = QVBoxLayout()
        self.output_textbox = QPlainTextEdit()
        text = "Welcome to brazzers db"
        self.output_textbox.setStyleSheet("background-color: rgb(255,210,43); border-radius: 10px")
        self.output_textbox.appendPlainText(text)
        self.text_statements_layout.addWidget(self.output_textbox)

        #% Test for QFrame...
        self.layout_for_frame = QHBoxLayout()
        self.frame_dummy_left = QFrame()
        self.layout_for_frame.addWidget(self.frame_dummy_left)
        self.frame_dummy_left.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame_for_scrollarea = None
        self.scrolling_area = QScrollArea()
        self.scrolling_area.setWidgetResizable(True)

        self.layout_for_frame.addWidget(self.scrolling_area)
        


        #% Add the single components to the layout
        self.comboboxes_complete_layout.addLayout(self.site_layout)
        self.comboboxes_complete_layout.addLayout(self.TopPS_layout)
        self.comboboxes_complete_layout.addLayout(self.PS1_layout)
        self.comboboxes_complete_layout.addLayout(self.PS2_layout)
        self.comboboxes_complete_layout.addLayout(self.title_layout)
        self.comboboxes_complete_layout.addLayout(self.load_play_and_close_button_layout)
        self.comboboxes_complete_layout.addLayout(self.search_df_layout)
        self.comboboxes_complete_layout.addLayout(self.summary_layout)
        self.comboboxes_complete_layout.addLayout(self.text_statements_layout)
        self.comboboxes_complete_layout.addLayout(self.layout_for_frame)

        #% Add both layout to the brazzers_table_and_comboxes_layout
        self.brazzers_table_and_comboxes_layout.addLayout(self.brazzers_table_layout)
        self.brazzers_table_and_comboxes_layout.addLayout(self.comboboxes_complete_layout)


        #% Add Label for the display of the complete link below the qtable
        self.complete_link_layout = QHBoxLayout()
        self.link_label = QLabel("Link: ")
        self.link_text = QLineEdit("")
        self.complete_link_layout.addWidget(self.link_label)
        self.complete_link_layout.addWidget(self.link_text)


        # Set the hand-made complete layout in a superordinate QWidget called dummy_widget
        # dummy_widget = QWidget()
        
        self.complete_layout.addLayout(self.brazzers_logo_site_logo_layout)
        self.complete_layout.setSpacing(10)
        self.complete_layout.addLayout(self.brazzers_table_and_comboxes_layout)#
        self.complete_layout.addStretch(1)
        self.complete_layout.addLayout(self.complete_link_layout)
        
        # dummy_widget.setLayout(self.complete_layout)
        # self.setCentralWidget(dummy_widget)
        self.setLayout(self.complete_layout)
        

    #% Define the methods of the buttons etc....

    def load_csv_file(self):

        self.csv_dir = QFileDialog.getExistingDirectory(
            parent=None,
            caption="Select directory of csv-file",
            # directory="",
        )

        if self.csv_dir == "":
            return
            

        csv_file = pathlib.Path(self.csv_dir) / "df_final_30_05_23.csv"
        # csv_file = pathlib.Path(self.csv_dir) / "df_final_my_db_py_22_04_2022.csv"
        
        print(f"Loading {csv_file} ... ")
        self.loaded_csv_df = pd.read_csv(csv_file)
        # print(self.loaded_csv_df.head())

        self.brazzers_table.setColumnWidth(0, 50)
        self.brazzers_table.setColumnWidth(1, 130)

        #% Filling the table with the content of the csv-file
        # for rows, columns in self.loaded_csv_df.iterrows():
        #     rows = self.brazzers_table.rowCount()
        #     self.brazzers_table.insertRow(rows)
        #     for num, data in enumerate(columns):
        #         self.brazzers_table.setItem(rows, num, QTableWidgetItem(str(data)))
        self.fill_brazzers_table(self.loaded_csv_df)


        #% Filling Combobox of "Top PS"
        self.TopPS_list_unique = list(self.TopPS)#.unique()
        self.TopPS_list_sorted = sorted(list(self.TopPS_list_unique))
        self.TopPS_list_sorted = [lf.lstrip() for lf in self.TopPS_list_sorted]
        self.TopPS_list_sorted.insert(0, "== All Top PS ==")
        # print('Sorted list: ', self.site_list_sorted)

        #% the next code rows are not relevant, when the MultiCombobox is used!!!    
        # for lf, TopPS_i in zip(self.TopPS_list_sorted, range(len(self.TopPS_list_sorted)+1)):
        #     self.combobox_TopPS.addItem(lf)
        #     self.combobox_TopPS.setItemData(TopPS_i, Qt.AlignRight)
        # self.combobox_TopPS.setFixedWidth(260)

        # self.combobox_TopPS.currentTextChanged.connect(self.site_changed)

        #% Filling Combobox of "Site"
        self.site_list_unique = self.loaded_csv_df['Site'].unique()
        self.site_list_sorted = sorted(list(self.site_list_unique))
        self.site_list_sorted = [lf.lstrip() for lf in self.site_list_sorted]
        self.site_list_sorted.insert(0, "== All Sites ==")

        for lf, i in zip(self.site_list_sorted, range(len(self.site_list_sorted)+1)):
            self.combobox_site.addItem(lf)
            self.combobox_site.setItemData(i, Qt.AlignRight)
        self.combobox_site.setFixedWidth(335)
        self.combobox_site.currentTextChanged.connect(self.site_changed)


        #% Filling/setting Top_PS-layout
        # self.btn_filter_TopPS.setFixedWidth(100)
        self.show


        #% Filling the ComboBox "PS1"
        self.ps1_list_unique = self.loaded_csv_df['PS1'].unique()
        self.ps1_list_sorted = sorted(list(self.ps1_list_unique))
        self.ps1_list_sorted = [lf.lstrip() for lf in self.ps1_list_sorted]
        self.ps1_list_sorted.insert(0, "== All PS1 ==")
        # for lf in sorted(self.ps1_list_sorted):
        #     self.combobox_PS1.addItem(lf)  
        self.combobox_PS1.setStyleSheet('color: rgb(255, 255, 255);')
        for lf, i_ps1 in zip(self.ps1_list_sorted, range(len(self.ps1_list_sorted)+1)):
            self.combobox_PS1.addItem(lf)    
            self.combobox_PS1.setItemData(i_ps1, Qt.AlignHCenter)
        self.combobox_PS1.setFixedWidth(335)
        self.combobox_PS1.currentTextChanged.connect(self.ps1_changed)
        
        #% Filling the ComboBox "PS2" 
        self.ps2_list_unique = self.loaded_csv_df['PS2'].unique()
        self.ps2_list_sorted = sorted(list(self.ps2_list_unique))
        self.ps2_list_sorted = [lf.lstrip() for lf in self.ps2_list_sorted]
        self.ps2_list_sorted.insert(0, "== All PS2 ==")
        self.combobox_PS2.setStyleSheet('color: rgb(255, 255, 255);')

        for lf in sorted(self.ps2_list_sorted):
            self.combobox_PS2.addItem(lf)  
        for lf, i_ps2 in zip(self.ps2_list_sorted, range(len(self.ps2_list_sorted)+1)):
            self.combobox_PS2.addItem(lf)    
            self.combobox_PS2.setItemData(i_ps2, Qt.AlignHCenter)
        

        #% Filling the ComboBox "PS2" and adjust it with the max_width of text-entry    
        # self.combobox_PS2.setFixedWidth(160)

        # self.combobox_title.setFixedWidth(160)

        # rows = 0

    def cell_was_clicked(self, row, column):
        # print("Row %d and Column %d was clicked" % (row, column))
        item = self.brazzers_table.item(row, 0)  
        ### look at the second entry! Because it is 0, python gives the column!

        self.ID_row = item.text()
        # print('selected row :', self.ID_row)
        self.selected_file = self.loaded_csv_df.iloc[int(self.ID_row)]['Link']
        self.selected_site_for_picture = self.loaded_csv_df.iloc[int(self.ID_row)]['Site']
        self.selected_title = self.loaded_csv_df.iloc[int(self.ID_row)]['Title']

        # print('Link: \n', self.selected_file)
        # print('Selected site: \n', self.selected_site_for_picture)
        # print('Selected title: \n', self.selected_title)
        self.link_text.setText(self.selected_file)
        self.link_text.setStyleSheet('color: rgb(255, 255, 255);')
        name_tmp = self.selected_site_for_picture.replace(" ", "_").lower() + ".png"
        path_folder_site_pictures = "/Users/joerg/repos/braz/site_pictures"
        path_to_picture = os.path.join(path_folder_site_pictures, name_tmp)
        # print('path_to_picture', path_to_picture)
        pixmap = QPixmap(path_to_picture)
        # self..setPixmap(pixmap)


    #% function for executing, when the site is changed in the combobox...
    def site_changed(self):
       self.brazzers_table.setRowCount(0)
       self.selected_site = self.combobox_site.currentText()
       print('currentText_site: ', self.combobox_site.currentText())

       if self.selected_site == "== All Sites ==":
           self.df_selected_site = self.loaded_csv_df
       else:
           self.df_selected_site = self.loaded_csv_df[self.loaded_csv_df['Site'] == self.combobox_site.currentText()].sort_values(by="PS1", ascending=True)
        
    #    self.df_selected_site = self.loaded_csv_df[self.loaded_csv_df['Site'] == self.combobox_site.currentText()]'
       

       self.fill_brazzers_table(self.df_selected_site)
       self.output_textbox.clear()
       displayed_text = "Site: {site}, counts: {ctn}".format(site=self.combobox_site.currentText(), ctn=len(self.df_selected_site))

       self.output_textbox.appendPlainText(displayed_text)
       self.show_brazzers_site_logo(self.selected_site)   


    #% function for executing, when the PS1 is changed in the combobox...
    def ps1_changed(self):
       self.brazzers_table.setRowCount(0)
       self.selected_ps1 = self.combobox_PS1.currentText()
       print('current_PS1: ', self.combobox_PS1.currentText())

       if self.selected_ps1 == "== All PS1 ==":
           self.df_selected_ps1 = self.loaded_csv_df
       else:
           self.df_selected_ps1 = self.loaded_csv_df[self.loaded_csv_df['PS1'] == self.combobox_PS1.currentText()].sort_values(by="PS1", ascending=True)
        
    #    self.df_selected_site = self.loaded_csv_df[self.loaded_csv_df['Site'] == self.combobox_site.currentText()]'
       
       self.fill_brazzers_table(self.df_selected_ps1)
    #    self.show_brazzers_site_logo(self.selected_site)  
 
    def theme_changed(self):
        self.selected_theme = self.combobox_change_theme.currentText()
        print('selected: theme: ', self.combobox_change_theme.currentText())


    def play_file(self):
        subprocess.call(['open', self.selected_file])

    def fill_brazzers_table(self, selected_df: pd.DataFrame):
        # self.loaded_csv_df = load_csv_df
        # Erstellen Sie eine QPalette-Instanz
        # Erstellen Sie eine Instanz der gewünschten Farbe
        color = QColor(extra1["success"])
        # Setzen Sie die Standardpalette des QTableWidgetItem zurück
        palette = QPalette()
        # self.brazzers_table.item(rows, num).setPalette(palette)

        

# Setzen Sie die Hintergrundfarbe des QTableWidgetItem
        

        #% Filling the table with the content of the csv-file
        for rows, columns in selected_df.iterrows():
            rows = self.brazzers_table.rowCount()
            self.brazzers_table.insertRow(rows)
            for num, data in enumerate(columns):
                self.brazzers_table.setItem(rows, num, QTableWidgetItem(str(data)))

                if rows == 3 and num == 2:
                    self.brazzers_table.item(rows, num).setBackground(QColor(255,210,43))
                    self.brazzers_table.item(rows, num).setForeground(QColor(12,210,43))
                    # Wenden Sie die Palette auf das QTableWidgetItem an
                    
                    self.brazzers_table.item(rows, num).setBackground(color)
                    # Deaktivieren Sie setAutoFillBackground
                    # self.brazzers_table.item(rows, num).setAutoFillBackground(False)

                    # Wiederherstellen der Standardpalette des QTableWidgetItem
                    # palette = self.brazzers_table.item(rows, num).palette()
                    # self.brazzers_table.item(rows, num).setPalette(palette)

                    # self.brazzers_table.item.setProperty('cool', True)
                    # self.brazzers_table.item(rows, num).setProperty('class', 'success') # (QColor(extra["warning"]))
        # self.brazzers_table.setItem(3, 5, QTableWidgetItem())
        # self.brazzers_table.item(3, 5).setBackground(QColor(255,210,43)) 
        # self.brazzers_table.setBackground(QColor(palette["green"]))

        
        # self.brazzers_table.setStyleSheet("")
        # self.brazzers_table.setStyleSheet("QTableWidgetItem {foreground-color: green; color: red;}")
        # item = QTableWidgetItem('black')
        # item.setBackgroundColor(QColor(255,210,43))
        # item.setForeground(QColor(255, 155, 255))
        # item.setBackgroundColor(QColor(230,230,250))
        
        

        # item.setForeground(QBrush(QColor("blue")))
        # self.brazzers_table.setItem(3, 2, item)
        # # item.setBackground(background_color)
        # item.setForeground(QColor("red"))  
        # self.brazzers_table.setItem(3, 2, item)

        # background_color = QColor(palette.color(QPalette.Light))
        # item.setBackground(background_color)
        # table_widget.setItem(row, column, item)

        # print('Debug 1', selected_df)

    def show_brazzers_site_logo(self, selected_site_for_picture):
            self.lbl_site_logo.hide()
            self.selected_site_for_picture = selected_site_for_picture
            if self.selected_site_for_picture == "== All Sites ==":
                path_to_picture = Path("/Users/joerg/repos/braz/braz_manual_edition/zz_series.jpg")
                
            else:
                print('self.selected_site_for_picture: ', self.selected_site_for_picture)
                site_name_tmp = self.selected_site_for_picture.replace(" ", "_").lower() + ".png"
                path_folder_site_pictures = Path(r"/Users/joerg/repos/braz/site_pictures")
                path_to_picture = path_folder_site_pictures / Path(site_name_tmp)


            lbl_site_logo_tmp = QLabel("")
            
            # self.pixmap = QPixmap("/Users/joerg/repos/braz/braz_manual_edition/zz_series.jpg")
            
            # default_site_pic_path = Path(r"/Users/joerg/repos/braz/site_pictures/big_tits_in_uniform.png")
            
            # site_pic_path = '/Users/joerg/repos/braz/site_pictures/big_tits_in_sports.png'
            pixmap = QPixmap(str(path_to_picture))

            scaled = pixmap.scaled(lbl_site_logo_tmp.size() / 10, QtCore.Qt.KeepAspectRatio)
            
            # scaled = pixmap.scaled(self.lbl_site_logo.size() / 4, QtCore.Qt.KeepAspectRatio)
            self.lbl_site_logo.setPixmap(scaled)
            self.lbl_site_logo.setScaledContents(False)
            self.lbl_site_logo.show()




            # self.selected_site_for_picture = selected_site_for_picture
            # print('self.selected_site_for_picture: ', self.selected_site_for_picture)
            # site_name_tmp = self.selected_site_for_picture.replace(" ", "_").lower() + ".png"
            # path_folder_site_pictures = Path(r"/Users/joerg/repos/braz/site_pictures")
            # path_to_picture = path_folder_site_pictures / Path(site_name_tmp)
            # # path_to_picture = os.path.join(path_folder_site_pictures, site_name_tmp)

            # print('path_to_picture', str(path_to_picture))
            # # self.pixmap = QPixmap(str(path_to_picture))
            
            # print('Debug 1')
            # pixmap = QPixmap(str(path_to_picture))
            # print('Debug 2')
            # lbl_site_logo_tmp = QLabel("")
            # print('Debug 3')
            # lbl_site_logo_tmp.setPixmap(pixmap)
            # # scaled_brazzers_picture = pixmap.scaled(lbl_site_logo_tmp.size() / 10, QtCore.Qt.KeepAspectRatio)
            
            # # lbl_site_logo_tmp.show()
            # print('Debug 4')
            # # self.lbl_site_logo.setScaledContents(False)
            # print('Debug 5')
            # # self.lbl_site_logo = lbl_site_logo_tmp
            # #self.lbl_site_logo.show()


            # image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.png)")
            # imagePath = image[0]
            # pixmap = QPixmap(imagePath)
            # self.pixmap_brazzers.setPixmap(pixmap)
            # print(imagePath)

    # def show_TopPSFilterFrame(self):
    #     print('Going into TopPSFilterFrame ....')
    #     self.anom_type_filter_frame = AnomTypeFilterFrame(parent=self)
    #     self.anom_type_filter_frame.move(self.btn_TopPS.pos())
    #     self.anom_type_filter_frame.init_ui()

    def filter_and_show_TopPS(self):
        print('self.combobox_TopPS.currentData: ', self.combobox_TopPS.currentData())
        self.brazzers_table.setRowCount(0)
        self.selected_TopPS = list(self.combobox_TopPS.currentData())
        print('TopPS selected!: ', self.selected_TopPS[0])
        print('len of TopPS selected: ', len(self.selected_TopPS))

        if self.selected_TopPS[0] == "All_TopPS":
            print('Debug 5')
            self.df_selected_TopPS = self.loaded_csv_df
        else:
            # self.df_selected_TopPS = self.loaded_csv_df[self.loaded_csv_df['PS1'].isin(self.selected_TopPS)].sort_values(by="PS1", ascending=True)
            self.df_selected_TopPS = self.loaded_csv_df[self.loaded_csv_df['PS1'].isin(self.selected_TopPS) |
                                                        self.loaded_csv_df['PS2'].isin(self.selected_TopPS) | 
                                                        self.loaded_csv_df['PS3'].isin(self.selected_TopPS) |
                                                        self.loaded_csv_df['PS4'].isin(self.selected_TopPS) |
                                                        self.loaded_csv_df['PS5'].isin(self.selected_TopPS) |
                                                        self.loaded_csv_df['PS6'].isin(self.selected_TopPS) |
                                                        self.loaded_csv_df['PS7'].isin(self.selected_TopPS) |
                                                        self.loaded_csv_df['PS8'].isin(self.selected_TopPS) |
                                                        self.loaded_csv_df['PS9'].isin(self.selected_TopPS) |
                                                        self.loaded_csv_df['PS10'].isin(self.selected_TopPS) ].sort_values(by="PS1", ascending=True)

        if len(self.selected_TopPS) == 1:
            self.txt_selected_ps.setText(self.selected_TopPS[0])
            self.txt_ctn_selected_ps.setText(str(len(self.df_selected_TopPS)))
            print('Length of single TopPS df: ', len(self.df_selected_TopPS))
            
        #    self.df_selected_site = self.loaded_csv_df[self.loaded_csv_df['Site'] == self.combobox_site.currentText()]'
        
        self.fill_brazzers_table(self.df_selected_TopPS)
        # self.show_brazzers_site_logo(self.selected_site)   

    def searchDF(self):
        # df: pd.DataFrame(), search_string: str()
        self.brazzers_table.setRowCount(0)
        print('Return was pressed!!!')
        print('Value: ', self.search_textbox.text())
        self.search_string = self.search_textbox.text()
        self.df = self.loaded_csv_df
        # self.df = df
        # self.search_string = search_string!
        mask = (self.df.applymap(lambda x: isinstance(x, str) and self.search_string in x)).any(1)
        self.filtered_df = self.df[mask]
        self.fill_brazzers_table(self.filtered_df)
        # #print('mask: ', dataFrame[mask]['Title'])
        print('filtered df: ', self.df[mask])
        # return self.df[mask]#['Title']

    def connect_to_WerderNAS(self):
        # self.main_werderNAS_window = Main_WERDERNAS(200, 150, 250, 150)
        self.main_werderNAS_window = Main_WERDERNAS()
        self.main_werderNAS_window.show()

############################################################
class AnomTypeFilterFrame(QFrame):
    """Overlay frame to set the current TopPS to filter.

    Args:
        parent: Parent widget in which this widget may be embedded into.
    """

    filter_anom_types_signal = QtCore.Signal(list)

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        style = """AnomTypeFilterFrame {
            border: 1px solid;
            background-color: white;
        }
        """
        self.setStyleSheet(style)

        # self.existing_anom_types: list[str] = []
        self.existing_anom_types = ['Abbey Brooks', 'Abbie Cat', 'Alena Croft', 'Aletta Ocean', 'Alexis Ford', 
            'Angel Wicky', 'Angela White', 'Armani Black', 'Ava Addams', 'Bridgette B']
            # 'Britney Shannon', 'Carmella Bing', 'Cathy Heaven', 'Chessie Kay', 'Christie Stevens', 'Claire Dames', 'Corinna Blake', 'Dee Williams', 'Diamond Foxxx']
            # ', 'Donna Bell', 'Ella Hughes', 'Emma Butt', 'Eva Karera', 'Eva Notty', 'Harmony Reigns', 'Holly Halston', 'Jasmine Jae', 'Jayden Jaymes', 'Jenna Presley', 'Jessica Moore', 'Jillian Janson', 'Julia Ann', 'Katie Kox', 'Kelly Divine', 'Kendra Lust', 'Kiara Mia', 'Krissy Lynn', 'Leigh Darby', 'Madison Ivy', 'Marsha May', 'Memphis Monroe', 'Nicolette Shea', 'Nikki Benz', 'Noelle Easton', 'Peta Jensen', 'Rebeca Linares', 'Rebecca More', 'Riley Evans', 'Roberta Gemma',
            # 'Romi Rain', 'Sensual Jane', 'Shyla Stylez', 'Sienna West', 'Sophie Dee', 'Stella Cox', 
            # 'Syren De Mer', 'Tarra White', 'Tory Lane', 'Velicity Von', 'Veronica Avluv', 'Yasmin Scott']
        self.chosen_anom_types: list[str] = []

        self.checkboxes: list[QCheckBox] = []
        self.enabling_mapping: Optional[dict[str, bool]] = None

    def init_ui(self) -> None:
        """Initialize the ui."""
        # Reparent layout to create the new layout without any issues
        if self.layout():
            QWidget().setLayout(self.layout())

        if self.enabling_mapping is None:
            self.enabling_mapping: dict[str, bool] = {}

            for single_topPS in ["All"] + self.existing_anom_types:
                self.enabling_mapping[single_topPS] = True
            # for anom_type in ["All"] + self.existing_anom_types:
            #     self.enabling_mapping[anom_type] = True

            self.enabling_mapping["None"] = False

        self.checkboxes: list[QCheckBox] = []

        layout = QVBoxLayout()

        anom_types_layout = QVBoxLayout()

        for anom_type in ["All", "None"] + self.existing_anom_types:
            anom_type_checkbox = QCheckBox(anom_type)
            anom_type_checkbox.setChecked(self.enabling_mapping[anom_type])
            anom_type_checkbox.clicked.connect(self.toggle_anom_type)
            anom_types_layout.addWidget(anom_type_checkbox)
            self.checkboxes.append(anom_type_checkbox)

        layout.addLayout(anom_types_layout)

        button_layout = QHBoxLayout()
        self.apply_button = QPushButton("Apply")
        self.apply_button.clicked.connect(self.emit_chosen_anom_types)
        button_layout.addWidget(self.apply_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setMinimumHeight(35 * (2 + len(self.existing_anom_types)) + 30)
        self.setMinimumWidth(200)
        self.show()

    def set_existing_anom_types(self, anom_types: list[str]) -> None:
        """Sets the existing anomaly types for this frame. The input will be sorted.

        Args:
            anom_types: List of anomaly types, e.g. ["LIN", "MIFE"]
        """
        self.existing_anom_types = sorted(anom_types)

    def emit_chosen_anom_types(self) -> None:
        """Emits the chosen anomaly types"""
        self.hide()

        self.chosen_anom_types: list[str] = []

        for anom_type in ["All", "None"] + self.existing_anom_types:
            is_checked = self.enabling_mapping[anom_type]

            if is_checked and anom_type not in {"All", "None"}:
                self.chosen_anom_types.append(anom_type)

        self.filter_anom_types_signal.emit(self.chosen_anom_types)

    def toggle_anom_type(self, state: bool) -> None:
        """Check or uncheck the clicked checkbox and update other checkboxes if needed.

        Since there is an "All" and a "None" checkbox, there is some update logic needed to
        check or uncheck other checkboxes.

        Args:
            state: True if the checkbox has been checked, False otherwise
        """

        clicked_anom_type = self.sender().text()

        if state is True:
            if clicked_anom_type == "All":
                for anom_type in ["All"] + self.existing_anom_types:
                    self.enabling_mapping[anom_type] = True

                self.enabling_mapping["None"] = False

            elif clicked_anom_type == "None":
                for anom_type in ["All"] + self.existing_anom_types:
                    self.enabling_mapping[anom_type] = False

                self.enabling_mapping["None"] = True

            else:
                self.enabling_mapping[clicked_anom_type] = True

                all_enabled = True

                for anom_type in self.existing_anom_types:
                    if self.enabling_mapping[anom_type] is False:
                        all_enabled = False
                        break

                self.enabling_mapping["All"] = all_enabled
                self.enabling_mapping["None"] = False

        elif state is False:
            if clicked_anom_type == "All":
                for anom_type in ["All"] + self.existing_anom_types:
                    self.enabling_mapping[anom_type] = False

                self.enabling_mapping["None"] = True
            elif clicked_anom_type == "None":
                for anom_type in ["All"] + self.existing_anom_types:
                    self.enabling_mapping[anom_type] = True

                self.enabling_mapping["None"] = False
            else:
                self.enabling_mapping[clicked_anom_type] = False
                self.enabling_mapping["All"] = False

                none_enabled = True

                for anom_type in self.existing_anom_types:
                    if self.enabling_mapping[anom_type] is True:
                        none_enabled = False
                        break

                self.enabling_mapping["None"] = none_enabled

        else:
            raise ValueError(f"State {state} is not valid.")

        for anom_type, checkbox in zip(["All", "None"] + self.existing_anom_types, self.checkboxes):
            is_checked = self.enabling_mapping[anom_type]
            checkbox.setChecked(is_checked)

        if self.enabling_mapping["None"] is True:
            self.apply_button.setEnabled(False)
        else:
            self.apply_button.setEnabled(True)

class RuntimeStylesheets(BrazzersManualMainWindow, QtStyleTools):
    
    def __init__(self):
        super().__init__()
        #self.main = QUiLoader().load('main_window.ui', self)
        # self.main = BrazzersManualMainWindow(200, 330, 800) 
        self.main = BrazzersManualMainWindow() 
        # self.apply_stylesheet(self.main, 'dark_amber.xml', extra=extra)

        # self.main.btn_change_theme.clicked.connect(lambda: self.apply_stylesheet(self.main, 'dark_teal.xml'))
        apply_stylesheet(app, theme='dark_teal.xml', extra=extra1)
        self.main.combobox_change_theme.currentTextChanged.connect(lambda: self.apply_stylesheet(self.main, self.main.combobox_change_theme.currentText(), extra=extra1))
        # self.main.btn_change_theme.clicked.connect(lambda: self.apply_stylesheet(self.main, 'light_red.xml', extra=extra2))
        # # self.main.pushButton_3.clicked.connect(lambda: self.apply_stylesheet(self.main, 'light_blue.xml', extra={'font_family': 'Raleway', }))
        # # self.apply_stylesheet(self.main, 'light_red.xml')
        # self.apply_stylesheet(self.main, 'light_blue.xml'

    
# extra['QMenu'] = {
#     'height': 50,
#     'padding': '10px 10px 10px 10px',  # top, right, bottom, left
# }

if __name__ == '__main__':
    app = QApplication(sys.argv)

    QFontDatabase.addApplicationFont('Raleway-Regular.ttf')
    frame = RuntimeStylesheets()
    frame.main.show()
    
    # apply_stylesheet(app, theme='dark_teal.xml', invert_secondary=False, extra=extra)
    # window = BrazzersManualMainWindow(200, 330, 800)
    # window = window = BrazzersManualMainWindow()
    # window.show()
    sys.exit(app.exec_())