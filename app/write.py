

def writeFile(df, file_address, sheet_name=0, sep=','):
    directory_name, fileName = os.path.split(file_address)
    name, suffix = os.path.splitext(fileName)
    if suffix == '.csv':
        df.to_csv(file_address,
            sep = sep,
            header = 1,
            encoding = 'gbk',
            index = None,
            )
        log(fileName + '保存完成')
        
    elif suffix == '.xlsx':
        writer = ExcelWriter(file_address)
        df.to_excel(writer,
            index = None,
            header = 1, 
            encoding = 'utf-8',
            )
        writer.save()
        log(fileName + '保存完成')

    else:
    	log("警告",'警告：文件类型无法保存，请输入xlsx/csv文件！')

    return 
