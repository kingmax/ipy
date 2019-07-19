import clr
clr.AddReference("wf_ipy")

from wf_ipy import Form1

#clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

#from System.Drawing import *
from System.Windows.Forms import *

#class MyForm(Form):
#    def __init__(self):
#        # Create child controls and initialize form
#        pass


Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

#form = MyForm()
form = Form1()

# both button1 and btnDoAction are public
form.button1.Click += lambda sender, event:form.txtLog.AppendText("[ipy] new event handler from ipy\n")
# https://stackoverflow.com/questions/2970858/why-doesnt-print-work-in-a-lambda
#form.btnDoAction.Click += lambda sender, e:print(sender, e)

def _print(sender, e):
    print('[ipy] %s %s'%(sender, e))

form.btnDoAction.Click += _print

Application.Run(form)
