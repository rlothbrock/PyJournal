from PySide2 import QtGui
from PySide2.QtPrintSupport import QPrinter, QPrintPreviewDialog

from packages.components.status import current_date


def draw_printable_(container):
    printable_template = QtGui.QTextDocument()

    table_data = ""
    table_headers = ""

    for colHeaderIndex in range(container.columnCount()):
        table_headers += "<th>{}</th>".format(
            container.takeHorizontalHeaderItem(colHeaderIndex).text()
        )

    for rowIndex in range(container.rowCount()):
        table_data += '<tr>'
        for column in range(container.columnCount()):
            table_data += '<td>{}</td>'.format(container.item(rowIndex,column).text() or "")
        table_data += '</tr>'

    main_html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        table, th, td {
            border: 1px solid black;
            padding: 3px;
            border-collapse: collapse;
            font-size: small; 
        }
        th {
            text-align: center;
            font-weight: bold;
        }
        td {
            text-align: center
        }
        .date_of_print {
            text-align: left;
            font-weight: bold;
        }'''+'''

    </style>
</head>
<body>
    <div class="date_of_print">printed using PyJournal on: {0}</div><br>
    <table>
          <thead><tr>{1}</tr></thead>
          <tbody>{2}</tbody>
          <tfoot>
          </tfoot>
      </table><br>
    <footer >
        <p class="date_of_print">printed using PyJournal on: {0}</p>
        <hr>
        <div>
            <small>PyJournal&copy; is a licensed product and belongs to rlothbrock.10@gmail.com</small>
        <div>
    </footer>
</body>
</
    '''.format(current_date, table_headers, table_data)

    printable_template.setHtml(main_html)
    return printable_template


def data_printer(self, data_container, drawer=draw_printable_):
    print_template = drawer(data_container)
    printer = QPrinter()
    previewDialog = QPrintPreviewDialog(printer,self)
    previewDialog.setGeometry(self.width()//2-200,self.height()//4,1200,600)
    previewDialog.paintRequested.connect(print_template.print_)
    previewDialog.exec_()
    return





