import csv
import pandas as pd
import os

def columns():
    global col_filter
    
    # Reads csv file and data is saved on variable csv_reader
    csv_data = pd.read_csv ('default-inventory.csv')
    
    # Selects them indicated columns -aka ['Dealer ID', 'Stock Number', 'VIN', 'Images']
    col_filter = csv_data[['Dealer ID', 'Stock Number', 'VIN', 'Images']]
    
    # Export data for the 4 columns without an index, includes header
    col_filter.to_csv (r'filtered-columns.csv', index = False, header=True)

    
def selectdid():
    with open('filtered-columns.csv', 'r') as csv_file, open('selectdid.csv', "w", newline='') as new_file:
        csv_reader = csv.DictReader(csv_file)
    
        did = input('Enter Dealer ID: ') #Test DID: 85296
        print ('Filtering for Dealer ID: ' + did)
        
        headers = col_filter.columns
        
        csv_reader = csv.DictReader(csv_file)
        csv_writer = csv.DictWriter(new_file, fieldnames=headers, delimiter='\t')   
        
        csv_writer.writeheader() 
       
        for line in csv_reader:
            if did == line ['Dealer ID']:
                csv_writer.writerow(line)
                continue
        
def sep_images():
    df = pd.read_csv("selectdid.csv", index_col=False, sep='\t', encoding='windows-1252')
    
    df_new = pd.concat([df[['Dealer ID', 'Stock Number', 'VIN']],
                        df['Images'].str.split(',',expand=True).rename(columns = lambda x: f"Images{(x+1)}")],
                       axis=1).fillna('')

    df_new.to_csv('image_urls.csv')


def img_urls():
    df = pd.read_csv("image_urls.csv", index_col=0, encoding='windows-1252')
    urlbeg = '=image("'
    urlend = '")'
    
    df['Images1'] = urlbeg + df['Images1'] + urlend
    df.to_csv('inventory_gsheets.csv', index = False, header=True)
    print ("\nThe file 'inventory_gsheets.csv' was created. Go to Google Sheets and Import CSV to view the first image of every vehicles for selected dealer.\n")

def remove_excess():
    os.remove("filtered-columns.csv")
    os.remove("selectdid.csv")
    os.remove("image_urls.csv")
        
columns()
selectdid()
sep_images()
img_urls()
remove_excess()
