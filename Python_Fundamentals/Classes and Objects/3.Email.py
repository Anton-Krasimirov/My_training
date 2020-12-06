# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
# emails = []
# line = input()
# while line != "Stop":
#     tokens = line.split(" ")
#     email = Email(tokens[0], tokens[1], tokens[2])
#     emails.append(email)
#     line = input()
# send_emails = [int(x) for x in input().split(", ")]
# for x in send_emails:
#     emails[x].send()
#
# for email in emails:
#     print(email.get_info())

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


class MailBox:
    def __init__(self):
        self.emails = []

    def add_emails(self, email):
        self.emails.append(email)

    def send_emails(self, email_index):
        for idx in email_index:
            self.emails[idx].send()

    def get_mailbox(self):
        for mail in self.emails:
            print(mail.get_info())

mailbox = MailBox()


command = input()
while command != "Stop":
    sender, receiver, content = command.split(" ")
    email = Email(sender, receiver, content)
    mailbox.add_emails(email)
    command = input()

emails_to_send = [int(x) for x in input().split(", ")]

mailbox.send_emails(emails_to_send)

mailbox.get_mailbox()





