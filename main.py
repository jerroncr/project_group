import overheads, cash_on_hand, profit_loss

def main():
    '''
    - IMPORTING ALL FUNCTIONS FROM ALL FILES
    - IMPORTED FUNCTIONS WOULD PRINT THEIR RESULTS INTO TXT FILE
    '''
    overhead_result = overheads.overhead_function()
    cash_on_hand_results = cash_on_hand.cash_on_hand_function()
    profit_loss_results = profit_loss.profit_loss_function()

    return overhead_result,cash_on_hand_results,profit_loss_results
