import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import *
from System.Windows.Forms import *


class MainForm(Form):
    def __init__(self):
        # Create child controls and initialize form
        self.Text = 'MultiDoc Editor'
        self.MinimumSize = Size(150, 150)

        self.tabControl = TabControl()
        self.tabControl.Dock = DockStyle.Fill
        self.tabControl.Alignment = TabAlignment.Bottom
        self.Controls.Add(self.tabControl)

        self.addTabPage('New Page', '')

    def addTabPage(self, label, text):
        tabPage = TabPage()
        tabPage.Text = label

        textBox = TextBox()
        textBox.Multiline = True
        textBox.Dock = DockStyle.Fill
        textBox.ScrollBars = ScrollBars.Vertical
        textBox.AcceptsReturn = True
        textBox.AcceptsTab = True
        textBox.WordWrap = True
        textBox.Text = text

        tabPage.Controls.Add(textBox)
        
        self.tabControl.TabPages.Add(tabPage)


Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MainForm()
Application.Run(form)
