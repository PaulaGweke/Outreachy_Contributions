import csv
import requests

# create a funtion to get codes of url. Use Error for exceptions
# this first funtion can be adapted for use for both the terminal print and the csv write but
# without the option of the csv Error Msg output option (from what I could deduce)
def codes_only(url):
    try:
        response=requests.get(url)
        return abs(response.status_code)
    except Exception as e:
        return "Error" 


# Create funtion to output status code and url of csv file list. Error files options with or without messages
def check_url_status(url):
    try:
        response=requests.get(url)
        return f"({response.status_code}) {url}"
    except Exception as e:
        return f"(Error) {url}" #cleaner output
        # return f"(Error) Msg Is: {e}: {url}" #alternative to see error messages

#read in csv file with url list and then split into separate lines 
df_csv =  "T347259.csv"
with open(df_csv, "r") as file:
    urls=file.read().splitlines()

status_results = []
for url in urls[1:]: # skip first line/row which is header 
    status = check_url_status(url) # for terminal view purpose
    status_codes = codes_only(url) # for csv write purpose
    status_results.append([status_codes, url]) # for csv write purpose
    print(status) #see terminal results

# ---------------  To write out the result

status_codes = codes_only(url)

df_csv_write = "T347259_status_codes.csv"

with open(df_csv_write, "w", newline="") as csv_f:
    csv_writer = csv.writer(csv_f)
    csv_writer.writerow(["Status", "URL"])
    csv_writer.writerows(status_results)




# Alternate shorter script
# import csv
# import requests

# # create a funtion to get codes of url. Use Error for exceptions
# def codes_only(url):
#     try:
#         response=requests.get(url)
#         return abs(response.status_code)
#     except Exception as e:
#         return "Error" 

# #read in csv file with url list and then split into separate lines 
# df_csv =  "T347259.csv"
# with open(df_csv, "r") as file:
#     urls=file.read().splitlines()

# status_results = []
# for url in urls[1:]: # skip first line/row which is header 
#     status_codes = codes_only(url) 
#     print(f"({status_codes})", url) 

