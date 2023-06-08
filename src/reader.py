# import sys
import time
import os
from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox, QToolButton,
                             QSplitter, QVBoxLayout, QHBoxLayout, QLabel,
                             QTableWidget, QTableWidgetItem, QAbstractItemView,
                             QLineEdit, QFileDialog, QMessageBox, QComboBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
from src import database
# from src import reader_information
# from src import book_information
# import database
# import reader_information
# import book_information


class readerPage(QWidget):

    def __init__(self, info):
        super().__init__()
        self.info = info
        self.focus = 0
        self.initUI()

    def initUI(self):
        # 标题栏
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1250, 50)
        self.setTitleBar()

        # 分割
        self.body = QSplitter()
        self.setLeftMunu()
        self.content = None
        self.setContent()

        self.bodyLayout = QGridLayout()
        self.bodyLayout.addWidget(self.titleBar, 0, 0, 1, 7)
        self.bodyLayout.addWidget(self.body, 1, 0, 7, 7)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.bodyLayout)
        self.setFixedSize(1280, 720)
        self.setMyStyle()

    # 设置标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('图书馆管理系统--读者页面')
        self.title.setFixedHeight(30)

        self.account = QToolButton()
        # self.account.setIcon(QIcon('icon/person.png'))
        self.account.setText(self.info['ID'])
        self.account.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.account.setFixedHeight(20)
        self.account.setEnabled(False)

        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFixedHeight(30)

        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(100)
        titleLayout.addWidget(self.title)
        titleLayout.addWidget(self.account)
        titleLayout.addWidget(self.out)
        self.titleBar.setLayout(titleLayout)

    # 左侧菜单栏
    def setLeftMunu(self):
        # 书籍管理
        self.bookManage = QToolButton()
        self.bookManage.setText('书籍查询')
        self.bookManage.setFixedSize(160, 50)
        self.bookManage.setIcon(QIcon('icon/book.png'))
        self.bookManage.setIconSize(QSize(30, 30))
        self.bookManage.clicked.connect(
            lambda: self.switch(0, self.bookManage))
        self.bookManage.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 读者管理
        self.userManage = QToolButton()
        self.userManage.setText('借阅信息')
        self.userManage.setFixedSize(160, 50)
        self.userManage.setIcon(QIcon('icon/detial.png'))
        self.userManage.setIconSize(QSize(30, 30))
        self.userManage.clicked.connect(
            lambda: self.switch(1, self.userManage))
        self.userManage.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 借阅日志
        self.history = QToolButton()
        self.history.setText('借阅历史')
        self.history.setFixedSize(160, 50)
        self.history.setIcon(QIcon('icon/history.png'))
        self.history.setIconSize(QSize(30, 30))
        self.history.clicked.connect(lambda: self.switch(2, self.history))
        self.history.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 借阅信息管理
        self.borrowManage = QToolButton()
        self.borrowManage.setText('个人信息')
        self.borrowManage.setFixedSize(160, 50)
        self.borrowManage.setIcon(QIcon('icon/borrowing.png'))
        self.borrowManage.setIconSize(QSize(30, 30))
        self.borrowManage.clicked.connect(
            lambda: self.switch(3, self.borrowManage))
        self.borrowManage.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.btnList = [
            self.bookManage, self.userManage, self.history, self.borrowManage
        ]

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.bookManage)
        self.layout.addWidget(self.userManage)
        self.layout.addWidget(self.history)
        self.layout.addWidget(self.borrowManage)
        self.layout.addStretch()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.menu = QGroupBox()
        self.menu.setFixedSize(160, 500)
        self.menu.setLayout(self.layout)
        self.menu.setContentsMargins(0, 0, 0, 0)
        self.body.addWidget(self.menu)

    def switch(self, index, btn):
        self.focus = index
        # for i in self.btnList:
        #     i.setStyleSheet('''
        #     *{
        #         background: white;
        #     }
        #     QToolButton:hover{
        #         background-color: rgba(230, 230, 230, 0.3);
        #     }
        #     ''')

        # btn.setStyleSheet('''
        # QToolButton{
        #     background-color: rgba(230, 230, 230, 0.7);
        # }
        # ''')
        self.setContent()

    # 设置右侧信息页
    def setContent(self):
        if self.content is not None:
            self.content.deleteLater()
        if self.focus == 0:
            self.content = BookSearch()
        elif self.focus == 1:
            self.content = ReaderManage()
        elif self.focus == 2:
            self.content = HistoryManage()
        else:
            self.content = BorrowManage()
        self.body.addWidget(self.content)

    def setMyStyle(self):
        pass
        # self.setStyleSheet('''
        # QWidget{
        #     background-color: white;
        # }
        # ''')
        # self.titleBar.setStyleSheet('''
        # QWidget{
        #     background-color: rgba(44,44,44,1);
        #     border:1px solid black;
        #     border-radius: 10px;
        # }
        # ''')
        # self.menu.setStyleSheet('''
        # QWidget{
        #     border: 0px;
        #     border-right: 1px solid rgba(227, 227, 227, 1);
        # }
        # QToolButton{
        #     color: rgba(51, 90, 129, 1);
        #     font-family: 微软雅黑;
        #     font-size: 25px;
        #     border-right: 1px solid rgba(227, 227, 227, 1);
        # }
        # QToolButton:hover{
        #     background-color: rgba(230, 230, 230, 0.3);
        # }
        # ''')
        # self.title.setStyleSheet('''
        # *{
        #     color: white;
        #     font-family: 微软雅黑;
        #     font-size: 25px;
        #     border: 0px;
        # }
        # ''')
        # self.account.setStyleSheet('''
        # *{
        #     color: white;
        #     font-weight: 微软雅黑;
        #     font-size: 25px;
        #     border: 0px;
        # }
        # ''')
        # self.out.setStyleSheet('''
        # QToolButton{
        #     color: white;
        #     border:0px;
        #     font-size: 12px;
        # }
        # QToolButton:hover{
        #     color: rgba(11, 145, 255, 1);
        # }
        # ''')


# 书籍查询
class BookSearch(QGroupBox):

    def __init__(self):
        super().__init__()
        self.book_list = []
        self.body = QVBoxLayout()
        self.table = None
        self.setTitleBar()
        self.setSearchBar()
        self.searchFunction()

        self.setLayout(self.body)
        self.initUI()

    # 标题栏
    def setTitleBar(self):
        pass

    # 设置搜索框
    def setSearchBar(self):
        self.selectBox = QComboBox()
        self.selectBox.addItems(['书号', '作者', '书名'])
        self.selectBox.setFixedHeight(30)
        self.searchTitle = QLabel()
        self.searchTitle.setText('搜索书籍')
        self.searchInput = QLineEdit()
        self.searchInput.setText('')
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setFixedSize(400, 40)
        self.searchButton = QToolButton()
        self.searchButton.setFixedSize(100, 40)
        self.searchButton.setText('搜索')
        self.searchButton.clicked.connect(self.searchFunction)
        self.addNewBookButton = QToolButton()
        self.addNewBookButton.setFixedSize(120, 40)
        self.addNewBookButton.setText('新增书籍')
        self.addNewBookButton.clicked.connect(self.addNewBookFunction)
        searchLayout = QHBoxLayout()
        searchLayout.addStretch()
        searchLayout.addWidget(self.selectBox)
        searchLayout.addWidget(self.searchTitle)
        searchLayout.addWidget(self.searchInput)
        searchLayout.addWidget(self.searchButton)
        searchLayout.addWidget(self.addNewBookButton)
        searchLayout.addStretch()
        self.searchWidget = QWidget()
        self.searchWidget.setLayout(searchLayout)
        self.body.addWidget(self.searchWidget)

    # 搜索方法
    def searchFunction(self):
        convert = {'书号': 'ID', '作者': 'author', '书名': 'name', '': 'name'}
        self.book_list = database.search_book(
            self.searchInput.text(), convert[self.selectBox.currentText()])
        if self.book_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.setTable()

    # 设置表格
    def setTable(self):
        self.table = QTableWidget(1, 7)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setColumnWidth(0, 80)
        self.table.setColumnWidth(7, 85)

        self.table.setItem(0, 0, QTableWidgetItem('书号'))
        self.table.setItem(0, 1, QTableWidgetItem('书名'))
        self.table.setItem(0, 2, QTableWidgetItem('作者'))
        self.table.setItem(0, 3, QTableWidgetItem('价格'))
        self.table.setItem(0, 4, QTableWidgetItem('状态'))
        self.table.setItem(0, 5, QTableWidgetItem('借阅数'))
        self.table.setItem(0, 6, QTableWidgetItem('管理'))
        for i in range(7):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('微软雅黑', 15))

        # 显示借阅详情
        for i in self.book_list:
            self.insertRow(i)
        self.body.addWidget(self.table)

    # 插入行
    def insertRow(self, val: list):
        print(val)
        itemBID = QTableWidgetItem(val[0])
        itemBID.setTextAlignment(Qt.AlignCenter)

        itemNAME = QTableWidgetItem('《' + val[1] + '》')
        itemNAME.setTextAlignment(Qt.AlignCenter)

        itemAUTHOR = QTableWidgetItem(val[2])
        itemAUTHOR.setTextAlignment(Qt.AlignCenter)

        itemPRICE = QTableWidgetItem(str(val[3]))
        itemPRICE.setTextAlignment(Qt.AlignCenter)

        itemSTATUS = QTableWidgetItem(str(val[4]))
        itemSTATUS.setTextAlignment(Qt.AlignCenter)

        itemSUM = QTableWidgetItem(str(val[5]))
        itemSUM.setTextAlignment(Qt.AlignCenter)

        itemModify = QToolButton(self.table)
        itemModify.setFixedSize(75, 25)
        itemModify.setText('修改')
        itemModify.clicked.connect(lambda: self.updateBookFunction(val[0]))
        itemDelete = QToolButton(self.table)
        itemDelete.setFixedSize(75, 25)
        itemDelete.setText('删除')
        itemDelete.clicked.connect(lambda: self.deleteBookFunction(val[0]))

        itemLayout = QHBoxLayout()
        itemLayout.setContentsMargins(0, 0, 0, 0)
        itemLayout.addWidget(itemModify)
        itemLayout.addWidget(itemDelete)
        itemWidget = QWidget()
        itemWidget.setLayout(itemLayout)

        self.table.insertRow(1)
        self.table.setItem(1, 0, itemBID)
        self.table.setItem(1, 1, itemNAME)
        self.table.setItem(1, 2, itemAUTHOR)
        self.table.setItem(1, 3, itemPRICE)
        self.table.setItem(1, 4, itemSTATUS)
        self.table.setItem(1, 5, itemSUM)

        self.table.setCellWidget(1, 6, itemWidget)

    def updateBookFunction(self, BID: str):
        book_info = database.get_book_info(BID)
        if book_info is None:
            return
        self.sum = book_info['BORROW_TIMES']
        self.updateBookDialog = book_information.BookInfo(book_info)
        self.updateBookDialog.after_close.connect(self.updateBook)
        self.updateBookDialog.show()

    def updateBook(self, book_info: dict):
        change = self.sum - book_info['SUM']
        # 书本减少的数量不能大于未借出的书本数
        if change > book_info['NUM']:
            book_info['SUM'] = self.sum - book_info['NUM']
            book_info['NUM'] = 0
        else:
            book_info['NUM'] -= change
        ans = database.update_book(book_info)
        if ans:
            self.searchFunction()

    def addNewBookFunction(self):
        self.newBookDialog = book_information.BookInfo()
        self.newBookDialog.show()
        self.newBookDialog.after_close.connect(self.addNewBook)

    def addNewBook(self, book_info: dict):
        ans = database.new_book(book_info)
        if ans:
            self.searchFunction()

    def deleteBookFunction(self, BID: str):
        msgBox = QMessageBox(QMessageBox.Warning, "警告!", '您将会永久删除这本书以及相关信息!',
                             QMessageBox.NoButton, self)
        msgBox.addButton("确认", QMessageBox.AcceptRole)
        msgBox.addButton("取消", QMessageBox.RejectRole)
        if msgBox.exec_() == QMessageBox.AcceptRole:
            ans = database.delete_book(BID)
            if ans:
                self.searchFunction()

    def initUI(self):
        self.setFixedSize(1100, 600)


class ReaderManage(QWidget):

    def __init__(self):
        super().__init__()
        self.book_list = []
        self.body = QVBoxLayout()
        self.table = None
        self.setTitleBar()
        self.setSearchBar()
        self.searchFunction()

        self.setLayout(self.body)
        self.initUI()

    # 标题栏
    def setTitleBar(self):
        pass
        # self.title = QLabel()
        # self.title.setText('读者信息管理')
        # self.title.setFixedHeight(25)
        # titleLayout = QHBoxLayout()
        # titleLayout.addSpacing(50)
        # titleLayout.addWidget(self.title)
        # self.titleBar = QWidget()
        # self.titleBar.setFixedSize(880, 50)
        # self.titleBar.setLayout(titleLayout)
        # self.body.addWidget(self.titleBar)

    # 设置搜索框
    def setSearchBar(self):
        self.searchTitle = QLabel()
        self.searchTitle.setText('搜索读者')
        self.searchInput = QLineEdit()
        self.searchInput.setText('ID/姓名')
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setFixedSize(400, 40)
        self.searchButton = QToolButton()
        self.searchButton.setFixedSize(100, 40)
        self.searchButton.setText('搜索')
        self.searchButton.clicked.connect(self.searchFunction)

        searchLayout = QHBoxLayout()
        searchLayout.addStretch()
        searchLayout.addWidget(self.searchTitle)
        searchLayout.addWidget(self.searchInput)
        searchLayout.addWidget(self.searchButton)
        searchLayout.addStretch()

        self.searchWidget = QWidget()
        self.searchWidget.setLayout(searchLayout)
        self.body.addWidget(self.searchWidget)

    # 搜索方法
    def searchFunction(self):
        self.stu_list = database.search_reader(self.searchInput.text())
        if self.stu_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.setTable()

    # 设置表格
    def setTable(self):
        self.table = QTableWidget(1, 6)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)

        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 175)
        self.table.setColumnWidth(4, 175)
        self.table.setColumnWidth(5, 120)

        self.table.setItem(0, 0, QTableWidgetItem('学号'))
        self.table.setItem(0, 1, QTableWidgetItem('姓名'))
        self.table.setItem(0, 2, QTableWidgetItem('邮箱'))
        # self.table.setItem(0, 3, QTableWidgetItem('专业'))
        # self.table.setItem(0, 4, QTableWidgetItem('最大借书数'))
        self.table.setItem(0, 3, QTableWidgetItem('操作'))

        for i in range(4):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('微软雅黑', 15))

        # 显示借阅详情
        for i in self.stu_list:
            self.insertRow(i)
        self.body.addWidget(self.table)

    # 插入行
    def insertRow(self, val: list):
        itemSID = QTableWidgetItem(val[0])
        itemSID.setTextAlignment(Qt.AlignCenter)

        itemNAME = QTableWidgetItem(val[1])
        itemNAME.setTextAlignment(Qt.AlignCenter)

        itemEMAIL = QTableWidgetItem(val[2])
        itemEMAIL.setTextAlignment(Qt.AlignCenter)

        itemModify = QToolButton(self.table)
        itemModify.setFixedSize(85, 25)
        itemModify.setText('修改')
        itemModify.clicked.connect(lambda: self.updatereaderFunction(val[0]))

        itemDelete = QToolButton(self.table)
        itemDelete.setFixedSize(85, 25)
        itemDelete.setText('删除')
        itemDelete.clicked.connect(lambda: self.deletereaderFunction(val[0]))

        itemLayout = QHBoxLayout()
        itemLayout.setContentsMargins(0, 0, 0, 0)
        itemLayout.addWidget(itemModify)
        itemLayout.addWidget(itemDelete)
        itemWidget = QWidget()
        itemWidget.setLayout(itemLayout)

        self.table.insertRow(1)
        self.table.setItem(1, 0, itemSID)
        self.table.setItem(1, 1, itemNAME)
        self.table.setItem(1, 2, itemEMAIL)
        self.table.setCellWidget(1, 3, itemWidget)

    def updatereaderFunction(self, SID: str):
        stu_info = database.get_reader_info(SID)
        if stu_info is None:
            return
        self.updatereaderDialog = reader_information.readerInfo(stu_info)
        self.updatereaderDialog.after_close.connect(self.updatereader)
        self.updatereaderDialog.show()

    def updatereader(self, stu_info: dict):
        ans = database.update_reader(stu_info)
        if ans:
            self.searchFunction()

    def deletereaderFunction(self, BID: str):
        msgBox = QMessageBox(QMessageBox.Warning, "警告!", '您将会永久删除此读者以及相关信息!',
                             QMessageBox.NoButton, self)
        msgBox.addButton("确认", QMessageBox.AcceptRole)
        msgBox.addButton("取消", QMessageBox.RejectRole)
        if msgBox.exec_() == QMessageBox.AcceptRole:
            ans = database.delete_reader(BID)
            if ans:
                self.searchFunction()

    def initUI(self):
        self.setFixedSize(900, 600)
        # self.setStyleSheet('''
        # *{
        #     background-color: white;
        #     border:0px;
        # }
        # ''')
        # self.titleBar.setStyleSheet('''
        # QWidget {
        #     border:0;
        #     background-color: rgba(216, 216, 216, 1);
        #     border-radius: 20px;
        #     color: rgba(113, 118, 121, 1);
        # }
        # QLabel{
        #     font-size: 25px;
        #     font-family: 微软雅黑;
        # }
        # ''')
        # self.searchTitle.setStyleSheet('''
        #     QLabel{
        #         font-size:25px;
        #         color: black;
        #         font-family: 微软雅黑;
        #     }
        # ''')
        # self.searchInput.setStyleSheet('''
        #     QLineEdit{
        #         border: 1px solid rgba(201, 201, 201, 1);
        #         border-radius: 5px;
        #         color: rgba(120, 120, 120, 1)
        #     }
        # ''')
        # self.searchButton.setStyleSheet('''
        #     QToolButton{
        #         border-radius: 10px;
        #         background-color:rgba(52, 118, 176, 1);
        #         color: white;
        #         font-size: 25px;
        #         font-family: 微软雅黑;
        #     }
        # ''')


class BorrowManage(QWidget):

    def __init__(self):
        super().__init__()
        self.body = QVBoxLayout()
        self.borrow_list = []
        self.table = None
        self.setTitleBar()
        self.setSearchBar()
        self.searchFunction()

        self.setLayout(self.body)
        self.initUI()

    # 标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('借阅信息管理')
        self.title.setFixedHeight(25)
        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(50)
        titleLayout.addWidget(self.title)
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(900, 50)
        self.titleBar.setLayout(titleLayout)
        self.body.addWidget(self.titleBar)

    # 设置搜索框
    def setSearchBar(self):
        self.searchTitle = QLabel()
        self.searchTitle.setText('搜索读者')
        self.searchInput = QLineEdit()
        self.searchInput.setText('ID/姓名')
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setFixedSize(450, 40)
        self.searchreaderButton = QToolButton()
        self.searchreaderButton.setFixedSize(120, 40)
        self.searchreaderButton.setText('搜索学号')
        self.searchreaderButton.clicked.connect(
            lambda: self.searchFunction('SID'))

        self.searchBookButton = QToolButton()
        self.searchBookButton.setFixedSize(120, 40)
        self.searchBookButton.setText('搜索书号')
        self.searchBookButton.clicked.connect(lambda: self.searchFunction())

        searchLayout = QHBoxLayout()
        searchLayout.addStretch()
        searchLayout.addWidget(self.searchTitle)
        searchLayout.addWidget(self.searchInput)
        searchLayout.addWidget(self.searchreaderButton)
        searchLayout.addWidget(self.searchBookButton)
        searchLayout.addStretch()

        self.searchWidget = QWidget()
        self.searchWidget.setLayout(searchLayout)
        self.body.addWidget(self.searchWidget)

    # 搜索方法
    def searchFunction(self, e: str = 'BID'):
        # 搜索书号
        if e == 'BID':
            self.borrow_list = database.get_borrowing_books(
                self.searchInput.text(), True)
        else:
            # 搜索学号
            self.borrow_list = database.get_borrowing_books(
                self.searchInput.text())
            self.SID = self.searchInput.text()
        if self.borrow_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.setTable()

    # 设置表格
    def setTable(self, val: dict = None):
        self.table = QTableWidget(1, 7)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.setFixedHeight(500)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setColumnWidth(2, 120)
        self.table.setColumnWidth(1, 120)
        self.table.setColumnWidth(4, 170)
        self.table.setColumnWidth(3, 170)

        self.table.setItem(0, 0, QTableWidgetItem('读者号'))
        self.table.setItem(0, 1, QTableWidgetItem('书号'))
        self.table.setItem(0, 2, QTableWidgetItem('书名'))
        self.table.setItem(0, 3, QTableWidgetItem('借书日期'))
        self.table.setItem(0, 4, QTableWidgetItem('还书日期'))
        self.table.setItem(0, 5, QTableWidgetItem('罚金'))
        self.table.setItem(0, 6, QTableWidgetItem('操作'))

        for i in range(7):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('微软雅黑', 15))
        for i in self.borrow_list:
            self.insertRow(i)

        self.body.addWidget(self.table)

    # 插入行
    def insertRow(self, val: list):
        itemSID = QTableWidgetItem(val[0])
        itemSID.setTextAlignment(Qt.AlignCenter)
        itemBID = QTableWidgetItem(val[1])
        itemBID.setTextAlignment(Qt.AlignCenter)
        itemNAME = QTableWidgetItem(val[2])
        itemNAME.setTextAlignment(Qt.AlignCenter)
        itemBEGIN = QTableWidgetItem(val[3])
        itemBEGIN.setTextAlignment(Qt.AlignCenter)
        itemBACK = QTableWidgetItem(val[4])
        itemBACK.setTextAlignment(Qt.AlignCenter)
        itemPUNISHED = QLabel()
        itemPUNISHED.setText('0')
        itemPUNISHED.setAlignment(Qt.AlignCenter)
        isPunished = database.days_between(val[4],
                                           time.strftime("%Y-%m-%d-%H:%M"))
        if isPunished <= 0:
            itemPUNISHED.setStyleSheet('''
                *{
                    color: green;
                    font-size:20px;
                    font-family: 微软雅黑;
                }
            ''')
        else:
            itemPUNISHED.setText(str(isPunished))
            itemPUNISHED.setStyleSheet('''
                *{
                    color: red;
                    font-size:20px;
                    font-family: 微软雅黑;
                }
            ''')
        itemOPERATE = QToolButton(self.table)
        itemOPERATE.setFixedSize(70, 25)
        itemOPERATE.setText('还书')
        itemOPERATE.clicked.connect(
            lambda: self.retrurnBook(val[0], val[1], isPunished))
        itemOPERATE.setStyleSheet('''
        *{
            color: white;
            font-family: 微软雅黑;
            background: rgba(38, 175, 217, 1);
            border: 0;
            border-radius: 10px;
            font-size:18px;
        }
        ''')

        itemLayout = QHBoxLayout()
        itemLayout.setContentsMargins(0, 0, 0, 0)
        itemLayout.addWidget(itemOPERATE)
        itemWidget = QWidget()
        itemWidget.setLayout(itemLayout)

        self.table.insertRow(1)
        self.table.setItem(1, 0, itemSID)
        self.table.setItem(1, 1, itemBID)
        self.table.setItem(1, 2, itemNAME)
        self.table.setItem(1, 3, itemBEGIN)
        self.table.setItem(1, 4, itemBACK)
        self.table.setCellWidget(1, 5, itemPUNISHED)
        self.table.setCellWidget(1, 6, itemWidget)

    def retrurnBook(self, SID: str, BID: str, isPunished: int):
        if isPunished > 0:
            database.pay(BID, SID, isPunished)
        ans = database.return_book(BID, SID)
        # 刷新表格
        if ans:
            self.searchFunction('BID')

    def initUI(self):
        self.setFixedSize(1000, 600)
        self.setStyleSheet('''
        *{
            background-color: white;
            border:0px;
        }
        ''')
        self.titleBar.setStyleSheet('''
        QWidget {
            border:0;
            background-color: rgba(216, 216, 216, 1);
            border-radius: 20px;
            color: rgba(113, 118, 121, 1);
        }
        QLabel{
            font-size: 25px;
            font-family: 微软雅黑;
        }
        ''')
        self.searchWidget.setStyleSheet('''
            QToolButton{
                border-radius: 10px;
                background-color:rgba(52, 118, 176, 1);
                color: white;
                font-size: 25px;
                font-family: 微软雅黑;
            }
            QLineEdit{
                border: 1px solid rgba(201, 201, 201, 1);
                border-radius: 5px;
                color: rgba(120, 120, 120, 1)
            }
            QLabel{
                font-size:25px;
                color: black;
                font-family: 微软雅黑;
            }
        ''')


class HistoryManage(QWidget):

    def __init__(self):
        super().__init__()
        self.body = QVBoxLayout()
        self.table = None
        self.setTitleBar()
        self.setSearchBar()
        self.searchFunction()
        self.body.addStretch()

        self.setLayout(self.body)
        self.initUI()

    # 标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('借阅记录管理')
        self.title.setFixedHeight(25)
        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(50)
        titleLayout.addWidget(self.title)
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(900, 50)
        self.titleBar.setLayout(titleLayout)
        self.body.addWidget(self.titleBar)

    # 设置搜索框
    def setSearchBar(self):
        self.searchTitle = QLabel()
        self.searchTitle.setText('搜索读者')
        self.searchInput = QLineEdit()
        self.searchInput.setText('ID/姓名')
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setFixedSize(400, 40)
        self.searchreaderButton = QToolButton()
        self.searchreaderButton.setFixedSize(120, 40)
        self.searchreaderButton.setText('搜索学号')
        self.searchreaderButton.clicked.connect(
            lambda: self.searchFunction('SID'))

        self.searchBookButton = QToolButton()
        self.searchBookButton.setFixedSize(120, 40)
        self.searchBookButton.setText('搜索书号')
        self.searchBookButton.clicked.connect(lambda: self.searchFunction())

        self.outButton = QToolButton()
        self.outButton.setText('导出')
        self.outButton.clicked.connect(self.outFunction)
        self.outButton.setFixedSize(100, 40)

        searchLayout = QHBoxLayout()
        searchLayout.addStretch()
        searchLayout.addWidget(self.searchTitle)
        searchLayout.addWidget(self.searchInput)
        searchLayout.addWidget(self.searchreaderButton)
        searchLayout.addWidget(self.searchBookButton)
        searchLayout.addWidget(self.outButton)
        searchLayout.addStretch()

        self.searchWidget = QWidget()
        self.searchWidget.setFixedWidth(900)
        self.searchWidget.setLayout(searchLayout)
        self.body.addWidget(self.searchWidget)

    # 搜索方法
    def searchFunction(self, e: str = 'BID'):
        # 搜索书号
        if e == 'BID':
            self.log_list = database.get_log(self.searchInput.text(), True)
        else:
            # 搜索学号
            self.log_list = database.get_log(self.searchInput.text())
        if self.log_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.setTable()

    # 创建表格
    def setTable(self, val: dict = None):
        self.table = QTableWidget(1, 6)
        self.table.setFixedHeight(450)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 170)
        self.table.setColumnWidth(3, 175)
        self.table.setColumnWidth(4, 175)
        self.table.setColumnWidth(5, 100)
        self.table.setItem(0, 0, QTableWidgetItem('学号'))
        self.table.setItem(0, 1, QTableWidgetItem('书号'))
        self.table.setItem(0, 2, QTableWidgetItem('书名'))
        self.table.setItem(0, 3, QTableWidgetItem('借书日期'))
        self.table.setItem(0, 4, QTableWidgetItem('还书日期'))
        self.table.setItem(0, 5, QTableWidgetItem('罚金'))

        for i in range(6):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('微软雅黑', 15))

        for i in self.log_list:
            self.insertRow(i)
        self.body.addWidget(self.table)

    # 插入行
    def insertRow(self, val: list):
        itemSNAME = QTableWidgetItem(val[0])
        itemSNAME.setTextAlignment(Qt.AlignCenter)
        itemBID = QTableWidgetItem(val[1])
        itemBID.setTextAlignment(Qt.AlignCenter)
        itemNAME = QTableWidgetItem('《' + val[2] + '》')
        itemNAME.setTextAlignment(Qt.AlignCenter)
        itemBEGIN = QTableWidgetItem(val[3])
        itemBEGIN.setTextAlignment(Qt.AlignCenter)
        itemBACK = QTableWidgetItem(val[4])
        itemBACK.setTextAlignment(Qt.AlignCenter)
        itemPUNISHED = QLabel()
        itemPUNISHED.setText(str(val[5]))
        itemPUNISHED.setAlignment(Qt.AlignCenter)
        if val[5] == 0:
            itemPUNISHED.setStyleSheet('''
                *{
                    color: green;
                    font-size: 20px;
                }
            ''')
        else:
            itemPUNISHED.setStyleSheet('''
                *{
                    color: red;
                    font-size: 20px;
                }
            ''')
        self.table.insertRow(1)
        self.table.setItem(1, 0, itemSNAME)
        self.table.setItem(1, 1, itemBID)
        self.table.setItem(1, 2, itemNAME)
        self.table.setItem(1, 3, itemBEGIN)
        self.table.setItem(1, 4, itemBACK)
        self.table.setCellWidget(1, 5, itemPUNISHED)

    def outFunction(self):
        import csv
        dirName = QFileDialog.getExistingDirectory(self, '选择文件夹')
        title = ['SID', 'BID', 'BNAME', 'BORROW_DATE', 'BACK_DATE', 'PUNISHED']
        with open(os.path.join(dirName, 'log.csv'), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(title)
            for row in self.log_list:
                writer.writerow(row)

    def initUI(self):
        self.setFixedSize(1000, 600)
        self.setStyleSheet('''
        *{
            background-color: white;
            border:0px;
        }
        ''')
        self.titleBar.setStyleSheet('''
        QWidget {
            border:0;
            background-color: rgba(216, 216, 216, 1);
            border-radius: 20px;
            color: rgba(113, 118, 121, 1);
        }
        QLabel{
            font-size: 25px;
            font-family: 微软雅黑;
        }
        ''')
        self.table.setStyleSheet('''
            font-size:18px;
            color: black;
            background-color: white;
            font-family: 微软雅黑;
        ''')
        self.outButton.setStyleSheet('''
        QToolButton{
            border-radius: 10px;
            background-color:rgba(52, 118, 176, 1);
            color: white;
            font-size: 25px;
            font-family: 微软雅黑;
        }
        ''')
        self.searchWidget.setStyleSheet('''
            QToolButton{
                border-radius: 10px;
                background-color:rgba(52, 118, 176, 1);
                color: white;
                font-size: 25px;
                font-family: 微软雅黑;
            }
            QLineEdit{
                border: 1px solid rgba(201, 201, 201, 1);
                border-radius: 5px;
                color: rgba(120, 120, 120, 1)
            }
            QLabel{
                font-size:25px;
                color: black;
                font-family: 微软雅黑;
            }
        ''')


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     user_message = {'class': 'master', 'ID': 'master'}
#     ex = AdministratorPage(user_message)
#     ex.show()
#     sys.exit(app.exec_())
