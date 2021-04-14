import win32com.client
import os
import time
import pandas as pd
outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
inbox = outlook.GetDefaultFolder(6)
ecn = inbox.Folders(6)
for messages in ecn.Items:
	print(messages)