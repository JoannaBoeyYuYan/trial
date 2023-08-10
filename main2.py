from pathlib import Path
import csv 
import overheads 
# import cash_on_hand 
# import profit_and_loss 

def main(): 
    highest_category, max_overhead  = overheads.overheads_function() 
    # cash_on_hand_output = cash_on_hand.cash_on_hand_function() 
    # profit_and_loss.profit_and_Loss_function()

    # Create a path object for summary_report.txt
    fp = Path.cwd() / "summary_report.txt" 
    fp.touch()   
    # Open the file for writing    
    with fp.open(mode='w', encoding='UTF-8', newline="") as file:
        file.write(f"[HIGHEST OVERHEAD] {highest_category}: {max_overhead} % \n" )

        # for result in cash_on_hand_output:
        #     flag, day, amount = result
        #     cash_line = f"[CASH {flag}] DAY: {day}, AMOUNT: USD {amount}\n"
        #     file.write(cash_line)

            
# if __name__ == "__main__":
#     main()

main()