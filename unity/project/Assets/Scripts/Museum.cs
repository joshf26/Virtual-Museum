using System.Collections.Generic;

public struct Topic {
    public Topic(string name, string imageUrl) {
        this.name = name;
        this.imageUrl = imageUrl;
    }
    
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
