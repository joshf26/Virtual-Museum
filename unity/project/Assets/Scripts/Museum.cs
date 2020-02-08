using System.Collections.Generic;

public struct Topic {
    public string name;
    public string imageUrl;
}

public struct Exhibit {
    public string name;
    public List<Display> displays;
}

public struct Display {
    public string imageUrl;
    public string imageCaption;
    public string text;
}
