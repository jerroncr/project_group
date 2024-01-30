def cash_on_hand_function():
    '''
    - EXTRACTING ALL DATA FROM CSV FILE, WHERE THERE IS A DEFFICIT FROM THE PREVIOUS DAY, SEPERATING THEM TO 4 CATEGORY (ALL DEFICITS, HIGHEST, 2ND HIGHEST AND 3RD HIGHEST)
    - APPENDING 4 CATEGORY OF DEFICITS FUNCTIONS TO TXT FILE
    '''

    from pathlib import Path
    import csv
    
    # READ CSV FILE, APPEND DATA FROM CSV FILE TO NEW LIST
    coh_fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"
    with coh_fp.open(mode="r", encoding="UTF-8", newline="") as file: 
        reader = csv.reader(file)
        next(reader)
        coh = []
        for row in reader:
            coh.append([row[0],row[1]])

    # CONVERSION FROM STRING TO INTEGER
    for string in coh:
        string[0] = int(string[0])
        string[1] = int(string[1])
    
    def deficit_coh():
        '''
        - EXTRACTING ALL DATA WITHIN LIST WHERE THERE IS A DEFICIT FROM THE PREVIOUS DAY
        - APPENDING EXTRACTED DATA TO NEW LIST
        '''
        # ITERATING NEW LIST FOR ALL DEFICITS
        deficit = []
        previous_amount = 0
        # EXTRACTING AND APPENDING ALL DEFICIT TO NEW LIST
        for day, amount in coh:
            if previous_amount != 0 and amount < previous_amount:
                deficit.append([day,amount])
            previous_amount = amount
        return deficit
    
    # RENAMING DEFICIT FUNCTION
    coh_deficit = deficit_coh()

    def top_1_coh():
        '''
        - EXTRACTING THE DATA WITH THE HIGHEST DEFICIT 
        - APPENDING EXTRACTED DATA TO NEW LIST
        '''
        # ITERATING NEW LIST FOR HIGHEST DEFICIT
        top_1_coh = []
        previous_amount = 0
        # EXTRACTING AND APPENDING ALL DEFICIT TO NEW LIST
        for day, amount in coh:
            if previous_amount != 0 and amount < previous_amount:
                top_1_coh.append([day,amount])
            previous_amount = amount
        # SORTING LIST AND EXTRACTING ONLY THE HIGHEST DEFICIT
        top_1_coh.sort(key = lambda x:x[1], reverse = True)
        return top_1_coh[0:1]
    
    # RENAMING HIGHEST DEFICIT FUNCTION
    coh_top_1 = top_1_coh()

    def top_2_coh():
        '''
        - EXTRACTING THE DATA WITH THE 2ND HIGHEST DEFICIT
        - APPENDING EXTRACTED DATA TO NEW LIST
        '''
        # ITERATING NEW LIST FOR 2ND HIGHEST DEFICIT
        top_2_coh = []
        previous_amount = 0
        # EXTRACTING AND APPENDING ALL DEFICIT TO NEW LIST
        for day,amount in coh:
            if previous_amount != 0 and amount > previous_amount:
                top_2_coh.append( [day,amount])
            previous_amount = amount
        # SORTING LIST AND EXTRACTING ONLY THE 2ND HIGHEST DEFICIT
        top_2_coh.sort(key = lambda x:x[1], reverse = True)
        return top_2_coh[1:2]

    # RENAMING 2ND HIGHEST DEFICIT FUNCTION
    coh_top_2 = top_2_coh()

    def top_3_coh(): 
        '''
        - EXTRACTING THE DATA WITH THE 3RD HIGHEST DEFICIT 
        - APPENDING EXTRACTED DATA TO NEW LIST
        '''
        # ITERATING NEW LIST FOR 3RD HIGHEST DEFICIT
        top_3_coh = []
        previous_amount = 0
        # EXTRACTING AND APPENDING ALL DEFICIT TO NEW LIST
        for day,amount in coh:
            if previous_amount != 0 and amount < previous_amount:
                top_3_coh.append([day,amount])
            previous_amount = amount
        # SORTING LIST AND EXTRACTING ONLY THE 3RD HIGHEST DEFICIT
        top_3_coh.sort(key = lambda x:x[1], reverse = True)
        return top_3_coh[2:3]
    
    # RENAMING 3RD HIGHEST DEFICIT FUNCTION
    coh_top_3 = top_3_coh()

    # ITERATING STRING FOR LIST WITH ALL DEFICITS, FOR LABELLING
    deficit_results = ""

    # LABELLING FOR LIST WITH ALL DEFICIT USING FOR LOOP
    for day, amount in coh_deficit:
        deficit_results += (f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD {amount:,}\n")

    # LABELLING FOR LIST WITH HIGHEST DEFICIT
    for day, amount in coh_top_1:
        top_1_results = f"[HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD {amount:,}\n"

    # LABELLING FOR LIST WITH 2ND HIGHEST DEFICIT
    for day, amount in coh_top_2:
        top_2_results = f"[2ND HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD {amount:,}\n"

    # LABELLING FOR LIST WITH 3RD HIGHEST DEFICIT
    for day, amount in coh_top_3:
        top_3_results = f"[3RD HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD {amount:,}\n"

    # OPENING TXT FILE
    # APPENDING LABELLED LISTS OF ALL DEFICITS, HIGHEST, 2ND HIGHEST AND 3RD HIGHEST DEFICITS INTO FILE 
    with open("summary_report.txt","a") as file:
        file.write(deficit_results)
        file.write(top_1_results)
        file.write(top_2_results)
        file.write(top_3_results)

    return deficit_results, top_1_results, top_2_results, top_3_results

# RENAMING MAIN CASH ON HAND FUNCTION
cash_on_hand_function = cash_on_hand_function()

# PRINT MAIN CASH ON HAND FUNCTION
print(cash_on_hand_function)
