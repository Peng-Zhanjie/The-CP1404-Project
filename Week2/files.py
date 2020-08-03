#Module 1

out_file1 = open("Name.txt", 'w')
Yourname=input("Please enter your name:")
print("{}".format(Yourname),file=out_file1)
out_file1.close()

#Module 2

out_file2 = open("Name.txt", 'r')
print("Your name is {}".format(out_file2.readline()))
out_file2.close()

#Module 3

out_file3 = open("numbers.txt", 'w')
Numbers=['17','42','400']
print("{}".format(Numbers[0]),file=out_file3)
print("{}".format(Numbers[1]),file=out_file3)
print("{}".format(Numbers[2]),file=out_file3)
out_file3.close()
out_file4 = open("numbers.txt", 'r')
Number1=int(out_file4.readline())
Number2=int(out_file4.readline())
print("{} + {} = {}".format(Number1,Number2,Number1+Number2))
out_file4.close()

#Module 4
#The input program
Ifnore=True
count=0
out_file5 = open("numbers.txt", 'w')
while Ifnore==True:
  Numbers=int(input("Please enter the numbers(If you enter zero it will stop):"))
  if Numbers!=0:
    print("{}".format(Numbers),file=out_file5)
    count+=1
  else :Ifnore=False
out_file5.close()
#The adding program:
total=0
out_file6 = open("numbers.txt", 'r')
for i in range(count):
  Number1=int(out_file6.readline())
  total=total+Number1
out_file6.close()
print("Total is {}".format(total))