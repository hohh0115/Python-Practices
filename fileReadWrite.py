
import time
localtime = time.asctime( time.localtime(time.time()) )

text = 'this is first line.\nthis is last line\nbye bye'
my_file = open('fileReadWrite.txt', 'w')
my_file.write(text)
my_file.close()

appended_text = '\nhello this is dogge\n' + localtime
my_file = open('fileReadWrite.txt', 'a')
my_file.write(appended_text)
my_file.close()

file = open('fileReadWrite.txt', 'r')
# content = file.read()
# content = file.readline()
content = file.readlines()  # return list
print(content)