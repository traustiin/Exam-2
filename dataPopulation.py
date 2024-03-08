import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Define a function to add data to a table
#don't run again
def add_data_BEthics(question,answer):
        cursor.execute(f'''INSERT INTO Business_Ethics (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")
        add_data_BEthics("What is the definition of business ethics?","Moral principles that guide you in the business world")

def add_data_bmgt(question,answer):
        cursor.execute(f'''INSERT INTO Business_Data_MGMT (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")
        add_data_bmgt("Question typed here","Answer right here")

def add_data_BCommunication(question,answer):
        cursor.execute(f'''INSERT INTO Business_Communication (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")
        add_data_BCommunication("Question typed here","Answer right here")

def add_data_PrincOfMacro(question,answer):
        cursor.execute(f'''INSERT INTO Principles_of_Macro (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")
        add_data_PrincOfMacro("Question typed here","Answer right here")

def add_data_AppDevelop(question,answer):
        cursor.execute(f'''INSERT INTO Business_App_Development (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")
        add_data_AppDevelop("Question typed here","Answer right here")













# Generate questions and answers for each category
business_ethics_data = [
    ("What is the definition of business ethics?", "Business ethics refers to the moral principles that guide the conduct of individuals and organizations in the business world."),
    ("Give an example of an ethical dilemma in business.", "An example of an ethical dilemma in business is deciding whether to prioritize profits over environmental sustainability."),
    ("What is corporate social responsibility (CSR)?", "Corporate social responsibility (CSR) is the practice of companies operating in a socially responsible manner by considering the interests of society in their operations and interactions with stakeholders."),
    ("Explain the concept of whistleblowing.", "Whistleblowing is the act of reporting unethical or illegal behavior within an organization to authorities or the public."),
    ("What are the key components of a code of ethics?", "The key components of a code of ethics include integrity, honesty, accountability, fairness, and respect for others."),
    ("What is the difference between ethics and compliance?", "Ethics refers to the moral principles that guide behavior, while compliance involves adhering to laws, regulations, and policies."),
    ("Why is ethical leadership important in business?", "Ethical leadership is important in business because it sets a positive example for employees, builds trust with stakeholders, and contributes to long-term organizational success."),
    ("Discuss the relationship between ethics and corporate culture.", "Ethics and corporate culture are closely linked, as corporate culture influences the ethical behavior of employees and leaders, and ethical behavior contributes to the development of a positive corporate culture."),
    ("What role does ethics play in decision-making?", "Ethics plays a crucial role in decision-making by guiding individuals and organizations to make choices that are morally acceptable and aligned with their values and principles."),
    ("How can businesses promote ethical behavior among eamployees?", "Businesses can promote ethical behavior among employees by establishing clear ethical standards, providing ethics training and education, rewarding ethical behavior, and fostering a culture of integrity and transparency.")
]

business_data_mgmt_data = [
    ("What is data management?", "Data management refers to the process of collecting, storing, organizing, and analyzing data to support business operations and decision-making."),
    ("Explain the importance of data quality.", "Data quality is important because accurate and reliable data is essential for making informed decisions, ensuring regulatory compliance, and improving business performance."),
    ("What are the key components of a data management strategy?", "The key components of a data management strategy include data governance, data architecture, data integration, data security, and data quality management."),
    ("What is a data warehouse?", "A data warehouse is a centralized repository that stores structured and unstructured data from multiple sources for reporting and analysis purposes."),
    ("What is the difference between data warehousing and data mining?", "Data warehousing involves storing and organizing data for analysis, while data mining involves discovering patterns and insights from large datasets."),
    ("What is master data management (MDM)?", "Master data management (MDM) is a process that ensures the consistency and accuracy of critical data across an organization's systems and applications."),
    ("Discuss the role of data governance in data management.", "Data governance is the framework and processes for managing data assets and ensuring data quality, security, and compliance."),
    ("Explain the concept of data integration.", "Data integration involves combining data from different sources to provide a unified view of information for analysis and decision-making."),
    ("What are some common challenges in data management?", "Common challenges in data management include data quality issues, data silos, lack of data governance, security concerns, and compliance requirements."),
    ("How can businesses benefit from effective data management?", "Businesses can benefit from effective data management by improving decision-making, enhancing operational efficiency, reducing costs, and gaining competitive advantage.")
]

business_communication_data = [
    ("What is business communication?", "Business communication refers to the exchange of information within and outside an organization to achieve business objectives."),
    ("What are the key elements of effective communication?", "The key elements of effective communication include clarity, conciseness, credibility, completeness, and consideration for the audience."),
    ("Discuss the importance of active listening in business communication.", "Active listening is important in business communication because it helps individuals understand others' perspectives, build rapport, and resolve conflicts."),
    ("Whata are the different channels of business communication?", "The different channels of business communication include face-to-face meetings, email, phone calls, video conferencing, and written documents."),
    ("Explain the concept of nonverbal communication.", "Nonverbal communication involves conveying messages without words through gestures, facial expressions, body language, and tone of voice."),
    ("How can businesses overcome communication barriers?", "Businesses can overcome communication barriers by promoting open communication, providing training in communication skills, using multiple communication channels, and seeking feedback from employees."),
    ("Discuss the role of communication technology in business.", "Communication technology such as email, instant messaging, and collaboration tools facilitates faster and more efficient communication, enabling organizations to collaborate across geographic locations and time zones."),
    ("What are the benefits of effective business communication?", "The benefits of effective business communication include improved productivity, enhanced teamwork, better decision-making, and increased customer satisfaction."),
    ("What is the difference between formal and informal communication?", "Formal communication follows established protocols and channels within an organization, while informal communication occurs spontaneously and is more casual in nature."),
    ("How can businesses ensure clarity in written communication?", "Businesses can ensure clarity in written communication by using simple and concise language, organizing information logically, and proofreading documents for errors.")
]

principles_of_macro_data = [
    ("What is macroeconomics?", "Macroeconomics is the branch of economics that studies the behavior of the economy as a whole, including topics such as inflation, unemployment, economic growth, and monetary and fiscal policy."),
    ("Explain the concept of gross domestic product (GDP).", "Gross domestic product (GDP) measures the total value of all goods and services produced within a country's borders in a specific period."),
    ("Discuss the relationship between inflation and unemployment.", "The Phillips curve illustrates the inverse relationship between inflation and unemployment, suggesting that when inflation is low, unemployment tends to be high, and vice versa."),
    ("What is monetary policy?", "Monetary policy refers to the actions taken by a central bank to control the money supply and interest rates to achieve economic goals such as price stability and full employment."),
    ("Explain the concept of fiscal policy.", "Fiscal policy involves the use of government spending and taxation to influence the economy, with the aim of achieving economic goals such as stabilizing economic growth and reducing unemployment."),
    ("Discuss the role of the Federal Reserve in the U.S. economy.", "The Federal Reserve, often referred to as the Fed, is the central bank of the United States, responsible for conducting monetary policy, supervising and regulating banks, and maintaining financial stability."),
    ("What is the difference between classical and Keynesian economics?", "Classical economics emphasizes the importance of free markets and limited government intervention, while Keynes.")
     
     
]
