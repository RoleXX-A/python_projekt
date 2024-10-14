from odf.opendocument import OpenDocumentSpreadsheet
from odf.table import Table, TableRow, TableCell
from odf.text import P

#создаем ODS файл
doc = OpenDocumentSpreadsheet()

#Создаем таблицу

table = Table(name = 'MyTable')

#Данные для записи
data = [["Имя", "Фамилия","Возраст"],
        ["Иван","Иванов","25"],
        ["Мария","Петрова","26"],
        ["Никита","Сергеев","27"]
]

#Добавляем строки и ячеки с данными
for row_data in data:
    row = TableRow()
    for cell_data in row_data:
        cell = TableCell()
        cell.addElement(P(text = str(cell_data)))# Добавляем текст в ячейку
        row.addElement(cell)
    table.addElement(row)

#Добавляем таблицу в документ
doc.spreadsheet.addElement(table)

#Сохраняем документ в файл
doc.save("example.ods")