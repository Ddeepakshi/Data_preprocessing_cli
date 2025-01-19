import pandas as pd

class Download:

    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    def __init__(self, data):
        self.data = data

    # download the modified DataFrame as .csv file
    def download(self):
        toBeDownload = {}
        for column in self.data.columns.values:
            toBeDownload[column] = self.data[column]

        newFileName = input("\nEnter the " + self.bold_start +"FILENAME" + self.bold_end +" you want? (Press -1 to go back):  ")
        if newFileName=="-1":
            return
        
        file_extension = newFileName.split('.')[-1]
        if file_extension not in ['csv', 'xlsx', 'json']:
            print("Unsupported file format. Please use .csv, .xlsx, or .json.")
            return
        newFileName = newFileName + "."+ file_extension
        
        # index=False as this will not add an extra column of index.
        if file_extension == 'csv':
            pd.DataFrame(self.data).to_csv(newFileName, index=False)
        elif file_extension == 'xlsx':
            pd.DataFrame(self.data).to_excel(newFileName, index=False)
        elif file_extension == 'json':
            pd.DataFrame(self.data).to_json(newFileName, orient='records', lines=True)

        
        print("Hurray!! It is done....\U0001F601")
        
        if input("Do you want to exit now? (y/n) ").lower() == 'y':
            print("Exiting...\U0001F44B")
            exit()
        else:
            return
