from BankAccount import BankAccount

class Main:

    @staticmethod
    def run():

        account = BankAccount("ACC001", "Suriyaa S", 19, 10831.0, "Savings")

        account.deposit(1000)
        account.deposit(2500)       

        account.withdraw(500, None)
        account.withdraw(300, None)

        account.print_statement()


if __name__ == "__main__":
    Main.run()
