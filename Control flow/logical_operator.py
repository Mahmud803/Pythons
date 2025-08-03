high_income=False
good_income=True
student=False

if high_income and good_income:
    print("eligible")
else:
    print("not eligible")   

if high_income or good_income:
    print("eligible")
else:
    print("not eligible")   


if not student:
    print("eligible")
else:
    print("not eligible")   


if (high_income or good_income) and not student:
    print("eligble")
else:
    print("not eligible")    