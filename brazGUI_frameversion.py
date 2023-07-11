import sys
sys.path.append('/Users/joerg/repos/werdernas')
import os
from pathlib import Path
from typing import Optional
from PySide2.QtGui import QPixmap, QColor, QPalette, QBrush
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QColor, QPalette, QBrush
from PySide2.QtCore import QThread
from PySide2.QtCore import Signal as pyqtSignal
import os, subprocess, sys
from MultiComboBox import MultiComboBox
from connectToWerderNas import Main_WERDERNAS
from qt_material import apply_stylesheet
from PySide2.QtGui import QFontDatabase
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt
from typing import Optional
import pandas as pd 
os.environ['QT_MAC_WANTS_LAYER'] = '1'

from PySide2.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QTableView,
    QMainWindow, QWidget, QPushButton, QComboBox, QLabel, QListWidget, QTableWidget,
    QFileDialog, QFrame, QMessageBox, QTableWidgetItem, QStyle, QPlainTextEdit, QCheckBox,
    QScrollArea, QHeaderView, QStyleFactory, QTextEdit, QTabWidget, QSizePolicy
)
from PySide2.QtGui import QFont
#from emat_mfl_combined.applications.pdw_upload.analysis_tools.path2proj import Path2ProjAnomaliesGeneral
import pathlib
import os
from tabulate import tabulate
from qt_material import QtStyleTools

BLUEISH_COLOR = QColor(230, 230, 250)

# def get_brazzers_csv_content(
#         loaded_csv_df: pd.DataFrame,

# )


class BrazzersManualMainWindow(QWidget):
    """Application to visualize the contents of brazzers folders

    Args:
        loaded_csv_df = dataframe of the loaded csv-file
    """

    def __init__(self, loaded_csv_df: Optional[pd.DataFrame] = None,
                 parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.setWindowTitle("BRAZZERS - QFrame Edition V0.2")
        self.resize(1280, 820)
        self.move(200, 0)

        self.set_dark_mode()

        if loaded_csv_df is None:
            self.loaded_csv_df = None
        else:
            self.loaded_csv_df = loaded_csv_df

        self.init_ui()

    def init_ui(self) -> None:
        """ Initialize the ui."""
        overall_layout = QVBoxLayout()
        self.tab_widget = QTabWidget()
        
        self.sites_ps_overview_wiget = BrazzersSitesPSOverview(self.loaded_csv_df, parent=self)
        self.tab_widget.addTab(self.sites_ps_overview_wiget, "Sites & PS")

        self.zz_series_overview = BrazzersZZSeriesOverview()
        self.tab_widget.addTab(self.zz_series_overview, "ZZ Series")

        overall_layout.addWidget(self.tab_widget)
        self.setLayout(overall_layout)

    def set_dark_mode(self):
        app.setStyle(QStyleFactory.create("Fusion"))
        palette = self.palette()
        palette.setColor(palette.Window, QColor(53, 53, 53))
        palette.setColor(palette.WindowText, QColor(QtCore.Qt.green))
        palette.setColor(palette.Base, QColor(25, 25, 25))
        palette.setColor(palette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(palette.ToolTipBase, QtCore.Qt.white)
        palette.setColor(palette.ToolTipText, QtCore.Qt.white)
        palette.setColor(palette.Text, QtCore.Qt.white)
        palette.setColor(palette.Button, QColor(53, 53, 53))
        palette.setColor(palette.ButtonText, QtCore.Qt.white)
        palette.setColor(palette.BrightText, QtCore.Qt.red)
        palette.setColor(palette.Highlight, QColor(142, 145, 197))
        palette.setColor(palette.HighlightedText, QtCore.Qt.black)
        palette.setColor(palette.Disabled, palette.Text, QtCore.Qt.darkGray)
        palette.setColor(palette.Disabled, palette.ButtonText, QtCore.Qt.darkGray)

        self.setPalette(palette)

class BrazzersSitesPSOverview(QWidget):
    """Widget to visualize the Overview of Brazzers Sites & PS.
       This replaces the former class BrazzersManualMainWindow 
       from the python-file: brazGUI_final.py!

    Args:
        loaded_csv_df: dataframe of the loaded csv-file 
    """

    def __init__(self, loaded_csv_df: pd.DataFrame, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.loaded_csv_file = loaded_csv_df

        self.init_ui()

    def init_ui(self) -> None:
        """Initialize the ui"""
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        self.brazzers_table_frame = BrazzersTableFrame(self.loaded_csv_file)
        self.brazzers_table_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.brazzers_table_frame.setLineWidth(10)
        layout.addWidget(self.brazzers_table_frame)

        #% Create a second QFrame for testing...
         # Prozentsatz für die Größe des zweiten Frames
        table_control_frame_percentage = 30

        #self.second_brazzers_table_frame = BrazzersTableFrame(self.loaded_csv_file)
        self.table_control_frame = TableControlFrame(self.loaded_csv_file)
        self.table_control_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.table_control_frame.setAlignment

       

        # self.second_brazzers_table_frame.setFrameShape(QFrame.VLine)
        layout.addWidget(self.table_control_frame)

        # Prozentsatz für die Größe des zweiten Frames festlegen
        layout.setStretch(0, 100 - table_control_frame_percentage)
        layout.setStretch(1, table_control_frame_percentage)

        self.setLayout(layout)

    

        
class BrazzersTableFrame(QFrame):
    """Frame to display the contents of the brazzers-sites and PS

    Args:
        distribution: Trying to adjust the contents of the frame with
        also for sites and ps and for zz_series respectively
    """
    def __init__(
        self, 
        loaded_csv_df: Optional[pd.DataFrame] = None,
        # distribution: pd.Series,
        # unique_anomaly_types: list[str],
        # unique_wall_thicknesses: list[str],
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)

        # self.distribution = distribution
        # self.unique_anomaly_types = unique_anomaly_types
        # self.unique_wall_thicknesses = unique_wall_thicknesses
        self.loaded_csv_df = loaded_csv_df
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize the ui.
        """

        # Reparent layout to create the new layout without any issues
        

        if self.layout():
            QWidget().setLayout(self.layout())

        layout = QVBoxLayout()

        brazzers_table_columns = ["Nr.", "Site", "PS1", "PS2", "PS3", 
                                  "Title", "PS4", "PS5", "PS6", "PS7", 
                                  "PS8", "PS9", "PS10", "loc", "link"]
        
        self.brazzers_table = QTableWidget()

        
        self.brazzers_table.setColumnCount(len(brazzers_table_columns) + 1)
        self.brazzers_table.setHorizontalHeaderLabels(brazzers_table_columns)
        self.fill_brazzers_table(self.loaded_csv_df)

        #% Define the function which his executed, when cell was clicked !
        self.brazzers_table.cellClicked.connect(self.cell_was_clicked)
        layout.addWidget(self.brazzers_table)

        self.test_label = QLabel("QLabel for testing")
        layout.addWidget(self.test_label)
        self.setLayout(layout)

        # for row_index, wall_thickness in enumerate(self.unique_wall_thicknesses):
        #     new_cell = QTableWidgetItem(str(wall_thickness))
        #     new_cell.setFlags(~Qt.ItemIsEditable) # make the cell content not editable
        #     self.brazzers_table.setItem(row_index, 0, new_cell)
        
    def fill_brazzers_table(self, selected_df: pd.DataFrame):
        self.brazzers_table.setRowCount(0)
        for rows, columns in selected_df.iterrows():
            rows = self.brazzers_table.rowCount()
            self.brazzers_table.insertRow(rows)
            for num, data in enumerate(columns):
                self.brazzers_table.setItem(rows, num, QTableWidgetItem(str(data)))
                if "_720p" in str(data):
                    # self.brazzers_table.item(rows, 0).setBackground(QColor(191, 141, 3))   
                    self.brazzers_table.item(rows, 0).setBackground(BLUEISH_COLOR)  
                 
    #% Define the function which his executed, when cell was clicked !
        self.brazzers_table.cellClicked.connect(self.cell_was_clicked)

    def cell_was_clicked(self, row, column):
        item = self.brazzers_table.item(row, 0)
        ### look at the second entry, because it is 0, python give the column!!

        self.ID_row = item.text()
        self.selected_file = self.loaded_csv_df.iloc[int(self.ID_row)]['Link']
        self.selected_site_for_picture = self.loaded_csv_df.iloc[int(self.ID_row)]['Site']
        self.selected_title = self.loaded_csv_df.iloc[int(self.ID_row)]['Title']
        print(f"self.selected_title: {self.selected_title}")
        # self.link_text.setText(self.selected_file)

class TableControlFrame(QFrame):
    """Frame to display the control elements, like buttons, labels etc
      of the brazzers-sites and PS """
    
    def __init__(
        self, 
        loaded_csv_df: Optional[pd.DataFrame] = None,
        # distribution: pd.Series,
        # unique_anomaly_types: list[str],
        # unique_wall_thicknesses: list[str],
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.brazzers_table_frame = BrazzersTableFrame(loaded_csv_df)
        self.loaded_csv_df = loaded_csv_df
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize the ui.
        """

        if self.layout():
            QWidget().setLayout(self.layout())

        #% ComboBoxes_layout
        
        layout = QVBoxLayout()
        # layout.setAlignment(Qt.AlignTop)

        site_layout = QHBoxLayout()
        site_label = QLabel("SITE: ")
        combobox_site = QComboBox()
        site_layout.addWidget(site_label)
        site_layout.addWidget(combobox_site)
        layout.addLayout(site_layout)


        self.brazzers_table_frame.fill_brazzers_table(self.loaded_csv_df)

        # site_layout.addSpacing(300)
        # self.site_layout.setAlignment(Qsortedt.AlignLeft)
        # self.site_label.setFont(QFont('Roboto', 13))
        # self.site_label.setStyleSheet("color: rgb(255,210,43);font-weight: bold;")
        # self.combobox_site = QComboBox()
        # self.combobox_site.setFixedWidth(335)
        
        # self.site_layout.addWidget(self.site_label)
        # self.site_layout.addWidget(self.combobox_site)

        # layout.addWidget(self.site_label)
        # layout.addWidget(self.combobox_site)
        self.setLayout(layout)



#% -----------------------------------------
class BrazzersZZSeriesOverview(QWidget):
    """Widget to visualize the Overview of Brazzers ZZ_Series.
        The general look is recreated in this file

    Args:
        loaded_csv_df: dataframe of the loaded csv-file 
    """
        
        








if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    
    if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
        app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, "AA_UseHighDpiPixmaps"):
        app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    
    _load_csv_file_automatically = True

    if _load_csv_file_automatically:
        print(f"Loading csv_file automatically: ..")
        _csv_file_path  = Path(
            r"/Users/joerg/repos/brazGUI/csv_data/df_final_19_06_23.csv"
        )
        _df = pd.read_csv(_csv_file_path)
    else:
        _df = None


    # app.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # QFontDatabase.addApplicationFont('Raleway-Regular.ttf')
    # frame = RuntimeStylesheets()
    # frame.main.show()
    
    # apply_stylesheet(app, theme='dark_teal.xml', invert_secondary=False, extra=extra)
    # window = BrazzersManualMainWindow()
    main_window = BrazzersManualMainWindow(loaded_csv_df=_df)
    main_window.show()
    sys.exit(app.exec_())
