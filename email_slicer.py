def get_email(user_input):
    name = ""
    character =""
    mail_type =""
    name = user_input.split("@")[0]
    character = "@" if '@' in user_input else ""
    mail_type = user_input.split('@')[-1]
    return (name,character,mail_type)
def main():
    user_input = input("Enter an email: ")
    name,character,mail_type = get_email(user_input)
    print(name)
    print(character)
    print(mail_type)

if __name__ =="__main__":
    main()