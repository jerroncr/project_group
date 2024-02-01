def profit_loss_function():
    '''
    - EXTRACTING ALL DATA FROM CSV FILE, WHERE THERE IS A DEFICIT FROM THE PREVIOUS DAY, SEPARATING THEM TO 4 CATEGORY (ALL DEFICIT, HIGHEST, 2ND HIGHEST AND 3RD HIGHEST)
    - APPENDING 4 CATEGORY OF DEFICIT FUNCTIONS TO TXT FILE    
    '''
    from pathlib import Path
    import csv

    # READ CSV FILE, APPEND DATA FROM CSV FILES TO NEW LIST
    pnl_fp = Path.cwd() / "csv_reports" / "Profits_and_Loss.csv"
    with pnl_fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        next(reader)
        pnl = []
        for row in reader: 
            pnl.append([row[0],row[1],row[2],row[3],row[4]])
    
    # REMOVE THE OBSOLETE DATA AND RETAIN ONLY THE IMPORTANT ONES
    for item in pnl:
        item[1:4] = []
    
    # CONVERSION FROM STRING TO INTEGER
    for string in pnl:
        string[0] = int(string[0])
        string[1] = int(string[1])

    def deficit_pnl():
        '''
        - EXTRACTING ALL DATA WITHIN LIST WHERE THERE IS A DEFICIT FROM THE PREVIOUS DAY
        - APPENDING EXTRACTED DATA TO NEW LIST
        '''
        # ITERATING NEW LIST FOR ALL DEFICITS
        deficit = []
        # CHECK IF AMOUNT THE DAY AFTER HAS A DEFICIT FROM THE DAY BEFORE
        for i in range(1,len(pnl)):
            if pnl[i][1] < pnl[i-1][1]:
                # CALCULATING THE DIFFERENCE
                difference = pnl[i-1][1] - pnl[i][1]
                # APPENDING THE DAY AND DIFFERENCE TO THE NEW LIST
                deficit.append([pnl[i][0],difference])
        return deficit
    
    # RENAMING ALL DEFICIT FUNCTION
    pnl_deficit = deficit_pnl()

    def top_1_pnl():
        '''
        - EXTRACTING THE DATA WITH THE HIGHEST DEFICIT
        - APPENDING THE EXTRACTED DATA TO NEW LIST
        '''
        # ITERATING NEW LIST FOR HIGHEST DEFICIT FUNCTION
        top_1_pnl = []
        # CHECK IF AMOUNT THE DAY AFTER HAS A DEFICIT FROM THE DAY BEFORE
        for i in range(1,len(pnl)):
            if pnl[i][1] < pnl[i-1][1]:
                # CALCULATING THE DIFFERENCE
                difference = pnl[i-1][1] - pnl[i][1]
                # APPENDING THE DAY AND DIFFERENCE TO THE NEW LIST
                top_1_pnl.append([pnl[i][0], difference])
        # ITERATING SORTING FUNCTION BASED ON THE 2ND NUMBER IN THE LSIT
        def sort_pnl(item):
            return item[1]
        # EXTRACTING ONLY THE HIGHEST DEFICIT
        top_1_pnl.sort(key = sort_pnl, reverse = True)
        return top_1_pnl[0:1]
    
    # RENAMING HIGHEST DEFICIT FUNCTION
    pnl_top_1 = top_1_pnl()
    
    def top_2_pnl():
        '''
        - EXTRACTING THE DATA WITH THE 2ND HIGHEAT DEFICIT
        - APPENDING EXTRACTED DATA TO NEW LIST
        '''
        # ITERATING NEW LIST FOR HIGHEST DEFICIT FUNCTION
        top_2_pnl = []
        # CHECK IF AMOUNT THE DAY AFTER HAS A DEFICIT FROM THE DAY BEFORE
        for i in range(1,len(pnl)):
            if pnl[i][1] < pnl[i-1][1]:
                # CALCULATING THE DIFFERENCE
                difference = pnl[i-1][1] - pnl[i][1]
                # APPENDING THE DAY AND DIFFERENCE TO THE NEW LIST
                top_2_pnl.append([pnl[i][0], difference])
        # ITERATING SORTING FUNCTION BASED ON THE 2ND NUMBER IN THE LIST
        def sort_pnl(item):
            return item[1]
        # EXTRACTING ONLY THE 2ND HIGHEST DEFICIT
        top_2_pnl.sort(key = sort_pnl, reverse = True)
        return top_2_pnl[1:2]

    # RENAMING 2ND HIGHEST DEFICIT FUNCTION
    pnl_top_2 = top_2_pnl()

    def top_3_pnl():
        '''
        - EXTRACTING THE DATA WITH THE 3RD HIGHEST DEFICIT
        - APPENDING EXTRACTED DATA TO NEW LIST
        '''
        # ITERATING NEW LIST FOR HIGHEST DEFICIT FUNCTION
        top_3_pnl = []
        # CHECK IF AMOUNT THE DAY AFTER HAS A DEFICIT FROM THE DAY BEFORE
        for i in range(1,len(pnl)):
            if pnl[i][1] < pnl[i-1][1]:
                # CALCULATING THE DIFFERENCE
                difference = pnl[i-1][1] - pnl[i][1]
                # APPENDING THE DAY AND DIFFERENCE TO THE NEW LIST
                top_3_pnl.append([pnl[i][0], difference])
        # ITERATING SORTING FUNCTION BASED ON THE 2ND NUMBER IN THE LIST
        def sort_pnl(item):
            return item[1]
        # EXTRACTING ONLY THE 3RD HIGHEST DEFICIT
        top_3_pnl.sort(key=sort_pnl, reverse = True)
        return top_3_pnl[2:3]
    
    # RENAMING 3RD HIGHEST DEFICIT FUNCTION
    pnl_top_3 = top_3_pnl()

    # ITERATING STRING FOR LIST WITH ALL DEFICITS, FOR LABELLING
    deficit_results = ""

    # LABELLING FOR LIST WITH ALL DEFICITS USING FOR LOOP
    for day, amount in pnl_deficit:
        deficit_results += (f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD {amount:,}\n")
    
    # LABELLING FOR LIST WITH HIGHEST DEFICIT
    for day, amount in pnl_top_1:
        top_1_results = f"[HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD {amount:,}\n"
    
    # LABELLING FOR LIST WITH 2ND HIGHEST DEFICIT
    for day, amount in pnl_top_2:
        top_2_results = f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD {amount:,}\n"
    
    # LABELLING FOR LIST WITH 3RD HIGHEST DEFICIT
    for day, amount in pnl_top_3:
        top_3_results = f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD {amount:,}\n"

    # OPENING TXT FILE
    # APPENDING LABELLED LISTS OF ALL DEFICITS, HIGHEST, 2ND HIGHEST AND 3RD HIGHEST DEFICITS INTO FILE
    with open("summary_report.txt",mode = "a", encoding = "UTF-8") as file:
        file.write(deficit_results)
        file.write(top_1_results)
        file.write(top_2_results)
        file.write(top_3_results)
    
    return deficit_results,top_1_results,top_2_results,top_3_results


# RENAMING MAIN PROFIT AND LOSS FUNCTION
profit_loss_function = profit_loss_function()

# PRINT MAIN PROFIT AND LOSS FUNCTION
print(profit_loss_function)
