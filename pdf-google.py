import requests
import urllib.parse
import pandas as pd

"""
https://www.codementor.io/@garethdwyer/create-pdf-files-from-templates-with-python-and-google-scripts-p63kal1vb
"""

url = "https://script.google.com/macros/s/AKfycbwWSdgAyjmbQ-ezQq5u5bFViDbFGdYt1fWmcpH5e8nWTzbFQM9i/exec?"

payments = pd.read_csv('tutor_payments.csv')

for idx,row in payments.iterrows():
    invoice_id = str(row[0])
    tutor_name = row['TutorName']
    tutor_id_number = row['CourseId']
    course_name = row['CourseName']
    total_revenue = str(round(row['NetRevenue'],2))
    tutor_revenue = str(round(int(row['NetRevenue'])*0.4,2)) + ' €'
    tax_amount = str(round(int(row['NetRevenue'])*0.4*0.15,2)) + ' €'
    tutor_payment = str(round(int(row['NetRevenue'])*0.4,2) - round(int(row['NetRevenue'])*0.4*0.15,2)) + ' €'

    print("processing ", invoice_id)
    payload = {"invoice_id": invoice_id, 
        "tutor_name": tutor_name,
        "tutor_id_number": tutor_id_number,
        "course_name": course_name,
        "total_revenue": total_revenue,
        "tutor_revenue": tutor_revenue,
        "tax_amount": tax_amount,
        "tutor_payment": tutor_payment}

    u = url + urllib.parse.urlencode(payload)
    response = requests.get(u)
    print("file generated")
    response = requests.get(response.content)
    print(response.content)
    print("file downloaded")
    with open("invoice{}.pdf".format(invoice_id), "wb") as f:
        f.write(response.content)