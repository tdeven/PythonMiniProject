from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

data = [
    ["Date", "Name", "Subscription", "Price (Rs.)"],
    [
        "15/12/2023",
        "Devendra Thakur",
        "LifeTime",
        "10,200.00"
    ],
    ["12/12/2022", "Rajesh", "one year", "635.010"],
    ["Sub Total","","","20000.000"],
    ["Discount","","","3000.00"],
    ["Total","","","17000.10"]
]



# def data(date,name,subcription,price):
#     print("Today Date", date)
#     print("Customer Name:",name)
#     print("Subsciption:", subcription)
#     print("Amount:",price)

# data(name="Tommy", date=2023/12/12, subcription="Nothing", price=120000.000)

# Date = 2023/12/25
# Name=input("Enter the customer name:")
# Subscription=input("Enter the subcription:")
# price=float(input("Enter the amount:"))



pdf = SimpleDocTemplate("receipt11.pdf", pagesizes=A4)

style=getSampleStyleSheet()
title_style = style["Heading1"]
title_style.alignment = 1

title = Paragraph("Devendra", title_style)

style = TableStyle(
     [ 
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
    ] 
)

table = Table(data, style= style)

pdf.build([title, table])