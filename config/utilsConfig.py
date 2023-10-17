'''config file for utils'''
from datetime import datatime 

class UtilsCongig:
    saving_data_path = 'C:\\development\\NewsBite\\artifacts\\data\\'
    data_file_name = 'article_{}.csv'.format(datatime.now().strftime('%m-%d-%Y-%H-%M-%S'))