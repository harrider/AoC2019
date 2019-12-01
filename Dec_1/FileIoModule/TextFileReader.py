

class TextFileReader:

    def __init__(self, textFilePath : str):
        if textFilePath == '':
            raise ValueError('ERROR :: "textFilePath" was Empty!')
        if textFilePath == None:
            raise ValueError('ERROR :: "textFilePath" was None!')
        if textFilePath.lower().endswith('.txt') == False:
            raise ValueError('ERROR :: "textFilePath" must be a .txt file!')
        
        self.textFilePath = textFilePath


    def Read(self):
        with open(self.textFilePath, 'r') as textFile:
            textFileData = textFile.read()

        return textFileData.split('\n')
