import sqlite3
from datetime import datetime
import xlrd
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QShortcut, QFileDialog, QTableWidgetItem, QApplication, QMessageBox
import xlwt
import Main
import edit_product
import add_product


class Mainwindow(QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.window2 = add_window()
        self.setupUi(self)
        self.progressBar.setVisible(False)
        self.progressBar2.setVisible(False)

        conn = sqlite3.connect("import.db")
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS dorilar(code INTEGER, nomi TEXT, manufacturer TEXT, narxi INTEGER, 
            qadoq INTEGER, yaroq INTEGER, soni INTEGER)""")
        conn.commit()
        conn.close()
        conn = sqlite3.connect("export.db")
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS export(id INTEGER PRIMARY KEY AUTOINCREMENT,code INTEGER, nomi TEXT, 
            manufacturer TEXT, narxi INTEGER, qadoq INTEGER, soni INTEGER, yaroq INTEGER)""")
        conn.commit()
        conn.close()

        self.tobaza = QShortcut(QKeySequence("Ctrl+F"), self)
        self.tobaza.activated.connect(self.tobaza_func)

        self.filtered.setColumnHidden(0, True)
        self.filtered.setColumnHidden(7, True)
        self.filtered.setColumnHidden(8, True)
        self.import_2.clicked.connect(self.fun_import)
        self.search_edit.textChanged.connect(self.text_changed)
        self.filtered.clicked.connect(self.product)
        self.delete_1.clicked.connect(self.del_func)
        self.btnsave.clicked.connect(self.save)
        self.delete_all.clicked.connect(self.deleteall)
        self.export_2.clicked.connect(self.dialog_export)
        self.filtered.itemSelectionChanged.connect(self.row_changed)
        self.search_edit_2.textChanged.connect(self.search_from_baza)
        self.update_table()
        self.search_edit.setFocus()
        self.mix.clicked.connect(self.import_files)


    def import_files(self):
        files = QFileDialog.getOpenFileNames(self, 'Файлларни юклаш', '', "Excel (*.xls)")[0]
        if len(files) != 0:
            conn = sqlite3.connect("export.db")
            cur = conn.cursor()
            cur.execute("""DROP TABLE export""")
            cur.execute("""CREATE TABLE IF NOT EXISTS export(id INTEGER PRIMARY KEY AUTOINCREMENT,code INTEGER, nomi TEXT, 
                                    manufacturer TEXT, narxi INTEGER, qadoq INTEGER, soni INTEGER, yaroq INTEGER)""")
            for i in files:
                wb = xlrd.open_workbook(i)
                sheet = wb.sheet_by_index(0)
                for k in range(3, sheet.nrows):
                    l = sheet.row(k)
                    code = int(l[2].value)
                    name = l[3].value
                    manufacture = l[4].value
                    cost = int(l[9].value)
                    qoldiq = int(l[10].value)
                    qadoq = int(l[11].value)
                    if l[15].value == "":
                        yaroq = 0
                    else:
                        yaroq = int(l[15].value)
                    cur.execute("""select * from export where nomi=? and qadoq=? and manufacturer=?""",
                                [name, qadoq, manufacture])
                    row = cur.fetchone()
                    if row is None:
                        cur.execute("""INSERT INTO export(code, nomi, manufacturer, narxi, qadoq, soni, yaroq) VALUES(?,?,?,?,?,
                        ?,?)""", [code, name, manufacture, cost, qadoq, qoldiq, yaroq])
                    else:
                        cur.execute("""update export set soni=? where nomi=? and manufacturer=? and qadoq=?""",
                                    (row[6] + qoldiq, row[2], row[3], row[5]))
            conn.commit()
            conn.close()
            self.update_table()

    def tobaza_func(self):
        self.search_edit_2.setFocus()

    def search_from_baza(self):
        if len(self.search_edit_2.text()) > 2:
            self.search_edit.setText("")
            conn = sqlite3.connect("export.db")
            cur = conn.cursor()
            text = '"%' + self.search_edit_2.text() + '%"'
            text2 = '"%' + self.search_edit_2.text().capitalize() + '%"'
            cur.execute(f"SELECT * FROM export WHERE nomi LIKE {text} OR nomi LIKE {text2} LIMIT 50")
            a = cur.fetchall()
            while self.filtered.rowCount() > 0:
                self.filtered.removeRow(0)
            if len(a) > 0:
                for row in range(0, len(a)):
                    b = self.filtered.rowCount()
                    self.filtered.insertRow(b)
                    excel_date = a[b][7]
                    if excel_date != "":
                        dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date)
                        date = dt.strftime("%m/%d/%Y")
                    else:
                        date = ""
                    self.filtered.setItem(b, 0, QTableWidgetItem(str(a[b][1])))
                    self.filtered.setItem(b, 1, QTableWidgetItem(a[b][2]))
                    self.filtered.setItem(b, 2, QTableWidgetItem(a[b][3]))
                    self.filtered.setItem(b, 3, QTableWidgetItem(str(a[b][4])))
                    self.filtered.setItem(b, 4, QTableWidgetItem(str(a[b][5])))
                    self.filtered.setItem(b, 5, QTableWidgetItem(str(a[b][6])))
                    self.filtered.setItem(b, 6, QTableWidgetItem(date))
                    self.filtered.setItem(b, 7, QTableWidgetItem(str(a[b][7])))
                    self.filtered.setItem(b, 8, QTableWidgetItem(str(a[b][0])))
        else:
            self.update_table()

    def save(self):
        if len(self.filtered.selectedItems()) != 0 and self.status.text() == "Қўшилган дорилар:":
            narx = self.narx.text()
            qadoq = self.qadoq.text()
            soni = self.soni.text()
            conn = sqlite3.connect("export.db")
            cur = conn.cursor()
            cur.execute("""UPDATE export SET narxi=?, qadoq=?, soni=? WHERE id=?""",
                        (int(narx), int(qadoq), int(soni), self.filtered.item(self.filtered.currentRow(), 8).text()))
            conn.commit()
            conn.close()
            self.update_table()

    def deleteall(self):
        if self.filtered.rowCount() != 0 and self.status.text() == "Қўшилган дорилар:":
            msg = QMessageBox()
            msg.setWindowTitle("Барчасини ўчириш")
            msg.setText("Ростдан ҳам ҳаммасини ўчирмоқчимисиз?")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            msg.buttonClicked.connect(self.delete)
            x = msg.exec_()

    def delete(self, i):
        if i.text() == "OK":
            conn = sqlite3.connect("export.db")
            cur = conn.cursor()
            cur.execute("""DROP TABLE export""")
            cur.execute("""CREATE TABLE IF NOT EXISTS export(id INTEGER PRIMARY KEY AUTOINCREMENT,code INTEGER, nomi TEXT, 
                        manufacturer TEXT, narxi INTEGER, qadoq INTEGER, soni INTEGER, yaroq INTEGER)""")
            conn.commit()
            conn.close()
            self.update_table()

    def tosearch_func(self):
        self.search_edit.setFocus()

    def del_func(self):
        if len(self.filtered.selectedItems()) != 0 and self.status.text() == "Қўшилган дорилар:":
            id = self.filtered.item(self.filtered.currentRow(), 8).text()
            conn = sqlite3.connect("export.db")
            cur = conn.cursor()
            cur.execute(f"""DELETE FROM export WHERE id = {int(id)}""")
            conn.commit()
            conn.close()
            self.update_table()
            if self.filtered.rowCount() != 0:
                self.filtered.setFocus()
                self.filtered.selectRow(0)

    def row_changed(self):
        if self.status.text() == "Қўшилган дорилар:" and len(self.filtered.selectedItems()) != 0:
            items = self.filtered.selectedItems()
            k = items[2].text()
            l = items[3].text()
            m = items[4].text()
            self.narx.setText(k)
            self.qadoq.setText(l)
            self.soni.setText(m)
            d = int(k) * int(m)
            self.summa.setText('{:,}'.format(d).replace(',', ' '))
        else:
            self.narx.setText("")
            self.qadoq.setText("")
            self.soni.setText("")
            self.summa.setText("")

    def dialog_export(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', '', "Excel (*.xls)")[0]
        conn = sqlite3.connect("export.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM export")
        a = cur.fetchall()
        self.path_export = filename
        if self.path_export != "" and len(a) != 0:
            conn.close()
            self.export_2.setVisible(False)
            self.progressBar2.setVisible(True)
            self.thread2 = MyThread2()
            self.thread2.val2.connect(self.setProgressVal2)
            self.thread2.start()

    def setProgressVal2(self, val2):
        self.progressBar2.setValue(val2)
        if val2 == 100:
            self.progressBar2.setVisible(False)
            self.progressBar2.setValue(0)
            self.export_2.setVisible(True)

    def fun_import(self):
        load_path = str(QFileDialog.getOpenFileName(self, "Load file", "", "Excel (*.xls)")[0])
        self.path = load_path
        if self.path != "":
            self.import_2.setVisible(False)
            self.progressBar.setVisible(True)
            self.thread = MyThread()
            self.thread.val.connect(self.setProgressVal)
            self.thread.start()

    def setProgressVal(self, val):
        self.progressBar.setValue(val)
        if val == 100:
            self.progressBar.setVisible(False)
            self.progressBar.setValue(0)
            self.import_2.setVisible(True)

    def keyPressEvent(self, e):
        if (e.key() == Qt.Key_Down or e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return) and self.search_edit.hasFocus():
            if self.filtered.rowCount() != 0:
                self.filtered.setFocus()
                self.filtered.selectRow(0)
        if e.key() == Qt.Key_Up and self.filtered.hasFocus():
            if self.filtered.rowCount() != 0:
                if self.filtered.currentRow() == 0:
                    self.filtered.clearFocus()
                    self.filtered.clearSelection()
                    self.search_edit.setFocus()
        if e.key() == Qt.Key_Delete and len(self.filtered.selectedItems()) != 0:
            self.del_func()
        if (e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return) and self.filtered.hasFocus():
            self.product()
        if e.key() == Qt.Key_Escape:
            self.filtered.clearFocus()
            self.filtered.clearSelection()
            self.search_edit.setFocus()
            self.search_edit.setText("")



    def update_table(self):
        while self.filtered.rowCount() > 0:
            self.filtered.removeRow(0)
        conn = sqlite3.connect("export.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM export order by -id")
        a = cur.fetchall()
        s = 0
        if len(a) > 0:
            for row in range(0, len(a)):
                b = self.filtered.rowCount()
                self.filtered.insertRow(b)
                excel_date = a[b][7]
                if excel_date != 0:
                    dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date)
                    date = dt.strftime("%m/%d/%Y")
                else:
                    date = ""
                self.filtered.setItem(b, 0, QTableWidgetItem(str(a[b][1])))
                self.filtered.setItem(b, 1, QTableWidgetItem(a[b][2]))
                self.filtered.setItem(b, 2, QTableWidgetItem(a[b][3]))
                self.filtered.setItem(b, 3, QTableWidgetItem(str(a[b][4])))
                self.filtered.setItem(b, 4, QTableWidgetItem(str(a[b][5])))
                self.filtered.setItem(b, 5, QTableWidgetItem(str(a[b][6])))
                self.filtered.setItem(b, 6, QTableWidgetItem(date))
                self.filtered.setItem(b, 7, QTableWidgetItem(str(a[b][7])))
                self.filtered.setItem(b, 8, QTableWidgetItem(str(a[b][0])))
                s += a[b][4] * a[b][6]
        self.jami.setText('{:,}'.format(s).replace(',', ' '))

    def product(self):
        if len(self.filtered.selectedItems()) != 0 and len(self.search_edit.text()) > 2:
            t = self.filtered.selectedItems()
            name = t[0].text()
            zavod = t[1].text()
            qadoq = t[3].text()
            conn = sqlite3.connect("export.db")
            cur = conn.cursor()
            cur.execute("""select * from export where nomi=? and manufacturer=? and qadoq=?""", [name, zavod, qadoq])
            checked = cur.fetchone()
            if checked is None:
                self.window2.setWindowFlag(Qt.WindowStaysOnTopHint)
                self.window2.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
                self.window2.show()
            else:
                self.w3 = edit_prdct(checked[0])
                self.w3.setWindowFlag(Qt.WindowStaysOnTopHint)
                self.w3.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
                self.w3.show()
                self.w3.lineEdit_5.setFocus()

    def text_changed(self):
        if len(self.search_edit.text()) >= 3:
            self.search_edit_2.setText("")
            self.status.setText("Қидирув натижалари:")
            conn = sqlite3.connect("import.db")
            cur = conn.cursor()
            text = '"%' + self.search_edit.text() + '%"'
            text2 = '"%' + self.search_edit.text().capitalize() + '%"'
            cur.execute(f"SELECT * FROM dorilar WHERE nomi LIKE {text} OR nomi LIKE {text2} order by soni desc LIMIT 50")
            a = cur.fetchall()
            while self.filtered.rowCount() > 0:
                self.filtered.removeRow(0)
            if len(a) > 0:
                for row in range(0, len(a)):
                    b = self.filtered.rowCount()
                    self.filtered.insertRow(b)
                    excel_date = a[b][5]
                    if excel_date != "":
                        dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date)
                        date = dt.strftime("%m/%d/%Y")
                    else:
                        date = ""
                    self.filtered.setItem(b, 0, QTableWidgetItem(str(a[b][0])))
                    self.filtered.setItem(b, 1, QTableWidgetItem(a[b][1]))
                    self.filtered.setItem(b, 2, QTableWidgetItem(a[b][2]))
                    self.filtered.setItem(b, 3, QTableWidgetItem(str(a[b][3])))
                    self.filtered.setItem(b, 4, QTableWidgetItem(str(a[b][4])))
                    self.filtered.setItem(b, 5, QTableWidgetItem(str(a[b][6])))
                    self.filtered.setItem(b, 6, QTableWidgetItem(date))
                    self.filtered.setItem(b, 7, QTableWidgetItem(str(a[b][5])))
        else:
            self.status.setText("Қўшилган дорилар:")
            self.filtered.setColumnHidden(5, False)
            self.update_table()


class MyThread(QThread):
    val = pyqtSignal(int)

    def run(self):
        load_path = w.path
        workbook = xlrd.open_workbook(load_path)
        sheet = workbook.sheet_by_index(0)
        conn = sqlite3.connect("import.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM dorilar")
        conn.commit()
        for i in range(3, sheet.nrows):
            a = sheet.row(i)
            id = int(a[2].value)
            nomi = a[3].value
            manufacturer = a[4].value
            narxi = int(a[9].value)
            qadoq = int(a[11].value)
            soni = int(a[10].value)
            if a[15].value == "":
                yaroq = ""
            else:
                yaroq = int(a[15].value)
            cur.execute(
                """INSERT INTO dorilar(code, nomi, manufacturer, narxi, qadoq, yaroq, soni) VALUES(?, ?, ?, ?, ?, ?, ?)""",
                [id, nomi, manufacturer, narxi, qadoq, yaroq, soni])
            cnt = int((i + 1) / sheet.nrows * 100)
            self.val.emit(cnt)
        conn.commit()
        conn.close()


class MyThread2(QThread):
    val2 = pyqtSignal(int)

    def run(self):
        load_path = w.path_export
        conn = sqlite3.connect("export.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM export")
        a = cur.fetchall()
        wb = xlwt.Workbook()
        ws = wb.add_sheet("Sheet 1")
        ws.write(2, 2, "Код")
        ws.write(2, 3, "Махсулот номи")
        ws.write(2, 4, "Ишлаб чиқарувчи")
        ws.write(2, 5, "Бош.нарх")
        ws.write(2, 6, "Ул/Б")
        ws.write(2, 7, "Ол.нарх")
        ws.write(2, 8, "Уст %")
        ws.write(2, 9, "Сот.нарх")
        ws.write(2, 10, "Қолдиқ")
        ws.write(2, 11, "Қадоқ")
        ws.write(2, 12, "Бош.Йиғ")
        ws.write(2, 13, "Ол.Йиғ.")
        ws.write(2, 14, "Сот.Йиғ")
        ws.write(2, 15, "Яроқ.")
        for i in range(len(a)):
            k = i + 3
            ws.write(k, 2, a[i][1])
            ws.write(k, 3, a[i][2])
            ws.write(k, 4, a[i][3])
            ws.write(k, 9, a[i][4])
            ws.write(k, 10, a[i][6])
            ws.write(k, 11, a[i][5])
            if a[i][7] != 0:
                ws.write(k, 15, a[i][7])
            cnt = int((i + 1) / len(a) * 100)
            self.val2.emit(cnt)
        conn.close()
        wb.save(load_path)


class add_window(QMainWindow, add_product.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.shortcut = QShortcut(QKeySequence("Enter"), self)
        self.shortcut2 = QShortcut(QKeySequence("Return"), self)
        self.shortcut3 = QShortcut(QKeySequence("Esc"), self)
        self.setupUi(self)
        self.shortcut.activated.connect(self.finished)
        self.shortcut2.activated.connect(self.finished)
        self.shortcut3.activated.connect(self.cancel)
        self.soni_edit.setFocus()
        self.enter.clicked.connect(self.finished)

    def finished(self):
        if len(self.soni_edit.text()) != 0 and w.filtered.selectedItems() != 0:
            t = w.filtered.selectedItems()
            name = t[0].text()
            zavod = t[1].text()
            narx = t[2].text()
            qadoq = t[3].text()
            soni = self.soni_edit.text()
            id = w.filtered.item(w.filtered.currentRow(), 0).text()
            muddati = w.filtered.item(w.filtered.currentRow(), 7).text()
            if len(muddati) == 0:
                muddati = "0"
            conn = sqlite3.connect("export.db")
            cur = conn.cursor()
            cur.execute(
                """INSERT INTO export(code, nomi, manufacturer, narxi, qadoq, soni, yaroq) VALUES(?, ?, ?, ?, ?, ?, 
                ?)""",
                [int(id), name, zavod, int(narx), int(qadoq), int(soni), int(muddati)])
            conn.commit()
            conn.close()
            self.close()
            w.update_table()
            w.search_edit.clear()
            self.soni_edit.setText("")
            w.search_edit.setFocus()
        else:
            self.soni_edit.setText("")
            self.close()

    def cancel(self):
        self.close()


class edit_prdct(QMainWindow, edit_product.Ui_MainWindow):
    def __init__(self, id_pr):
        super().__init__()
        self.setupUi(self)
        self.id = id_pr
        self.conn = sqlite3.connect("export.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""select * from export where id=?""", [self.id])
        t = self.cur.fetchone()
        nomi = t[2]
        zavod = t[3]
        narxi = t[4]
        qadoq = t[5]
        soni = t[6]
        self.lineEdit.setText(nomi)
        self.lineEdit_2.setText(zavod)
        self.lineEdit_3.setText(str(narxi))
        self.lineEdit_4.setText(str(qadoq))
        self.lineEdit_5.setText(str(soni))
        self.shortcut = QShortcut(QKeySequence("Return"), self)
        self.shortcut2 = QShortcut(QKeySequence("Esc"), self)
        self.shortcut.activated.connect(self.ok)
        self.shortcut2.activated.connect(self.cancel)
        self.btn_ok.clicked.connect(self.ok)
        self.btn_cancel.clicked.connect(self.cancel)

    def cancel(self):
        self.close()

    def ok(self):
        self.cur.execute("""update export set soni=? where id=?""", (int(self.lineEdit_5.text()), self.id))
        self.conn.commit()
        self.conn.close()
        w.update_table()
        w.search_edit.setText("")
        w.search_edit.setFocus()
        self.close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Mainwindow()
    w.showMaximized()
    sys.exit(app.exec_())
