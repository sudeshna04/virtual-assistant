def generate_application(name, recipient, company, position, source, qualifications):
    letter = f"""
{name}
[Your Address]
[City, State, Zip Code]
[Email Address]
[Phone Number]
[Date]

{recipient}
{company}
[Company Address]
[City, State, Zip Code]

Dear {recipient},

I am writing to express my interest in the {position} position at {company} as advertised on {source}. With my background in {qualifications}, I am confident that I would be a valuable addition to your team.

I have attached my resume for your review. I would welcome the opportunity to discuss how my skills align with your needs.

Thank you for considering my application. I look forward to the possibility of contributing to {company}.

Sincerely,
{name}
"""
    return letter.strip()

# Example usage:
if __name__ == "__main__":
    your_name = input("Your full name: ")
    recipient_name = input("Recipient's name (e.g., Hiring Manager): ")
    company_name = input("Company name: ")
    position = input("Position applying for: ")
    source = input("Where did you find the job listing?: ")
    qualifications = input("Briefly, your qualifications or experience: ")

    application_text = generate_application(your_name, recipient_name, company_name, position, source, qualifications)

    # Save to file
    with open("application_letter.txt", "w", encoding="utf-8") as f:
        f.write(application_text)

    print("\nApplication letter generated and saved as 'application_letter.txt'.")
