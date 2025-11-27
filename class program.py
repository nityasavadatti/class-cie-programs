import sys

if len(sys.argv) == 6:
    script_name = sys.argv[0]
    m1 = float(sys.argv[1])
    m2 = float(sys.argv[2])
    m3 = float(sys.argv[3])
    m4 = float(sys.argv[4])
    m5 = float(sys.argv[5])
else:
    script_name = sys.argv[0]
    # Default marks
    m1 = 60
    m2 = 80
    m3 = 94
    m4 = 82
    m5 = 78

avg = (m1 + m2 + m3 + m4 + m5) / 5

# Grade calculation
if avg > 90:
    grade = "A+"
elif avg > 80:
    grade = "A"
elif avg > 70:
    grade = "B"
elif avg > 60:
    grade = "C"
elif avg > 50:
    grade = "D"
else:
    grade = "Fail"

print("Marks 1:", m1)
print("Marks 2:", m2)
print("Marks 3:", m3)
print("Marks 4:", m4)
print("Marks 5:", m5)
print("Average:", avg)
print("Grade:", grade)
