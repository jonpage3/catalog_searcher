import win32com.client, re

outlook = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
folder = outlook.Folders.Item("Library Circulation")
inbox = folder.Folders.Item("Inbox")
msgs = inbox.Items
msg = msgs.GetFirst()
body = msg.body

oclcRegex = re.compile(r'OCLC #: (.*)')
oclc_searched = oclcRegex.search(body)
oclc_list = oclc_searched.group(1).split('\r')
oclc = oclc_list[0]
print(oclc)


