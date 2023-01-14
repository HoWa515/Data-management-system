import json

card_list = []


def read_info():
    with open("data_info.txt") as f:
        dict_list = json.load(f)
        return dict_list


def write_info(dict_list):
    with open("data_info.txt", 'w') as f:
        json.dump(dict_list, f)


def show_menu():
    """show menu"""
    print('-' * 50)
    print("Welcome to use card management system")
    print("1.Add new card", end='\t\t')
    print("2.Display all cards", end='\t\t')
    print("3.Search card", end='\t\t')
    print("0.Exit system")
    print('*' * 50)


def add_card():
    """ add new"""
    print('-' * 50)
    print("add new card")
    name_str = input("enter name: ")
    phone_str = input("enter phone: ")
    email_str = input("enter email: ")
    # create dict to store card
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "email": email_str}
    card_list.append(card_dict)
    print("%s card added" % name_str)

    # choose to add more or not
    choose = input("add more? 1 -yes, 0 -no : ")
    if choose == '1':
        add_card()
    elif choose == '0':
        return


def show_all():
    """ show all cards"""
    print('-' * 50)
    # if table is empty, ask user to add
    if len(card_list) == 0:
        print("No card exists.")
        select = input("add new card? 1 -yes, 0 -no : ")
        if select == '1':
            add_card()
        elif select == '0':
            return

    # not empty, print the table
    for name in ["name", "phone", "email"]:
        print(name, end="\t\t")

    print('')
    print("=" * 50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s" % (card_dict["name"],
                                  card_dict["phone"],
                                  card_dict["email"]))


def search_card():
    """ search cards"""
    print('-' * 50)
    print("search card")
    # name to be searched
    find_name = input("Enter the name to be searched: ")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("name\t\tphone\t\temail")
            print("=" * 50)
            print("")
            print("%s\t\t%s\t\t%s" % (card_dict["name"],
                                      card_dict["phone"],
                                      card_dict["email"]))
            # here can call modify and delete ,call deal function
            deal_card(card_dict)
            break
    else:
        print("Sorry, %s not found " % find_name)


def deal_card(find_dict):
    # modify/delete find_dict
    action_str = input("[1] for modify, [2] for delete, [0] back")
    if action_str == '1':
        find_dict["name"] = input_card(find_dict["name"], "new name:(enter to skip)")
        find_dict["phone"] = input_card(find_dict["phone"], "new phone:(enter to skip)")
        find_dict["email"] = input_card(find_dict["email"], "new email:(enter to skip)")
        print("Card modified")

    elif action_str == '2':
        card_list.remove(find_dict)
        print("Card deleted!")


def input_card(dict_value, tip_message):
    # user type in
    result_str = input(tip_message)
    # if user typed , change value
    if len(result_str) > 0:
        return result_str
    # if user didn't type ,return original value
    else:
        return dict_value



