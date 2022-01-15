message1 = 'hello' + ' ' +'world'
print(message1)

message2a = 'hello ' *3
message2b = 'world'
print(message2a + message2b)

message3 = 'howdy'
message3 += ' '
message3 += 'world'
print(message3)

message4 = 'hello' + ' ' + 'world'
print(len(message4))

message5 = 'hello world'
message5a = message5.find('worl')
print(message5a)

message6 = 'Hello World'
message6b = message6.find('squirrel')
print(message6b)

message7 = 'HELLO WORLD'
message7a = message7.lower()
print(message7a)

message8 = "HELLO WORLD"
message8a = message8.replace("L", "pizza")
print(message8a)

message9 = 'Hello World'
message9a = message9[1:8]
print(message9a)

startLoc=2
endLoc=9
message9b = message9[startLoc: endLoc]
print(message9b)

message9 = "Hello World"
print(message9[:5].find("d"))

print('\"')

print('The program printed \'Hello World\'')


print('hello\thello\thello\nworld')

n=1

converted_n = str(n).zfill(2)
string10='/data/today/Sun_Live_'+converted_n+'.jpg'
print(string10)

c2="{:04n}".format(n)
string11='/data/today/Sun_Live_'+c2+'.jpg'
print(string11)




