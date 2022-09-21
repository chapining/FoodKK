import cgi

content = cgi.FieldStorage()

print("Content-type: text/html\n")
print("<head>")
print("<meta charset='windows-1251'>")
print("</head>")
sex = content.getfirst("sex")
print(content.getfirst("sex"))
age = content.getfirst("age")
print(content.getfirst("age"))
weight = content.getfirst("weight")
print(content.getfirst("weight"))
height = content.getfirst("height")
print(content.getfirst("height"))
activity = content.getfirst("activity")
print(content.getfirst("activity"))

if sex = "М":
	foodKK = (5 + (10 × weight) + (6,25 × height) − (5 × age)) * activity
elif sex = "Ж"
	foodKK = ((10 × weight) + (6,25 × height) − (5 × age) – 161) * activity

print(foodKK)