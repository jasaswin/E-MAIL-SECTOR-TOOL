
def extract_domain(email):
    return email.strip().split("@")[-1]


def is_personal_domain(domain):
    personal_domains = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com"
    ]
    return domain.lower() in personal_domains


def load_emails(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]
    


def extract_name(email):

    username = email.split("@")[0]

    name = username.replace(".", " ").replace("_", " ")

    return name.title()

def detect_domain_type(domain):

    personal_domains = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com"
    ]

    if domain in personal_domains:
        return "Free webmail (Google)"

    return "Corporate / Organization Domain"


def extract_person(email):

    username = email.split("@")[0]

    name = username.replace(".", " ").replace("_", " ")

    return name.title()