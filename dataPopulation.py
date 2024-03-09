import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Define a function to add data to a table
def add_data_BEthics(question,answer):
        cursor.execute(f'''INSERT INTO Business_Ethics (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")

        add_data_BEthics("What is the definition of business ethics?","B) Moral principles that guide you in the business world","B")
        add_data_BEthics("An open, peaceful violation of a law to protect its alleged injustice is? ","A) Morality Disobedience B) Civil Disobedinece C) Ethic Violation","B")
        add_data_BEthics("Personal human liberties that are guaranteed by the US Constitution is?","A) Human Rights B) Civil Rights C) Common rights","B")
        add_data_BEthics("Determining what is right or wrong action in a reasoned and impartial manner is?","A) Morality B) Ethics C) Integrity","B")
        add_data_BEthics("Making decisions that treat everyone the same.","A) Partial B) Impartiality C) Ethics","B")
        add_data_BEthics("The capacity to do what is right even when tempted to do otherwise","A) Temptation B) Integrity C) Morality","B")
        add_data_BEthics("Business ethics are the ethical principles used in making good business decisions.","A) True B) False","B")
        add_data_BEthics("An organization's financial statement containing untrue data which is used to mislead is known as?","A) A bankruptcy discharge B) A false financial statement C) A bank statement fee","B")
        add_data_BEthics("An entrusted person who converts other's assets or property for his or her own use is an?","A) Identity theif B) Embezzler C) Fee schemer","B")
        add_data_BEthics("All parties which interact with a business are known as?","A) Shareholders B) Stakeholders C) Customers","B")

def add_data_bmgt(question,answer):
        cursor.execute(f'''INSERT INTO Business_Data_MGMT (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")

        add_data_bmgt("What is the full form of DBMS?","A) Data of Binary Management System B) Database Management System C) Database Management Service","B")
        add_data_bmgt("What is a database?","A) Organized collection of data that cannot be updated B) Organized collection of data or information that can be accessed, updated, and managed C) Collection of data or information without organizing","B")
        add_data_bmgt("What is DBMS?","A) A collection of queries B) DBMS stores, modifies, and retrieves data C) DBMS is a programming language","B")
        add_data_bmgt("Who created the first DBMS?","A) Edgar Frank Codd B) Charles Bachman C) Charles Babbage","B")
        add_data_bmgt("Which type of data can be stored in the database?","A) Image oriented data B) All of the above C) Text, files containing data","B")
        add_data_bmgt("In which of the following formats data is stored in the DBMS?","A) Image B) Table C) Graph","B")
        add_data_bmgt("Which of the following is not a type of database?","Hierarchical B) Decentralized C) Network","B")
        add_data_bmgt("Which of the following is not an example of DBMS?","A) MySQL B) Google C) Microsoft Access","B")
        add_data_bmgt("Which of the following is not a feature of DBMS?","A) High level of security B) Single-user access only C) Support ACID Property","B")
        add_data_bmgt("Which of the following is a feature of the database?","A) Lack of authentication B) User interface provided C) Store data in multiple locations","B")

def add_data_BCommunication(question,answer):
        cursor.execute(f'''INSERT INTO Business_Communication (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")

        add_data_BCommunication("The term communis derived from ___ word","A) Greek B) Latin C) Chinese","B")
        add_data_BCommunication("Communication means ___ information, feeling and thoughts, with others","A) To recieve B) Exchange of C) Conveying","B")
        add_data_BCommunication("Grapevine communication is associated with ___ communication","A) Formal B) Informal C) Horizontal","B")
        add_data_BCommunication("Lateral communication is between","A) Superior and subordinate B) Same cadre of personal C) Among all","B")
        add_data_BCommunication("Audio visual communicationis","A) Written B) Both auditory & visual C) Visual only","B")
        add_data_BCommunication("Communication problems otherwise known as","A) Enquire B) Barriers C) Encoding","B")
        add_data_BCommunication("Posters fall under ___ communication","A) Oral B) Visual C) Written","B")
        add_data_BCommunication("Informal communication is otherwise known as ___ communication","A) Lateral B) Grapevine C) Visual","B")
        add_data_BCommunication("Horizontal communication flows through","A) Telephonic talk B) All of the above C) Periodical meeting","B")
        add_data_BCommunication("Gestural communication is a ___","A) Direct conversation B) Non-verbal message C) Oral communication","B")

def add_data_PrincOfMacro(question,answer):
        cursor.execute(f'''INSERT INTO Principles_of_Macro (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")
        
        add_data_PrincOfMacro("A given increase in government spending is more effective at increasing output in a country that __","A) A decrease in interest rate B) A decrease in the level of output C) No change","B")
        add_data_PrincOfMacro("In the short run, under a flexable exchange rate, an expansionary monetary policy ___","A) Has an ambiguous effect on investment B) Has an ambiguous effect on net exports C) Has an ambiguous effect on the interest rate","B")
        add_data_PrincOfMacro("In the short run, under a flexible exchange rate, an expansionary fiscal policy ___","A) Has a negative effect on investment B) Has a negative effect on net exports C) Has a positive effect on investment","B")
        add_data_PrincOfMacro("A country with a fixed exchange rate ___","A) Must open its capital market B) Gives up control of its monetary policy if it maintains open capital markets C) Must give up control of its monetary policy","B")
        add_data_PrincOfMacro("Higher government spending will not crowd out investment in___","A) A closed economy B) An open economy with fixed exchange rates C) An open economy with fixed exchange rates","B")
        add_data_PrincOfMacro("A country will be expected to have a larger trade volume to GDP if___","A) Europe's economies have inflexible labor markets B) Europe's economies are already highly dependent on trade with each other C) Europe's economies are subject to uncorrelated shocks","B")
        add_data_PrincOfMacro("To decrease the trade deficit and to increase short-run output, which of the following could work?","A) Contractionary monetary policy B) A depreciation of the dollar C) Adoption of a fixed exchange rate","B")
        add_data_PrincOfMacro("A nation's standard of living is","A) Real GDP B) Real GDP per person C) Nominal GDP","B")
        add_data_PrincOfMacro("Profits that are reinvested in a frim rather than paid to the firm's owners are called?","A) Dividends B) Retained earnings C) Stock options","B")
        add_data_PrincOfMacro("If nominal GDP exceeds real GDP for a specific year, then the GDP deflator must be___","A) Equal to 100 B) Greater than 100 C) Less than 100","B")

def add_data_AppDevelop(question,answer):
        cursor.execute(f'''INSERT INTO Business_App_Development (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")

        add_data_AppDevelop("Name of the screen that recognizes touch input is?","A) Digital screen B) Touch screen C) Point screen","B")
        add_data_AppDevelop("Which of these stores more data than a DVD?","A) CD Rom B) Blue Ray disk C) Floppy disk","B")
        add_data_AppDevelop("What do functions do?","A) Functions manipulate data within a program B) Functions define a set of instructions to perform a specific task C) Functions create graphical interfaces for user interaction","B")
        add_data_AppDevelop("What are booleans?","A) Booleans are data types used to represent numeric values B) Booleans are data types that represent true or false values C) Booleans are used to perform arithmetic operations in programming","B")
        add_data_AppDevelop("What is the primary purpose of a while loop in progamming?","A) To execute a block of code a specific number of times B) To repeat a block of code until a certain condition is no longer true C) To perform mathmatical calculations efficiently","B")
        add_data_AppDevelop("What does sequencing refer to in programming?","A) Organizing data into structured formats like arrays and lists B) Arranging code statements in a specific order to execute tasks step by step C) Determining the flow of control within conditional statements","B")
        add_data_AppDevelop("What is the primary purpose of dictionaries in programming?","A) Storing and organizing data in a sequential manner B) Mapping keys to corresponding values for efficient retrieval C) Performing mathmatical operations on numeric datasets","B")
        add_data_AppDevelop("What is the main function of a for loop in programming?","A) To execute a block of code repeatedly until a certain condition is met B) To iterate over a sequence and perform an action on each item C) To define a set of instructions to perform a task","B")
        add_data_AppDevelop("What is the primary goal of prompt engineering?","A) To design user-friendly interfaces for software applications B) To create clear instructions for achieving desired outcomes C) To optomize the efficiency of algorithms and data structures","B")
        add_data_AppDevelop("What is the primary purpose of defining functions?","A) To execute a block of code repreatedly until a certain condition is met B) To organize code into reuseable modules for easier readability C) To perfom mathmatical calculations on numeric datasets","B")
