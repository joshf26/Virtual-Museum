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
        
        return topics;
    } 
    
    public List<Exhibit> get_museum(string topic) {
        var exhibits = new List<Exhibit>();
        
        // TODO: Perform network request and format results.
        
        return exhibits;
    }
}