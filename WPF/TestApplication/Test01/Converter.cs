using System;
using System.Globalization;
using System.Windows.Data;

namespace Test01
{
    [ValueConversion(typeof(ElementType), typeof(string))]
    public class Converter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is ElementType)
            {
                return value.ToString();
            }
            return string.Empty;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new Exception("Can't convert back");
        }
    }
}