"""
Class used to run the exploit filters in the result file
"""
import os
import sys

PATH = os.path.join(os.sep, os.getcwd() + '/' + 'xpl_filters')


class XplFilter():

    def __init__(self, filters):
        self.filters = filters
        self.exploits = self.validate_xpl_filters()
        self.run_filter()

    def validate_xpl_filters(self):
        xpl_list = [''.join(file.name.split('.')[0]) for file in os.scandir(
            PATH) if not file.name.startswith('.') and file.is_file() and
            'xpl_filter' not in file.name]
        filters = self.filters.split(',')
        exploits = list(set(filters).intersection(set(xpl_list)))
        if exploits:
            return exploits
        else:
            print("\n\033[31m### Error ###")
            print("\033[33mNone of the xpl filters you choose "
                  "was found!!\033[0m\n")
            print("The current options are:\n")
            [print(xpl) for xpl in xpl_list]
            sys.exit(1)

    def run_filter(self):
        try:
            for xpl in self.exploits:
                xpl_path = os.path.join(PATH + '/' + xpl + '.py')
                os.system('python3 ' + xpl_path)
        except:
            pass
