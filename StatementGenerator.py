#Statement

class StatementGenerator:

    def generate(self, account):

        print(
            f"---- Statement for Account #{account.account_number} "
            f"({account.name}) ----"
        )

        for entry in account.transaction_log:
            print(entry)

        print(f"Current Balance: Rs. {account.balance}")

        print(
            "-----------------------------------------------------"
        )


