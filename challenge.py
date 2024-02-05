import gspread
from google.oauth2 import service_account
from tabulate import tabulate
import re

credentials_path = 'path.json'   # the location of the file containing Google Cloud API credentials


credentials = service_account.Credentials.from_service_account_file(
    credentials_path,
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)


spreadsheet_id = '1fzIWOfkKeJX-762x99IxfdOz19S64hypM9hCNI0x6VU'   # the spreadsheet ID, which can be found between the characters '/d/' and '/edit...' in the URL


gc = gspread.authorize(credentials)                 # call a method to authorize, passing the credentials as an argument
sheet = gc.open_by_key(spreadsheet_id).sheet1       # opening the spreadsheet using its ID


table_main = sheet.get_all_values()    # show the table


title = table_main[0]         # obtaining the title from the spreadsheet
classes = table_main[1]       # obtaining the total of classes from the spreadsheet
headers = table_main[2]       # obtaining the headers from the spreadsheet
data = table_main[3:]         # obtaining the data from the spreasheet


print(f"{title}\n{classes}")                    # representation of the table
print(tabulate(data, headers=headers, tablefmt='pretty'))   # table formatting/organization for console display

number_pattern = r'\d+'     # remove everything that is not a number

all_classes_number = re.findall(number_pattern, classes[0])


for i, data in enumerate(data[0:], start=4):  
    absences = int(data[2])
    average = round((int(data[3]) + int(data[4]) + int(data[5])) / 30)    # calculation for the average of grades
    

    if absences > (0.25 * int(all_classes_number[0])):   # if the student fails due to absence, will execute this block
        sheet.update_cell(i, 7, "Reprovado por falta")
        sheet.update_cell(i, 8, 0)


    elif average < 5:                                   # if the student fails due to grades, will execute this block
        sheet.update_cell(i, 7, "Reprovado por nota")    
        sheet.update_cell(i, 8, 0)


    elif 5 <= average < 7:                              # if the student needs to take the final exam, it will execute this block
        naf = max(0, 10 - average)
        sheet.update_cell(i, 7, "Exame Final")          
        sheet.update_cell(i, 8, round(naf))


    elif average >= 7:                                  # if the student passes, doesn't need to take the final exam, and is within the absence limit, it will execute this block 
        sheet.update_cell(i, 7, "Aprovado")  
        sheet.update_cell(i, 8, 0)
 