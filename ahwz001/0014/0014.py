#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0014
* by ahwz001
* 2017/9/10
* Thanks for this project. I learned a lot here.
"""

import xlwt
 

def deal_text(source_file):
    """convert txt file to a dict of id to a list of data.
    return the dict
    """
    with open(source_file) as fn:
        content = fn.read()
    des_dict = eval(content)
    return des_dict


def save_to_xls(data, des_file):
    """write a dict to xls file.
    data: dict of id to a list of data.
    """
    wb = xlwt.Workbook(encoding = 'utf-8')
    sheet = wb.add_sheet('student',cell_overwrite_ok=True)
    row, column = 0,0

    for id in sorted(data.keys()):        
        sheet.write(row, column, id)
        print "write ... ",id,
        for val in data[id]:
            print val,
            column += 1
            sheet.write(row, column, val)
        row += 1
        column = 0
        print '\n'
    print 'ALL DONE!'
    wb.save(des_file)


def main():
    source_file = 'student.txt'
    des_file = 'student.xls'
    data = deal_text(source_file)
    save_to_xls(data, des_file)


if __name__ == '__main__':
    main()
    