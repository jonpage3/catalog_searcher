
import win32com.client
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(30)

messages = inbox.Items
message = messages.GetLast()
body_content = message.body
print(body_content)


