using System;
using System.Collections;
using System.Collections.Generic;
using Newtonsoft.Json;
using UnityEngine;
using UnityEngine.Networking;

public class Network {
    private readonly string _address;

    public Network(string address) {
        _address = address;
    }

    public IEnumerator GetTopics(Action<List<Topic>> callback) {
        Debug.Log($"Making request to {_address}/topics");
        UnityWebRequest www = UnityWebRequest.Get($"{_address}/topics");

        yield return www.SendWebRequest();

        var topicsDict = new Dictionary<string, string>();
        if (www.isNetworkError) {
            Debug.Log($"Error: {www.error}");
        } else {
            topicsDict = JsonConvert.DeserializeObject<Dictionary<string, string>>(www.downloadHandler.text);
        }

        var topics = new List<Topic>();

        int i = 0;
        foreach (var topic in topicsDict) {
            topics.Add(new Topic(topic.Key, topic.Value));
            if (i++ == 30) break;
        }
        
        callback(topics);
    }
    
    public List<Exhibit> get_museum(string topic) {
        var exhibits = new List<Exhibit>();
        
        // TODO: Perform network request and format results.
        exhibits.Add(new Exhibit("Text Exhibit 1", new List<Display>()));
        exhibits.Add(new Exhibit("Text Exhibit 2", new List<Display>()));
        exhibits.Add(new Exhibit("Text Exhibit 3", new List<Display>()));
        exhibits.Add(new Exhibit("Text Exhibit 4", new List<Display>()));
        exhibits.Add(new Exhibit("Text Exhibit 5", new List<Display>()));
        exhibits.Add(new Exhibit("Text Exhibit 6", new List<Display>()));
        exhibits.Add(new Exhibit("Text Exhibit 7", new List<Display>()));
        exhibits.Add(new Exhibit("Text Exhibit 8", new List<Display>()));
        
        return exhibits;
    }
}