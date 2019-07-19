using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace wf_ipy
{
    static class Program
    {
        /// <summary>
        /// 应用程序的主入口点。
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Form wf = new Form1();
            wf.ShowDialog();
            //Application.Run(new Form1());
        }
    }
}
