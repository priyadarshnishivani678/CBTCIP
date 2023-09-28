from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
  
DATA = [
    [ "Date" , "Name", "Subscription", "Price (Rs.)" ],
    [
        "15/09/2023",
        "Full Stack Development with JAVA  - Live",
        "2 Year",
        "8,999.00/-",
    ],
    [ "17/08/2023", "Cyber Security", "6 months", "9,999.00/-"],
    [ "05/07/2023", "Data Structure and Algorithm","3 month","15,000.00/-"],
    [ "Sub Total", "", "", "33,998.00/-"],
    [ "Discount", "", "", "-5,000.00/-"],
    [ "Total", "", "", "28,998.00/-"],
]
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 )
  
styles = getSampleStyleSheet()
  
title_style = styles[ "Heading1" ]

title_style.alignment = 1
  
title = Paragraph( "BILL RECEIPT" , title_style )
  
style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.blueviolet ),
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),  
        ("BOTTOMPADDING", (0, 1), (-1, -1), 6), 
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]
)

table = Table( DATA , style = style )
pdf.build([ title , table ])