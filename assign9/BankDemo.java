import java.util.ArrayList;
import java.util.Scanner;

// Base class
class Account {
    private String accountNumber;
    private String ownerName;
    private double balance;

    // Constructor chaining
    public Account() {
        this("Unknown", "Unknown", 0.0);
    }

    public Account(String accountNumber, String ownerName) {
        this(accountNumber, ownerName, 0.0);
    }

    public Account(String accountNumber, String ownerName, double balance) {
        setAccountNumber(accountNumber);
        setOwnerName(ownerName);
        setBalance(balance);
    }

    // Getters and setters
    public String getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(String accountNumber) {
        if (accountNumber == null || accountNumber.isEmpty()) {
            throw new IllegalArgumentException("Account number cannot be empty.");
        }
        this.accountNumber = accountNumber;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String ownerName) {
        if (ownerName == null || ownerName.isEmpty()) {
            throw new IllegalArgumentException("Owner name cannot be empty.");
        }
        this.ownerName = ownerName;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        if (balance < 0) {
            throw new IllegalArgumentException("Balance cannot be negative.");
        }
        this.balance = balance;
    }

    // This protected method allows CurrentAccount to use overdraft
    protected void updateBalance(double balance) {
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive.");
        }

        setBalance(getBalance() + amount);
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive.");
        }

        if (amount > getBalance()) {
            throw new IllegalArgumentException("Insufficient balance.");
        }

        setBalance(getBalance() - amount);
    }

    public void display() {
        System.out.println("Account Number: " + getAccountNumber());
        System.out.println("Owner Name: " + getOwnerName());
        System.out.println("Balance: " + getBalance());
    }
}

// Child class 1
class SavingsAccount extends Account {
    private double interestRate;

    public SavingsAccount() {
        this("Unknown", "Unknown", 0.0, 0.0);
    }

    public SavingsAccount(String accountNumber, String ownerName, double balance, double interestRate) {
        super(accountNumber, ownerName, balance);
        setInterestRate(interestRate);
    }

    public double getInterestRate() {
        return interestRate;
    }

    public void setInterestRate(double interestRate) {
        if (interestRate < 0) {
            throw new IllegalArgumentException("Interest rate cannot be negative.");
        }
        this.interestRate = interestRate;
    }

    public double calculateInterest() {
        return getBalance() * interestRate / 100;
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Account Type: Savings Account");
        System.out.println("Interest Rate: " + getInterestRate() + "%");
        System.out.println("Interest Amount: " + calculateInterest());
        System.out.println();
    }
}

// Child class 2
class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount() {
        this("Unknown", "Unknown", 0.0, 0.0);
    }

    public CurrentAccount(String accountNumber, String ownerName, double balance, double overdraftLimit) {
        super(accountNumber, ownerName, balance);
        setOverdraftLimit(overdraftLimit);
    }

    public double getOverdraftLimit() {
        return overdraftLimit;
    }

    public void setOverdraftLimit(double overdraftLimit) {
        if (overdraftLimit < 0) {
            throw new IllegalArgumentException("Overdraft limit cannot be negative.");
        }
        this.overdraftLimit = overdraftLimit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive.");
        }

        if (amount > getBalance() + getOverdraftLimit()) {
            throw new IllegalArgumentException("Withdrawal exceeds overdraft limit.");
        }

        updateBalance(getBalance() - amount);
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Account Type: Current Account");
        System.out.println("Overdraft Limit: " + getOverdraftLimit());
        System.out.println();
    }
}

// Main class
public class BankDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Account> accounts = new ArrayList<>();

        try {
            System.out.println("Enter Savings Account Details");

            System.out.print("Account Number: ");
            String savingsAccNo = input.nextLine();

            System.out.print("Owner Name: ");
            String savingsOwner = input.nextLine();

            System.out.print("Balance: ");
            double savingsBalance = input.nextDouble();

            System.out.print("Interest Rate: ");
            double interestRate = input.nextDouble();

            input.nextLine();

            SavingsAccount savings = new SavingsAccount(
                    savingsAccNo,
                    savingsOwner,
                    savingsBalance,
                    interestRate
            );

            System.out.println();

            System.out.println("Enter Current Account Details");

            System.out.print("Account Number: ");
            String currentAccNo = input.nextLine();

            System.out.print("Owner Name: ");
            String currentOwner = input.nextLine();

            System.out.print("Balance: ");
            double currentBalance = input.nextDouble();

            System.out.print("Overdraft Limit: ");
            double overdraftLimit = input.nextDouble();

            CurrentAccount current = new CurrentAccount(
                    currentAccNo,
                    currentOwner,
                    currentBalance,
                    overdraftLimit
            );

            accounts.add(savings);
            accounts.add(current);

            int choice;

            do {
                System.out.println();
                System.out.println("===== Banking Menu =====");
                System.out.println("1. Deposit");
                System.out.println("2. Withdraw");
                System.out.println("3. Display All Accounts");
                System.out.println("4. Exit");
                System.out.print("Enter your choice: ");
                choice = input.nextInt();

                if (choice == 1 || choice == 2) {
                    System.out.println();
                    System.out.println("Choose Account:");
                    System.out.println("1. Savings Account");
                    System.out.println("2. Current Account");
                    System.out.print("Enter account choice: ");
                    int accountChoice = input.nextInt();

                    Account selectedAccount;

                    if (accountChoice == 1) {
                        selectedAccount = savings;
                    } else if (accountChoice == 2) {
                        selectedAccount = current;
                    } else {
                        throw new IllegalArgumentException("Invalid account choice.");
                    }

                    System.out.print("Enter amount: ");
                    double amount = input.nextDouble();

                    if (choice == 1) {
                        selectedAccount.deposit(amount);
                        System.out.println("Deposit successful.");
                    } else {
                        selectedAccount.withdraw(amount);
                        System.out.println("Withdrawal successful.");
                    }

                    System.out.println();
                    System.out.println("Updated Account Details");
                    System.out.println("-----------------------");
                    selectedAccount.display();

                } else if (choice == 3) {
                    System.out.println();
                    System.out.println("Displaying All Accounts");
                    System.out.println("-----------------------");

                    // Polymorphism
                    for (Account account : accounts) {
                        account.display();
                    }

                } else if (choice == 4) {
                    System.out.println("Thank you for using the banking system.");

                } else {
                    System.out.println("Invalid menu choice.");
                }

                // Basic debugging example
                assert savings.getBalance() >= 0 : "Savings account balance should not be negative.";

            } while (choice != 4);

        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            input.close();
        }
    }
}
