choice = input("Enter USSD *311#, *312#, or *303#: ")

ussd = ["*311#", "*312#", "*303#"]

if choice in ussd:
    select_service_provider = input(
        "SIM 1: GLO\nSIM 2: MTN\nSIM 3: Airtel\nSelect SIM: "
    )

    if select_service_provider == "sim 1" or select_service_provider == "1":
        option = input(
            "What would you like to do?\n"
            "1. Voice plans\n"
            "2. Buy Data\n"
            "3. Check Tariff plans\n"
            "4. Data Gifting\n"
            "Select option: "
        )

        if option == "2":
            print("Data Plans")
            plan_type = input(
                "1. Daily\n"
                "2. Weekly\n"
                "3. Monthly\n"
                "Select plan type: "
            )

            # DAILY PLANS
            if plan_type == "1":
                daily_plan = input(
                    "Daily Plans\n"
                    "1. 75MB - ₦100\n"
                    "2. 200MB - ₦200\n"
                    "3. 350MB - ₦300\n"
                    "Select option: "
                )

                if daily_plan == "1":
                    confirm = input(
                        "Purchase 75MB for ₦100?\n"
                        "1. Confirm\n2. Cancel\n"
                    )
                    if confirm == "1":
                        print("You have successfully purchased 75MB.")
                    else:
                        print("Purchase cancelled.")

                elif daily_plan == "2":
                    confirm = input(
                        "Purchase 200MB for ₦200?\n"
                        "1. Confirm\n2. Cancel\n"
                    )
                    if confirm == "1":
                        print("You have successfully purchased 200MB.")
                    else:
                        print("Purchase cancelled.")

                elif daily_plan == "3":
                    confirm = input(
                        "Purchase 350MB for ₦300?\n"
                        "1. Confirm\n2. Cancel\n"
                    )
                    if confirm == "1":
                        print("You have successfully purchased 350MB.")
                    else:
                        print("Purchase cancelled.")

                else:
                    print("Invalid daily plan.")

            # WEEKLY PLANS
            elif plan_type == "2":
                weekly_plan = input(
                    "Weekly Plans\n"
                    "1. 750MB - ₦500\n"
                    "2. 1.5GB - ₦1000\n"
                    "Select option: "
                )

                if weekly_plan == "1":
                    confirm = input(
                        "Purchase 750MB for ₦500?\n"
                        "1. Confirm\n2. Cancel\n"
                    )
                    if confirm == "1":
                        print("You have successfully purchased 750MB.")
                    else:
                        print("Purchase cancelled.")

                elif weekly_plan == "2":
                    confirm = input(
                        "Purchase 1.5GB for ₦1000?\n"
                        "1. Confirm\n2. Cancel\n"
                    )
                    if confirm == "1":
                        print("You have successfully purchased 1.5GB.")
                    else:
                        print("Purchase cancelled.")

                else:
                    print("Invalid weekly plan.")

            # MONTHLY PLANS
            elif plan_type == "3":
                monthly_plan = input(
                    "Monthly Plans\n"
                    "1. 2GB - ₦1500\n"
                    "2. 5GB - ₦3500\n"
                    "3. 10GB - ₦5500\n"
                    "Select option: "
                )

                if monthly_plan == "1":
                    confirm = input(
                        "Purchase 2GB for ₦1500?\n"
                        "1. Confirm\n2. Cancel\n"
                    )
                    if confirm == "1":
                        print("You have successfully purchased 2GB.")
                    else:
                        print("Purchase cancelled.")

                elif monthly_plan == "2":
                    confirm = input(
                        "Purchase 5GB for ₦3500?\n"
                        "1. Confirm\n2. Cancel\n"
                    )
                    if confirm == "1":
                        print("You have successfully purchased 5GB.")
                    else:
                        print("Purchase cancelled.")

                elif monthly_plan == "3":
                    confirm = input(
                        "Purchase 10GB for ₦5500?\n"
                        "1. Confirm\n2. Cancel\n"
                    )
                    if confirm == "1":
                        print("You have successfully purchased 10GB.")
                    else:
                        print("Purchase cancelled.")

                else:
                    print("Invalid monthly plan.")

            else:
                print("Invalid plan type.")

        elif option == "3":
            print("Your current data balance is 1.2GB.")

        elif option == "4":
            print("Data gifting service selected.")

        elif option == "1":
            print("Voice plans selected.")

        else:
            print("Invalid service option.")

    else:
        print("This SIM provider is not implemented yet.")

else:
    print("Invalid USSD code.")