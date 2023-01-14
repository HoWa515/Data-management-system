import tools
# read the stored data into card_list
tools.card_list = tools.read_info()

while True:

    # display actions
    tools.show_menu()

    action_str = input("Choose an option:")
    print("Choose action is:[%s]" % action_str)

    if action_str in ['1', '2', '3']:
        # add new card
        if action_str == '1':
            tools.add_card()
        # display all cards
        if action_str == '2':
            tools.show_all()
        # search cards
        if action_str == '3':
            tools.search_card()
        pass
    # Exit system
    elif action_str == '0':
        tools.write_info(tools.card_list)
        print("Thanks for using, bye.")
        break
    else:
        print("Input incorrect, choose again")
