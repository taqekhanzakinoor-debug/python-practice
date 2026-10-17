def analyze(marks):
    if not marks:
        print("No marks to analyze")
        return
    total=sum(marks)
    avg=total /len(marks)
    if avg>90:
        print("Excellent")
    elif avg>70:
        print("Normal")
    elif avg> 50:
        print("Needs improvement ")
    else:
        print("Bad Result")
    for mark in marks:
        print(mark)
    print("Totall:",total)
    print("Average:",round(avg, 2))
    print("Highest:",max(marks))
    print("Lowest:",min(marks))
student_marks=[40,80,90,100,50]
analyze(student_marks)
analyze([95,98, 100])
analyze([10,20,30])
analyze([])