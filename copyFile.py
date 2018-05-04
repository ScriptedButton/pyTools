# File Copier V1

class Copy:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

    def doCopy(self):
        try:
            with open(self.source, 'rb') as source, open(self.dest, 'wb+') as dest:
                data = source.read()
                dest.write(data)
        except Exception as err:
            print("Fatal error occured: ", err)


file1 = input("Enter the source file: ")
file2 = input("Enter the destination file: ")

c = Copy(file1, file2)
c.doCopy()

