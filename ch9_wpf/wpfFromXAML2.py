import clr

clr.AddReference("PresentationFramework", "PresentationCore")

from System.IO import File
from System.Windows.Markup import XamlReader
from System.Windows import (Application, Window)
from System.Windows.Controls import Label


class HelloWorld(object):
    def __init__(self):
        #stream = File.OpenRead("wpfFromXAML.xaml") #r'D:\git\ipy\ch9_wpf\wpfFromXAML.xaml'
        stream = File.OpenRead(r'D:\git\ipy\ch9_wpf\wpfFromXAML2.xaml') #r'D:\git\ipy\ch9_wpf\wpfFromXAML.xaml'
        # create WPF object from xaml
        self.Root = XamlReader.Load(stream)
        self.button = self.Root.FindName('button')
        self.stackPanel = self.Root.FindName('stackPanel')
        self.button.Click += self.on_click

        self.button.Click += self.button_Click


    def on_click(self, sender, event):
        msg = Label(FontSize = 36, Content='Welcome to IronPython!')
        self.stackPanel.Children.Add(msg)

    def button_Click(self, sender, event):
        print('method from xaml event')
        print(self, sender, event)


def main():
    hello = HelloWorld()
    app = Application()
    app.Run(hello.Root)

if __name__ == '__main__':
    main()