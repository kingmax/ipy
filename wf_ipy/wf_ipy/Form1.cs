using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace wf_ipy
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            this.linkLabel1.LinkVisited = true;
            System.Diagnostics.Process.Start(this.linkLabel1.Text);
        }

        void logButtonClick(object sender)
        {
            this.txtLog.AppendText((sender as Button).Text + "  clicked\n");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            logButtonClick(sender);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            logButtonClick(sender);
            if (this.folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                this.txtLog.AppendText(this.folderBrowserDialog1.SelectedPath + "\n");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            logButtonClick(sender);
            if (this.openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                this.txtLog.AppendText(this.openFileDialog1.FileName + "\n");
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            logButtonClick(sender);
            if (this.saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                this.txtLog.AppendText(this.saveFileDialog1.FileName + "\n");
            }
        }

        private void btnDoAction_Click(object sender, EventArgs e)
        {
            logButtonClick(sender);
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.textBox1.Text = Convert.ToString(this.comboBox1.SelectedIndex) + ": " + this.comboBox1.SelectedItem;
        }
    }
}
