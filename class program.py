import sys
if len (sys.argv) == 6:
 script_name =sys.argv[0]
 m1=sys.argv[1]
 m2=sys.argv[2]
 m3=sys.argv[3]
 m4=sys.argv[4]
 m5=sys.argv[5]
else:
  script_name =sys.argv[0]
  m1=60
  m1=80
  m1=94
  m1=82
  m1=78
avg=(m1+m2+m3+m4+m5)/5
if(avg>90)
grade='A+'
elif(avg>80)
grade='A'
elif(avg>70)
grade='B'
elif(avg>60)
grade='C'
elif(avg>50)
grade='fail'

print("marks 1",m1)
print("marks 2",m2)
print("marks 3",m3)
print("marks 4",m4)
print("marks 5",m5)
print("average",avg)
print("grade",grade)

