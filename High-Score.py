student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max = student_scores[0]
for x in student_scores :
  if x > max :
    max = x
 
print(max)