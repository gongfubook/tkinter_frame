from pandas import read_csv
from pandas import read_excel
from pandas import ExcelFile

from public_function.public import log

def read(file_address, sheet_name=0, sep=','):
    directory_name, file_name = os.path.split(file_address)
    fileName, suffix = os.path.splitext(file_name)
    if suffix == '.csv':
        df = read_csv(file_address,
            sep = sep,
            header = 0,
            encoding = 'gbk',
            engine = 'python',
            )
    elif suffix == '.xlsx':
        df = read_excel(file_address,
            sheetname = sheet_name,
            index = None,
            header = 0, 
            encoding = 'utf-8',
            )
    elif suffix == '.xls':
        xls_file = ExcelFile(file_address)
        df = read_excel(xls_file,
            sheetname = sheet_name,
            index = None,
            header = 0,
            encoding = 'utf-8',
            )
    else:
        raise IOError('文件类型错误，请输入xls/xlsx/csv文件')
    log(df.head())

    return df
