using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using Microsoft.Win32;
using Test01.Elements;

namespace Test01
{
    public partial class MainWindow : Window
    {
        public string PythonPath { get; set; }

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click_IncX(object sender, RoutedEventArgs e)
        {
            var element = new IncrementXElement();
            Panel01.Children.Add(element);
            var index = Panel01.Children.IndexOf(element);
            element.Index = index;
        }

        private void Button_Click_IncY(object sender, RoutedEventArgs e)
        {
            var element = new IncrementYElement();
            Panel01.Children.Add(element);
            var index = Panel01.Children.IndexOf(element);
            element.Index = index;
        }

        private void Button_Click_IncZ(object sender, RoutedEventArgs e)
        {
            var element = new IncrementZElement();
            Panel01.Children.Add(element);
            var index = Panel01.Children.IndexOf(element);
            element.Index = index;
        }

        private void Button_Click_IncYaw(object sender, RoutedEventArgs e)
        {
            var element = new IncrementYawElement();
            Panel01.Children.Add(element);
            var index = Panel01.Children.IndexOf(element);
            element.Index = index;
        }

        private void Button_Click_AbsPos(object sender, RoutedEventArgs e)
        {
            var element = new PositionMoverElement();
            Panel01.Children.Add(element);
            var index = Panel01.Children.IndexOf(element);
            element.Index = index;
            
        }

        private void Stackpanel_Click(object sender, RoutedEventArgs e)
        {
            if (!(e.Source is IElement source))
                return;

            if (!(e.OriginalSource is Button button))
                return;
            
            if (button.Content != null && (string) button.Content == "Up")
            {
                Panel01.Up(source);
            }

            if (button.Content != null && (string)button.Content == "Down")
            {
                Panel01.Down(source);
            }
        }

        private void Play_PythonPath(object sender, RoutedEventArgs e)
        {
            var dialog = new OpenFileDialog();
            dialog.ShowDialog();
            PythonPath = dialog.FileName;
        }

        private TcpClient _client;
        private NetworkStream _stream;
        
        private void Send(object sender, RoutedEventArgs e)
        {
            var children = Panel01.Children.OfType<IElement>();
            var parser = new JsonParser();
            var jsonString = parser.Serialize(children);

            var bytes = Encoding.ASCII.GetBytes(jsonString);

            _stream.Write(bytes, 0, bytes.Length);
        }

        private void Connect(object sender, RoutedEventArgs e)
        {
            _client = new TcpClient();
            _client.Connect("localhost", 9050);
            _stream = _client.GetStream();
        }

        private void Play_Click(object sender, RoutedEventArgs e)
        {
            var children = Panel01.Children.OfType<IElement>();
            var parser = new JsonParser();
            var jsonString = parser.Serialize(children);

            var pr = new PythonRunner(PythonPath);
            // var result = pr.RunPython(@"C:\Users\Felix\Desktop\PythonTest.py", "Hund Katze Maus");
            var result = pr.RunPython(@"C:\Users\Felix\Documents\Git\crazyflie-learning\Backend\PythonRunner.py", jsonString);
            Log.Text += result;
        }
    }

    public class JsonParser
    {
        /*
        { 
        "IncrementXElement":0.5,
        "IncrementYElement": -1,
        "PositionMoverElement":[1,3.5,1,0],
        "IncrementZElement": -1,
        "IncrementYawElement": -30
        }
        */
        public string Serialize(IEnumerable<IElement> elements)
        {
            var result = "{ " + string.Join(",", elements.Select(x => x.Serialize())) + " }";
            return result;
        }
    }

    public class PythonRunner
    {
        private readonly string _pythonPath;

        public PythonRunner(string pythonPath)
        {
            _pythonPath = pythonPath;
        }

        public string RunPython(string cmd, string args)
        {
            string result;
            var start = new ProcessStartInfo
            {
                // FileName = _pythonPath,
                FileName = @"C:\Python34\python.exe",
                Arguments = $"{cmd} {args}",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true
            };

            using (var process = Process.Start(start))
                using (var reader = process.StandardError)
                    result = reader.ReadToEnd();
            return result;
        }
    }
}