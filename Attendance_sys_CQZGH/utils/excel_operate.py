# -*- coding:utf-8 -*- 
import sys
import os
import xlrd
from xlutils.copy import copy
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)

########################################################################
class excel_obj:
    """"""
    #----------------------------------------------------------------------
    def __init__(self,sheet_name,exl_f_path):
        """"""
        self.sheet_name = sheet_name
        excel_file = exl_f_path
        self.excel_oper = xlrd.open_workbook(excel_file)
        self.sheet = self.excel_oper.sheet_by_name(sheet_name)
        
    #----------------------------------------------------------------------
    def get_sheet(self):
        """"""
        return self.sheet
    
    #----------------------------------------------------------------------
    def get_lines_cnt(self):
        """"""
        return self.sheet.nrows
        
    #----------------------------------------------------------------------
    def get_cell_value(self,row,col):
        """"""
        return self.sheet.cell_value(row,col)
        
    #----------------------------------------------------------------------
    def get_row_data(self,row_num):
        """"""
        return self.sheet.row_values(row_num)
        
    #----------------------------------------------------------------------
    def get_col_data(self,col_num):
        """"""
        return self.sheet.col_values(col_num)
        
        
if __name__ == '__main__':
    excel_obj = excel_obj()
    url = excel_obj.get_row_data(1)
    print(url)