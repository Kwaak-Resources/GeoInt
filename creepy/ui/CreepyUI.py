# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\creepy.ui'
#
# Created: Mon Dec 16 19:18:52 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CreepyMainWindow(object):
    def setupUi(self, CreepyMainWindow):
        CreepyMainWindow.setObjectName(_fromUtf8("CreepyMainWindow"))
        CreepyMainWindow.resize(1483, 719)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreepyMainWindow.sizePolicy().hasHeightForWidth())
        CreepyMainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../creepy/include/creepy.xpm")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CreepyMainWindow.setWindowIcon(icon)
        CreepyMainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(CreepyMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.centralStackedWidget = QtGui.QStackedWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralStackedWidget.sizePolicy().hasHeightForWidth())
        self.centralStackedWidget.setSizePolicy(sizePolicy)
        self.centralStackedWidget.setAutoFillBackground(True)
        self.centralStackedWidget.setObjectName(_fromUtf8("centralStackedWidget"))
        self.mapPage = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapPage.sizePolicy().hasHeightForWidth())
        self.mapPage.setSizePolicy(sizePolicy)
        self.mapPage.setObjectName(_fromUtf8("mapPage"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.mapPage)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.mapWebView = QtWebKit.QWebView(self.mapPage)
        self.mapWebView.setAutoFillBackground(True)
        self.mapWebView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.mapWebView.setObjectName(_fromUtf8("mapWebView"))
        self.verticalLayout_4.addWidget(self.mapWebView)
        self.centralStackedWidget.addWidget(self.mapPage)
        self.analysisPage = QtGui.QWidget()
        self.analysisPage.setObjectName(_fromUtf8("analysisPage"))
        self.centralStackedWidget.addWidget(self.analysisPage)
        self.verticalLayout_2.addWidget(self.centralStackedWidget)
        CreepyMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CreepyMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1483, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuCreepy = QtGui.QMenu(self.menubar)
        self.menuCreepy.setObjectName(_fromUtf8("menuCreepy"))
        self.menuNewProject = QtGui.QMenu(self.menuCreepy)
        self.menuNewProject.setObjectName(_fromUtf8("menuNewProject"))
        self.menuExport = QtGui.QMenu(self.menuCreepy)
        self.menuExport.setObjectName(_fromUtf8("menuExport"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuFilters = QtGui.QMenu(self.menubar)
        self.menuFilters.setObjectName(_fromUtf8("menuFilters"))
        CreepyMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CreepyMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CreepyMainWindow.setStatusBar(self.statusbar)
        self.dockWLocationsList = QtGui.QDockWidget(CreepyMainWindow)
        self.dockWLocationsList.setMinimumSize(QtCore.QSize(250, 127))
        self.dockWLocationsList.setObjectName(_fromUtf8("dockWLocationsList"))
        self.dockWLocationsListContents = QtGui.QWidget()
        self.dockWLocationsListContents.setObjectName(_fromUtf8("dockWLocationsListContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWLocationsListContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.locationsTableView = QtGui.QTableView(self.dockWLocationsListContents)
        self.locationsTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.locationsTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.locationsTableView.setObjectName(_fromUtf8("locationsTableView"))
        self.locationsTableView.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.locationsTableView)
        self.dockWLocationsList.setWidget(self.dockWLocationsListContents)
        CreepyMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWLocationsList)
        self.dockWProjects = QtGui.QDockWidget(CreepyMainWindow)
        self.dockWProjects.setMinimumSize(QtCore.QSize(200, 300))
        self.dockWProjects.setObjectName(_fromUtf8("dockWProjects"))
        self.dockWProjectsContents = QtGui.QWidget()
        self.dockWProjectsContents.setObjectName(_fromUtf8("dockWProjectsContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWProjectsContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.treeViewProjects = QtGui.QTreeView(self.dockWProjectsContents)
        self.treeViewProjects.setObjectName(_fromUtf8("treeViewProjects"))
        self.verticalLayout_3.addWidget(self.treeViewProjects)
        self.dockWProjects.setWidget(self.dockWProjectsContents)
        CreepyMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWProjects)
        self.dockWCurrentLocationDetails = QtGui.QDockWidget(CreepyMainWindow)
        self.dockWCurrentLocationDetails.setObjectName(_fromUtf8("dockWCurrentLocationDetails"))
        self.dockWCurrentTargetDetailsContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWCurrentTargetDetailsContents.sizePolicy().hasHeightForWidth())
        self.dockWCurrentTargetDetailsContents.setSizePolicy(sizePolicy)
        self.dockWCurrentTargetDetailsContents.setObjectName(_fromUtf8("dockWCurrentTargetDetailsContents"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.dockWCurrentTargetDetailsContents)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.currentTargetDetailsDetailsDateLabel = QtGui.QLabel(self.dockWCurrentTargetDetailsContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTargetDetailsDetailsDateLabel.sizePolicy().hasHeightForWidth())
        self.currentTargetDetailsDetailsDateLabel.setSizePolicy(sizePolicy)
        self.currentTargetDetailsDetailsDateLabel.setTextFormat(QtCore.Qt.RichText)
        self.currentTargetDetailsDetailsDateLabel.setObjectName(_fromUtf8("currentTargetDetailsDetailsDateLabel"))
        self.horizontalLayout_2.addWidget(self.currentTargetDetailsDetailsDateLabel)
        self.currentTargetDetailsDateValue = QtGui.QLabel(self.dockWCurrentTargetDetailsContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTargetDetailsDateValue.sizePolicy().hasHeightForWidth())
        self.currentTargetDetailsDateValue.setSizePolicy(sizePolicy)
        self.currentTargetDetailsDateValue.setText(_fromUtf8(""))
        self.currentTargetDetailsDateValue.setObjectName(_fromUtf8("currentTargetDetailsDateValue"))
        self.horizontalLayout_2.addWidget(self.currentTargetDetailsDateValue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.currentTargetDetailsLocationLabel = QtGui.QLabel(self.dockWCurrentTargetDetailsContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTargetDetailsLocationLabel.sizePolicy().hasHeightForWidth())
        self.currentTargetDetailsLocationLabel.setSizePolicy(sizePolicy)
        self.currentTargetDetailsLocationLabel.setObjectName(_fromUtf8("currentTargetDetailsLocationLabel"))
        self.horizontalLayout_3.addWidget(self.currentTargetDetailsLocationLabel)
        self.currentTargetDetailsLocationValue = QtGui.QLabel(self.dockWCurrentTargetDetailsContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTargetDetailsLocationValue.sizePolicy().hasHeightForWidth())
        self.currentTargetDetailsLocationValue.setSizePolicy(sizePolicy)
        self.currentTargetDetailsLocationValue.setText(_fromUtf8(""))
        self.currentTargetDetailsLocationValue.setObjectName(_fromUtf8("currentTargetDetailsLocationValue"))
        self.horizontalLayout_3.addWidget(self.currentTargetDetailsLocationValue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.currentTargetDetailsSourceLabel = QtGui.QLabel(self.dockWCurrentTargetDetailsContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTargetDetailsSourceLabel.sizePolicy().hasHeightForWidth())
        self.currentTargetDetailsSourceLabel.setSizePolicy(sizePolicy)
        self.currentTargetDetailsSourceLabel.setObjectName(_fromUtf8("currentTargetDetailsSourceLabel"))
        self.horizontalLayout_4.addWidget(self.currentTargetDetailsSourceLabel)
        self.currentTargetDetailsSourceValue = QtGui.QLabel(self.dockWCurrentTargetDetailsContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTargetDetailsSourceValue.sizePolicy().hasHeightForWidth())
        self.currentTargetDetailsSourceValue.setSizePolicy(sizePolicy)
        self.currentTargetDetailsSourceValue.setText(_fromUtf8(""))
        self.currentTargetDetailsSourceValue.setObjectName(_fromUtf8("currentTargetDetailsSourceValue"))
        self.horizontalLayout_4.addWidget(self.currentTargetDetailsSourceValue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.currentTargetDetailsContextLabel = QtGui.QLabel(self.dockWCurrentTargetDetailsContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTargetDetailsContextLabel.sizePolicy().hasHeightForWidth())
        self.currentTargetDetailsContextLabel.setSizePolicy(sizePolicy)
        self.currentTargetDetailsContextLabel.setObjectName(_fromUtf8("currentTargetDetailsContextLabel"))
        self.horizontalLayout_5.addWidget(self.currentTargetDetailsContextLabel)
        self.currentTargetDetailsContextValue = QtGui.QLabel(self.dockWCurrentTargetDetailsContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTargetDetailsContextValue.sizePolicy().hasHeightForWidth())
        self.currentTargetDetailsContextValue.setSizePolicy(sizePolicy)
        self.currentTargetDetailsContextValue.setText(_fromUtf8(""))
        self.currentTargetDetailsContextValue.setTextFormat(QtCore.Qt.RichText)
        self.currentTargetDetailsContextValue.setWordWrap(True)
        self.currentTargetDetailsContextValue.setOpenExternalLinks(True)
        self.currentTargetDetailsContextValue.setObjectName(_fromUtf8("currentTargetDetailsContextValue"))
        self.horizontalLayout_5.addWidget(self.currentTargetDetailsContextValue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.dockWCurrentLocationDetails.setWidget(self.dockWCurrentTargetDetailsContents)
        CreepyMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWCurrentLocationDetails)
        self.mainToolbar = QtGui.QToolBar(CreepyMainWindow)
        self.mainToolbar.setObjectName(_fromUtf8("mainToolbar"))
        CreepyMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolbar)
        CreepyMainWindow.insertToolBarBreak(self.mainToolbar)
        self.locationsActionsToolbar = QtGui.QToolBar(CreepyMainWindow)
        self.locationsActionsToolbar.setObjectName(_fromUtf8("locationsActionsToolbar"))
        CreepyMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.locationsActionsToolbar)
        self.actionExportKML = QtGui.QAction(CreepyMainWindow)
        self.actionExportKML.setCheckable(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/020 DocumentKML.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExportKML.setIcon(icon1)
        self.actionExportKML.setObjectName(_fromUtf8("actionExportKML"))
        self.actionExportCSV = QtGui.QAction(CreepyMainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/020 DocumentCSV.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExportCSV.setIcon(icon2)
        self.actionExportCSV.setObjectName(_fromUtf8("actionExportCSV"))
        self.actionExit = QtGui.QAction(CreepyMainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/059 CircledOff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionReportProblem = QtGui.QAction(CreepyMainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/107 Flag.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReportProblem.setIcon(icon4)
        self.actionReportProblem.setObjectName(_fromUtf8("actionReportProblem"))
        self.actionAbout = QtGui.QAction(CreepyMainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/creepy32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon5)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionPluginsConfiguration = QtGui.QAction(CreepyMainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/054 Preferences2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPluginsConfiguration.setIcon(icon6)
        self.actionPluginsConfiguration.setObjectName(_fromUtf8("actionPluginsConfiguration"))
        self.actionLocations_List = QtGui.QAction(CreepyMainWindow)
        self.actionLocations_List.setCheckable(True)
        self.actionLocations_List.setChecked(True)
        self.actionLocations_List.setSoftKeyRole(QtGui.QAction.NoSoftKey)
        self.actionLocations_List.setObjectName(_fromUtf8("actionLocations_List"))
        self.actionResult_Details = QtGui.QAction(CreepyMainWindow)
        self.actionResult_Details.setCheckable(True)
        self.actionResult_Details.setChecked(True)
        self.actionResult_Details.setObjectName(_fromUtf8("actionResult_Details"))
        self.actionAvailable_Plugins = QtGui.QAction(CreepyMainWindow)
        self.actionAvailable_Plugins.setCheckable(True)
        self.actionAvailable_Plugins.setChecked(True)
        self.actionAvailable_Plugins.setObjectName(_fromUtf8("actionAvailable_Plugins"))
        self.actionSettings = QtGui.QAction(CreepyMainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionNewPersonProject = QtGui.QAction(CreepyMainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/003 User2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewPersonProject.setIcon(icon7)
        self.actionNewPersonProject.setObjectName(_fromUtf8("actionNewPersonProject"))
        self.actionNewLocationBasedProject = QtGui.QAction(CreepyMainWindow)
        self.actionNewLocationBasedProject.setObjectName(_fromUtf8("actionNewLocationBasedProject"))
        self.actionAnalyzeCurrentProject = QtGui.QAction(CreepyMainWindow)
        self.actionAnalyzeCurrentProject.setIcon(icon5)
        self.actionAnalyzeCurrentProject.setObjectName(_fromUtf8("actionAnalyzeCurrentProject"))
        self.actionDrawCurrentProject = QtGui.QAction(CreepyMainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/079 Pin2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDrawCurrentProject.setIcon(icon8)
        self.actionDrawCurrentProject.setObjectName(_fromUtf8("actionDrawCurrentProject"))
        self.actionFilterLocationsDate = QtGui.QAction(CreepyMainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/005 CalendarDate.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterLocationsDate.setIcon(icon9)
        self.actionFilterLocationsDate.setObjectName(_fromUtf8("actionFilterLocationsDate"))
        self.actionFilterLocationsPosition = QtGui.QAction(CreepyMainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/226 CircledGeo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterLocationsPosition.setIcon(icon10)
        self.actionFilterLocationsPosition.setObjectName(_fromUtf8("actionFilterLocationsPosition"))
        self.actionRemoveFilters = QtGui.QAction(CreepyMainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/070 Minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveFilters.setIcon(icon11)
        self.actionRemoveFilters.setObjectName(_fromUtf8("actionRemoveFilters"))
        self.actionShowHeatMap = QtGui.QAction(CreepyMainWindow)
        self.actionShowHeatMap.setCheckable(True)
        self.actionShowHeatMap.setIcon(icon4)
        self.actionShowHeatMap.setObjectName(_fromUtf8("actionShowHeatMap"))
        self.actionLocation_Actions = QtGui.QAction(CreepyMainWindow)
        self.actionLocation_Actions.setObjectName(_fromUtf8("actionLocation_Actions"))
        self.actionMain_Toolbar = QtGui.QAction(CreepyMainWindow)
        self.actionMain_Toolbar.setObjectName(_fromUtf8("actionMain_Toolbar"))
        self.actionDeleteCurrentProject = QtGui.QAction(CreepyMainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/cr/200 CircledMinus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteCurrentProject.setIcon(icon12)
        self.actionDeleteCurrentProject.setObjectName(_fromUtf8("actionDeleteCurrentProject"))
        self.actionExportFilteredKML = QtGui.QAction(CreepyMainWindow)
        self.actionExportFilteredKML.setIcon(icon1)
        self.actionExportFilteredKML.setObjectName(_fromUtf8("actionExportFilteredKML"))
        self.actionExportFilteredCSV = QtGui.QAction(CreepyMainWindow)
        self.actionExportFilteredCSV.setIcon(icon2)
        self.actionExportFilteredCSV.setObjectName(_fromUtf8("actionExportFilteredCSV"))
        self.menuNewProject.addAction(self.actionNewPersonProject)
        self.menuExport.addAction(self.actionExportKML)
        self.menuExport.addAction(self.actionExportCSV)
        self.menuExport.addAction(self.actionExportFilteredKML)
        self.menuExport.addAction(self.actionExportFilteredCSV)
        self.menuCreepy.addAction(self.menuNewProject.menuAction())
        self.menuCreepy.addAction(self.menuExport.menuAction())
        self.menuCreepy.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionPluginsConfiguration)
        self.menuAbout.addAction(self.actionReportProblem)
        self.menuAbout.addAction(self.actionAbout)
        self.menuView.addSeparator()
        self.menuFilters.addAction(self.actionFilterLocationsDate)
        self.menuFilters.addAction(self.actionFilterLocationsPosition)
        self.menuFilters.addAction(self.actionRemoveFilters)
        self.menubar.addAction(self.menuCreepy.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuFilters.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.mainToolbar.addAction(self.actionNewPersonProject)
        self.mainToolbar.addAction(self.actionPluginsConfiguration)
        self.mainToolbar.addAction(self.actionAnalyzeCurrentProject)
        self.mainToolbar.addAction(self.actionDrawCurrentProject)
        self.mainToolbar.addAction(self.actionExportKML)
        self.mainToolbar.addAction(self.actionExportCSV)
        self.mainToolbar.addSeparator()
        self.locationsActionsToolbar.addAction(self.actionFilterLocationsDate)
        self.locationsActionsToolbar.addAction(self.actionFilterLocationsPosition)
        self.locationsActionsToolbar.addAction(self.actionShowHeatMap)
        self.locationsActionsToolbar.addAction(self.actionRemoveFilters)

        self.retranslateUi(CreepyMainWindow)
        self.centralStackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("activated()")), CreepyMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(CreepyMainWindow)

    def retranslateUi(self, CreepyMainWindow):
        CreepyMainWindow.setWindowTitle(QtGui.QApplication.translate("CreepyMainWindow", "cree.py - Geolocation OSINT tool", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCreepy.setTitle(QtGui.QApplication.translate("CreepyMainWindow", "Creepy", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNewProject.setTitle(QtGui.QApplication.translate("CreepyMainWindow", "New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExport.setTitle(QtGui.QApplication.translate("CreepyMainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("CreepyMainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("CreepyMainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("CreepyMainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFilters.setTitle(QtGui.QApplication.translate("CreepyMainWindow", "Filters", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWLocationsList.setWindowTitle(QtGui.QApplication.translate("CreepyMainWindow", "Locations List", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWProjects.setWindowTitle(QtGui.QApplication.translate("CreepyMainWindow", "Target Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWCurrentLocationDetails.setWindowTitle(QtGui.QApplication.translate("CreepyMainWindow", "Current Location Details", None, QtGui.QApplication.UnicodeUTF8))
        self.currentTargetDetailsDetailsDateLabel.setText(QtGui.QApplication.translate("CreepyMainWindow", "<b>Date:       </b>        ", None, QtGui.QApplication.UnicodeUTF8))
        self.currentTargetDetailsLocationLabel.setText(QtGui.QApplication.translate("CreepyMainWindow", "<b>Location: </b>", None, QtGui.QApplication.UnicodeUTF8))
        self.currentTargetDetailsSourceLabel.setText(QtGui.QApplication.translate("CreepyMainWindow", "<b>From:       <b>", None, QtGui.QApplication.UnicodeUTF8))
        self.currentTargetDetailsContextLabel.setText(QtGui.QApplication.translate("CreepyMainWindow", "<b>Context:  <b>", None, QtGui.QApplication.UnicodeUTF8))
        self.mainToolbar.setWindowTitle(QtGui.QApplication.translate("CreepyMainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.locationsActionsToolbar.setWindowTitle(QtGui.QApplication.translate("CreepyMainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportKML.setText(QtGui.QApplication.translate("CreepyMainWindow", "Export Project Locations as KML", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportKML.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "Export project locations in KML format", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportCSV.setText(QtGui.QApplication.translate("CreepyMainWindow", "Export Project Locations as CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportCSV.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "Export project locations in CSV format", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("CreepyMainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReportProblem.setText(QtGui.QApplication.translate("CreepyMainWindow", "Report a problem / bug", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("CreepyMainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPluginsConfiguration.setText(QtGui.QApplication.translate("CreepyMainWindow", "Plugins Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLocations_List.setText(QtGui.QApplication.translate("CreepyMainWindow", "Locations List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionResult_Details.setText(QtGui.QApplication.translate("CreepyMainWindow", "Result Details", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAvailable_Plugins.setText(QtGui.QApplication.translate("CreepyMainWindow", "Available Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("CreepyMainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewPersonProject.setText(QtGui.QApplication.translate("CreepyMainWindow", "Person Based Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewLocationBasedProject.setText(QtGui.QApplication.translate("CreepyMainWindow", "Location Based Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnalyzeCurrentProject.setText(QtGui.QApplication.translate("CreepyMainWindow", "Analyze Current Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnalyzeCurrentProject.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "Analyze Current Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDrawCurrentProject.setText(QtGui.QApplication.translate("CreepyMainWindow", "Draw Locations for Current Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDrawCurrentProject.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "Draw Locations for the currently selected project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterLocationsDate.setText(QtGui.QApplication.translate("CreepyMainWindow", "Filter Locations by Date", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterLocationsDate.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "<html><head/><body><p>You can filter the retrieved locations from a project based on a date range within which they have been created</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterLocationsPosition.setText(QtGui.QApplication.translate("CreepyMainWindow", "Filter Locations by Position", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilterLocationsPosition.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "<html><head/><body><p>You can filter the retrieved locations based on their distance from a given point in the map</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveFilters.setText(QtGui.QApplication.translate("CreepyMainWindow", "Remove Filters", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveFilters.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "<html><head/><body><p>Remove all the filters on date and locations and show all the retreived locations on the map</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowHeatMap.setText(QtGui.QApplication.translate("CreepyMainWindow", "Show HeatMap", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowHeatMap.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "<html><head/><body><p>Show a heatmap with the selected locations instead of pointers.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLocation_Actions.setText(QtGui.QApplication.translate("CreepyMainWindow", "Location Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMain_Toolbar.setText(QtGui.QApplication.translate("CreepyMainWindow", "Main Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteCurrentProject.setText(QtGui.QApplication.translate("CreepyMainWindow", "Delete Current Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteCurrentProject.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "Delete this project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportFilteredKML.setText(QtGui.QApplication.translate("CreepyMainWindow", "Export Filtered Locations as KML", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportFilteredKML.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "Export  currently visible locations as a KML file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportFilteredCSV.setText(QtGui.QApplication.translate("CreepyMainWindow", "Export Filtered Locations as CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportFilteredCSV.setToolTip(QtGui.QApplication.translate("CreepyMainWindow", "Export currently visible locations as CSV", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
import creepy_resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CreepyMainWindow = QtGui.QMainWindow()
    ui = Ui_CreepyMainWindow()
    ui.setupUi(CreepyMainWindow)
    CreepyMainWindow.show()
    sys.exit(app.exec_())

