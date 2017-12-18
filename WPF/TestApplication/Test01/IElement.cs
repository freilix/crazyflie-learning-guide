namespace Test01
{
    public interface IElement
    {
        ElementType Type { get; }
        int Index { get; set; }

        string Serialize();
    }
}