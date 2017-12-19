using System.Windows.Controls;

namespace Test01.Elements
{
    public partial class PositionMoverElement : UserControl, IElement
    {
        public PositionMoverElement()
        {
            DataContext = this;
            InitializeComponent();
            UpEnabled = true;
            DownEnabled = true;
        }

        public ElementType Type => ElementType.AbsolutPosition;
        public int ValueX { get; set; }
        public int ValueY { get; set; }
        public int ValueZ { get; set; }
        public int ValueYaw { get; set; }
        public bool UpEnabled { get; set; }
        public bool DownEnabled { get; set; }
        public int Index { get; set; }

        public string Serialize()
        {
            return "\"PositionMoverElement\": [" + ValueX + ", " + ValueY + ", " + ValueZ + ", " + ValueYaw + "]";
        }

        private void Button_Click_Down(object sender, System.Windows.RoutedEventArgs e)
        {
        }

        private void Button_Click_Up(object sender, System.Windows.RoutedEventArgs e)
        {
        }
    }
}
