using System.Collections.Generic;
using UnityEngine.Networking;

public class Network {
    private readonly string _address;

    public Network(string address) {
        _address = address;
    }
    
    public List<Topic> get_topics() {
        var topics = new List<Topic>();
        
        // TODO: Perform network request and format results.
        topics.Add(new Topic("Test Topic 1", "https://knowpathology.com.au/app/uploads/2018/07/Happy-Test-Screen-01-825x510.png"));
        topics.Add(new Topic("Test Topic 2", "https://iscnow.us/wp-content/uploads/2018/03/Test.png"));
        
        return topics;
    } 
    
    public List<Exhibit> get_museum(string topic) {
        var exhibits = new List<Exhibit>();
        
        // TODO: Perform network request and format results.
        exhibits.Add(new Exhibit("Text Exhibit 1", new List<Display>()));
        exhibits.Add(new Exhibit("Text Exhibit 2", new List<Display>()));
        
        return exhibits;
    }
}