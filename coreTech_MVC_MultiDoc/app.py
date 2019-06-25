#coding:utf-8

from controller import *

class MainForm(Form):
    def __init__(self):
        super(MainForm, self).__init__()
        self.Text = 'MultiDoc Editor'
        self.MinimumSize = Size(150, 200)

        self.tabControl = TabControl()
        self.tabControl.Dock = DockStyle.Fill
        self.tabControl.Alignment = TabAlignment.Bottom
        self.Controls.Add(self.tabControl)

        self.document = Document()
        self.tabController = TabController(self.tabControl, self.document)


Application.EnableVisualStyles()
Application.Run(MainForm())
