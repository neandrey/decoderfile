# decoder.py
'''
this file detect encoding format with function
encodingFormat and module chardet and print result on monitor
function decoderFile decoder file and create new file with add
expansion '.a'
'''
import sys
from chardet.universaldetector import UniversalDetector


class decodeFile:
    def __init__(self, filename):
        self.detector = UniversalDetector()
        self.encodingFormat(filename)
        self.decoderFile(filename)

    def encodingFormat(self, filename):
        for line in open(filename, 'rb'):
            self.detector.feed(line)
            if self.detector.done:
                break
        self.detector.close()
        print(self.detector.result)

    def parseFileName(self, filename):
        posExp = filename.find('.')
        baseName = filename[:posExp]
        expName = filename[posExp:]
        newFileName = (baseName + '.a' + expName)
        return newFileName


    def decoderFile(self, filename):
        with open(self.parseFileName(filename), 'w') as file:
            for line in open(filename, 'rb'):
                file.writelines(line.decode(self.detector.result['encoding']))


if __name__ == '__main__':
    decoder = decodeFile(sys.argv[1])
