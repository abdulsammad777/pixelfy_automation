import time

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import as_code.automation_script as automation
import logging

main_sheet_url ="https://docs.google.com/spreadsheets/d/19r14YzTIblHyWHcvZMy9upKDYWW6sxKMpI3M30uaC8k/edit#gid=0"

sheet_records = {}

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',filename='app.log')


def update_pixify_urls(url_list, title):
    print("updating urls of list ",url_list)
    print("updating for title",title)
    automation.Login('lap318181@gmail.com', 'ZEV4JY901n7')
    automation.Modify_Tracking_links(url_list, title)




def process_subsheet(sub_sheet,pixify_title):

    urls_list = []
    sub_sheet_row_index = 2
    cell_value = sub_sheet.cell(col=2, row=sub_sheet_row_index).value

    cell_values = sub_sheet.get_all_values()


    for i in range (1,len(cell_values)):
        urls_list.append(cell_values[i][1])

    #while(cell_value!=None):
    #    urls_list.append(cell_value)
    #   sub_sheet_row_index+=1
    #    cell_value = sub_sheet.cell(col=2, row=sub_sheet_row_index).value

    update_pixify_urls(urls_list,pixify_title)


def open_worksheet(sub_sheet , sub_sheets_url):



    worksheet_id = sub_sheets_url.split('=')[1]

    worksheets =  sub_sheet.worksheets()


    for worksheet in worksheets:
        if(worksheet.id ==int(worksheet_id)):
            return sub_sheet.worksheet(worksheet.title)
    x=0


if __name__ == "__main__":
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('pixifybot-86c9ef6c73b9.json', scope)

    # authorize the clientsheet
    client = gspread.authorize(creds)

    logging.warning('Going to Start Script')


    while True:
        time.sleep(15)



        sheet = client.open_by_url(main_sheet_url)

        logging.warning('Opened Main Sheet')

        sheet_instance = sheet.get_worksheet(0)

        sheet_values = sheet_instance.get_all_values()
        sub_sheet_row_index = 2;

        sub_sheets_url = sheet_instance.cell(col=1, row=sub_sheet_row_index).value


        prev_sub_sheet_index = sub_sheet_row_index
        while sub_sheets_url!="" and sub_sheets_url!=None:
            time.sleep(2)
            try:
                prev_sub_sheet_index = sub_sheet_row_index

                enable_check = sheet_instance.cell(col=3, row=sub_sheet_row_index).value

                if(enable_check == "1"):

                    logging.warning('Checking for sheet :'+sub_sheets_url )
                    sub_sheet  = client.open_by_url(sub_sheets_url)


                    sub_sheet = open_worksheet(sub_sheet , sub_sheets_url)



                    sub_sheet_update_date = sub_sheet.cell(col=13, row=2).value
                    sub_sheet_pixify_title = sheet_instance.cell(col=2, row=sub_sheet_row_index).value

                    if sub_sheets_url in sheet_records.keys():

                        if(sheet_records[sub_sheets_url] != sub_sheet_update_date):

                            print("Sheet date changed ",sub_sheets_url)
                            try:
                                process_subsheet(sub_sheet,sub_sheet_pixify_title)
                            except Exception as e:
                                error_msg = 'Issue in Processing Sheet :' + sub_sheets_url + ' :' + str(e)
                                logging.error(error_msg)



                    else:
                        logging.warning('New Sheet Processing for first time :' + sub_sheets_url)
                        sheet_records[sub_sheets_url] = sub_sheet_update_date
                        try :
                            process_subsheet(sub_sheet,sub_sheet_pixify_title)
                        except Exception as e:
                            error_msg = 'Issue in Processing Sheet :' + sub_sheets_url + ' :' + str(e)
                            logging.error(error_msg)

                sub_sheet_row_index += 1
                sub_sheets_url = sheet_instance.cell(col=1, row=sub_sheet_row_index).value

            except Exception as e:

                if(sub_sheet_row_index == prev_sub_sheet_index):
                    sub_sheet_row_index += 1
                error_msg = 'Issue in main Iteration for file :'+sub_sheets_url +' :'+ str(e)
                logging.error(error_msg)