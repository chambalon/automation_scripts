import csv

new_row = ['CUST003','Noah','Williams','Brisbane Solutions','noah.williams@brisbane.solutions.net','Brisbane','Australia']
with open('customers.csv', 'a', newline='') as csvfile:
  csv_writer = csv.writer(csvfile)
  csv_writer.writerow(new_row)
