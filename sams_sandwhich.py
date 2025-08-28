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
    return cheese

        

def vegies():
    salad_list = ["None", "Açaí Palm Hearts", "Aguaje Fruit", "Amaranth Greens", "Arracacha", "Asparagus Pea", "Balsam Apple", "Boniato", "Bottle Gourd", "Broccoflower", "Cactus Pad", "Cardoon", "Cassava Leaves", "Celtuce", "Chayote", "Chrysanthemum Greens", "Cime di Rapa", "Daikon Radish", "Dinosaur Kale", "Ensete", "Fiddlehead Fern", "Galangal", "Gai Lan", "Goji Berry Leaves", "Gourd Luffa", "Horned Melon", "Huacatay", "Jicama", "Kaffir Lime Leaves", "Kohlrabi", "Lemon Grass", "Malabar Spinach", "Moringa", "Nopales", "Oca", "Oysterleaf", "Perilla", "Purslane", "Quinoa Greens", "Radicchio", "Ramps", "Romanesco Broccoli", "Salsify", "Samphire", "Shiso", "Taro Root", "Tepin Peppers", "Tomatillo", "Ube", "Water Chestnut", "Yacón"]
    count = 0
    print("We have the following salads, you can have as many as you want")
    while count <len(salad_list):

#main program
print("welcome to Sam's Sandwhich Shop")
bread_choice=bread_selection()
print(f"Your selected bread: {bread_choice}")
meat_choice=meats()
print(f"Your selected the meat: {meat_choice}")