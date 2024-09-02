#Write a program to slice the username and domain from email

email_id="akhilgkrishnan@gmail.com"

at_index_pos=email_id.index("@")

user_name=email_id[:at_index_pos]

domain=email_id[at_index_pos:]

print(user_name)

print(domain)