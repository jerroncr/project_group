def overhead_function():
    '''
    - EXTRACTING ALL DATA FROM CSV FILE, THE HIGHEST OVERHEAD 
    - WRITING THE HIGHEST OVERHEAD INTO A TXT FILE
    '''
    from pathlib import Path 
    import csv 

# READ CSV FILE, APPEND DATA FROM CSV FILE TO NEW LIST 
    fp = Path.cwd() / 'csv_reports' / 'Overheads.csv'
    with fp.open(mode='r', encoding='UTF-8', newline="") as file:
        reader = csv.reader(file)
        next(reader)
        overheads = []
        for row in reader:
            overheads.append([row[0], row[1]])

# CONVERSATION TO UPPERCASE AND FROM STRING TO INTEGER
    for item in overheads: 
        item[0] = item[0].upper()
        item[1] = float(item[1])

    
    def highest_overhead():
        '''
        - EXTRACTING ONLY THE DATA WITH THE HIGHEST OVERHEAD 
        - APPENDING EXTRACTED DATA TO NEW LIST 
        '''
        # ITERATING NEW LIST FOR HIGHEST OVERHEAD 
        highest_overhead = []
        expense = 0 
        # EXTRACTING AND APPENDING THE HIGHEST OVERHEAD TO NEW LIST 
        for name,amount in overheads:
            if amount > expense:
                highest_overhead = [[name,amount]]
                expense = amount 
        return highest_overhead
    
    # RENAMING HIGHEST OVERHEAD FUNCTION 
    highest_overhead = highest_overhead()

    # LABELLING FOR LIST WITH HIGHEST OVERHEAD 
    for name, amount in highest_overhead:
        result = (f'[HIGHEST OVERHEAD] {name}: {amount:,}%\n')

    # OPENING TXT FILE AND WRITING HIGHEST OVERHEAD INFO FILE 
    with open('summary_report.txt', 'w') as file:
        file.write(result)

    return highest_overhead

# RENAMING MAIN OVERHEAD FUNCTION 
overhead_function = overhead_function()

# PRINT MAIN OVERHEAD FUNCTION
print(overhead_function)