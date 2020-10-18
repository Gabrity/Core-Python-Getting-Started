

f = open('wasteland.txt', mode ='wt', encoding = 'utf-8')
f.write('What are the roots...\nGrow')
f.close()

g = open('wasteland.txt', mode ='rt', encoding = 'utf-8')
print(g.read(32))
print(g.read())

g.seek(0)
print(g.readline())

g.seek(0)
print(g.readlines())

h = open('wasteland.txt', mode ='at', encoding = 'utf-8')
h.writelines('Todo')

