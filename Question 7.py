contacts = [
    {
        "name": "Dr. Ravi",
        "phone": "+91 98400 12345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "ravi kumar",
        "phone": "9840012345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Priya",
        "phone": "+91 98765 43210",
        "email": "priya@gmail.com"
    },
    {
        "name": "Kumar",
        "phone": "9876543211",
        "email": "kumar@gmail.com"
    }
]

def normalize_phone(phone):
    number = "".join(
        ch for ch in phone if ch.isdigit()
    )

    if len(number) == 10:
        number = "91" + number

    return number

def normalize_name(name):
    return " ".join(name.lower().split())

merged = {}

for contact in contacts:
    phone = normalize_phone(contact["phone"])

    if phone not in merged:
        merged[phone] = {
            "names": set(),
            "phones": set(),
            "emails": set()
        }

    merged[phone]["names"].add(
        normalize_name(contact["name"])
    )

    merged[phone]["phones"].add(
        contact["phone"]
    )

    if contact["email"]:
        merged[phone]["emails"].add(
            contact["email"].lower()
        )

print("MERGED CONTACTS")

for phone, details in merged.items():
    print("Phone:", phone)
    print("Names:", sorted(details["names"]))
    print("Phone Numbers:", sorted(details["phones"]))
    print("Emails:", sorted(details["emails"]))
    print()
