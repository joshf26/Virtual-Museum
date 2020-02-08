using System.Collections.Generic;
using UnityEngine;

public class Controller : MonoBehaviour {
    public string address;
    
    List<Topic> _topics;
    Network _network;
    
    void Awake() {
        _network = new Network(address);

        _topics = _network.get_topics();
    }

    public void GenerateMuseum(string topic) {
        List<Exhibit> museum = _network.get_museum(topic);
        
        // TODO: Generate museum from exhibit list.
    }
}
