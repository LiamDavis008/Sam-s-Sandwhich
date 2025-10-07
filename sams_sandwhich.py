import datetime
#Sam's Sandwhich
def bread_selection():
    bread_list =["White", "Brown","Italian","Granary"]
    count = 0
    print("We have the following breads:")
    while count < len(bread_list):#prints out each item on the list
        print(count+1," ", bread_list[count])
        count +=1
    bread_selected=int(input("Which bread did you want? Enter a number"))
    return bread_list[bread_selected-1]

def meats():
    meat_list = ["No meat", "kangaroo","Unicorn", "Yak"]
    count = 0
    print("We have the following meat options:")
    while count < len(meat_list):#prints out each item on the list
        print(count+1," ", meat_list[count])
        count +=1
    meat_selected=int(input("Which meat did you want? Enter a number"))
    return meat_list[meat_selected-1]

def cheese():
    cheese_list = ["No cheese","Carefully Raw Milk Cheese","Pitchfork Sommerset Cloth Wrapped Cheddar Cheese","Kraft Cheese"]
    count = 0
    print("we have the following cheese options:")
    while count < len(cheese_list):
        print(count+1," ", cheese_list[count])
        count +=1
    cheese_selected=int(input("Which cheese did you want? Enter a number"))
    return cheese_list[cheese_selected-1]

def sauce():
    sauce_list = ["Smorgaskaviar"]   
    count = 0
    print("we have the following sauce options") 
    while count < len(sauce_list):
        print(count+1," ", sauce_list[count])
        count +=1
    sauce_selected = int(input("Which cheese did you want? Enter a number"))
    return sauce_list[sauce_selected-1]

def salad():
    salad_list = ["Lettuce", "Tomato", "Carrot", "Cucumber", "Onions"]
    count = 0
    print("We have the following salads, you can have as many as you want")
    while count <len(salad_list):
        print(count+1, " ", salad_list[count])
        count +=1 
    print("press enter when you have finished choosing your salads")
    salads_added = ""
    selected_salad = " "

    while selected_salad != "":
        selected_salad = input(f"What number salad do you want?\nYou have selected: {salads_added}")
        if selected_salad != "":
            selected_salad = int(selected_salad)
            salads_added = salads_added + " " + salad_list[selected_salad-1]
    return salads_added.strip()
def textfile(name, cell, today, sandwhihc_order):
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

#main program
print("welcome to Sam's Sandwhich Shop")
name=input("what is your name?")
cell=input("what is your phone number")
bread_choice=bread_selection()
meat_choice=meats()
cheese_choice=cheese()
salad_choice=salad()
sauce_choice=sauce()
sandwhich_order=[]
today=datetime.datetime.now()
sandwhich_order.append(bread_choice)
sandwhich_order.append(meat_choice)
sandwhich_order.append(cheese_choice)
sandwhich_order.append(sauce_choice)
sandwhich_order.append(salad_choice)
textfile(name, cell, today, sandwhich_order)