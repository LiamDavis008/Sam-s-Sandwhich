#library imports 
import datetime
#Sam's Sandwhich
#function to force the user to input a valid name
def force_name(message,lower,upper):#defines the function
    while True: # this is a infinate loop.
        name=str(input(message)).title() #asking for and storing the users name and adding a captial letter to the first character
        if len(name)>=lower and len(name)<=upper and name.isalpha(): 
            break
        else:
            print("Invalid name")
    return name #outputs a valid name back to the variable
#function to force user to input a valid number
def force_number(message,lower,upper):
    while True:
        try:
            num=int(input(message))
            if num>=lower and num<=upper:
                break
            else:
                print(f"invalid number please enter in {lower} - {upper}")
        except:
            print("error - only type in numbers please")
    return num
#function to force cellphone number
def cell_num(message, lower, upper):
    while True:
        cell=str(input(message))
        if len(cell) >= lower and len(cell) <= upper and cell.isnumeric():
            break
        else:
            print(f"Error!, please enter between {lower} - {upper}")
    return cell
#funciton for the user to pick bread option
def bread_selection():
    bread_list =["White", "Brown","Italian","Granary"]
    print_list(bread_list,"breads")
    bread_selected=force_number("Which bread did you want? Enter a number",1,len(bread_list))
    return bread_list[bread_selected-1]
#funciton for the user to pick meat option 
def meats():
    meat_list = ["No meat", "kangaroo","Unicorn", "Yak"]
    print_list(meat_list,"meat")
    meat_selected=force_number("Which meat did you want? Enter a number",1,len(meat_list))
    return meat_list[meat_selected-1]
#function for the user to pick cheese options 
def cheese():
    cheese_list = ["No cheese","Carefully Raw Milk Cheese","Pitchfork Sommerset Cloth Wrapped Cheddar Cheese","Kraft Cheese"]
    print_list(cheese_list, "cheese")
    cheese_selected=force_number("Which cheese did you want? Enter a number",1,len(cheese_list))
    return cheese_list[cheese_selected-1]
#function for the user to pick sauce options 
def sauce():
    sauce_list = ["Smorgaskaviar"]   
    print_list(sauce_list,"sauce")
    sauce_selected = force_number("Which cheese did you want? Enter a number",1,len(sauce_list))
    return sauce_list[sauce_selected-1]
#function for the user to pick salad toppings
def salad():
    salad_list = ["Lettuce", "Tomato", "Carrot", "Cucumber", "Onions"]
    print_list(salad_list,"salad")
    print("press enter when you have finished choosing your salads")
    salads_added = ""
    selected_salad = " "

    while selected_salad != "":
        selected_salad = input(f"What number salad do you want?\nYou have selected: {salads_added}")
        if selected_salad != "":
            selected_salad = int(selected_salad)
            salads_added = salads_added + " " + salad_list[selected_salad-1]
    return salads_added.strip()
#function to make code robust and remove the constant while lists that print out otions 
def print_list(list, item):
    count = 0
    print(f"We have the following {item}, ")
    while count <len(list):
        print(count+1, " ", list[count])
        count +=1 
    return

#text file creats/opens a text file and prints sandwhich order
def textfile(name, cell, today, sandwhich_order):
    outF=open("sams_sandwhich.txt","a")
    print(f"\n***Order for {name} - {cell}***")
    outF.write(f"\n Date of Order:{today}")
    for item in sandwhich_order:
        print(item)
        outF.write(f"\n {item}")
    print(f"*** END OF ORDER: ***")
    outF.write("\n")
    outF.write("\n")
    outF.close()

def main():#main function 
    print("welcome to Sam's Sandwhich Shop")#intro print
    name=force_name("what is your name?",2,15)#forces the user to input a valid name 2,15 charaters in length
    cell=cell_num("what is your phone number",9,12)#forces a phone number 9 - 12 characters in length
    #gets the user to choice there sandwhich options
    bread_choice=bread_selection()
    meat_choice=meats()
    cheese_choice=cheese()
    salad_choice=salad()
    sauce_choice=sauce()
    sandwhich_order=[]
    
    today=datetime.datetime.now()#gets the current date
    #appends all the sandwhich options to a list
    sandwhich_order.append(f"{bread_choice} bread")
    sandwhich_order.append(f"{meat_choice} Meat")
    sandwhich_order.append(f"{cheese_choice} Cheese")
    sandwhich_order.append(f"{salad_choice} salad")
    sandwhich_order.append(f"{sauce_choice} sauce")
    textfile(name, cell, today, sandwhich_order)# calls the textfile funciton to print to a text file

#main program
main()