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
    public Exhibit(string name, List<Display> displays) {
        this.name = name;
        this.displays = displays;
    }
    
    public string name;
    public List<Display> displays;
}

public struct Display {
    public Display(string imageUrl, string imageCaption, string text) {
        this.imageUrl = imageUrl;
        this.imageCaption = imageCaption;
        this.text = text;
    }
    
    public string imageUrl;
    public string imageCaption;
    public string text;
}
