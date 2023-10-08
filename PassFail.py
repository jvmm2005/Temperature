E1 = float(input("First exam (0-100):"))
E2 = float(input("Second exam (0-100):"))
E3 = float(input("Third exam (0-100):"))
Media_exámenes = ((E1+E2+E3)/3)
asist = float(input("Enter attendance (0-40):"))
number_of_classes = 40
NumberAsist = (100*asist/number_of_classes)
if (Media_exámenes >= 70 and NumberAsist >= 80):
    print ("¡You passed the exam!... NOW USE YOUR REAL MARKS!!!")
else:
    print ("You failed :_( _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _and will never pass HAHAHAH")