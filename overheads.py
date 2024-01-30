def overhead_function():
    '''
    - EXTRACTING ALL DATA FROM CSV FILE, THE HIGHEST OVERHEAD 
    - WRITING THE HIGHEST OVERHEAD INTO A TXT FILE
    '''
    from pathlib import Path 
    import csv 

    fp = Path.cwd() / 'csv_reports' / 'Overheads.csv'
    with fp.open(mode='r', encoding='UTF-8', newline="") as file:
        reader = csv.reader(file)
        next(reader)
        overheads = []
        for row in reader:
            overheads.append([row[0], row[1]])

        for item in overheads: 
            item[0] = item[0].upper()
            item[1] = float(item[1])

        # print(overheads)
    def highest_overhead():
        highest_overhead = []
        expense = 0 
        for name,amount in overheads:
            if amount > expense:
                highest_overhead = [[name,amount]]
                expense = amount 
        return highest_overhead
        
    highest_overhead = highest_overhead()

    for name, amount in highest_overhead:
        result = (f'[HIGHEST OVERHEAD] {name}: {amount:,}%\n')

    with open('summary_report.txt', 'w') as file:
        file.write(result)

    return highest_overhead
    
overhead_function = overhead_function()

print(overhead_function)