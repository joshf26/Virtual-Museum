using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
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
    
    private class RawExhibit {
        public string exhibit_name;
        public List<string> imageUrl;
        public List<string> caption;
        public string text;
    }
    
    public IEnumerator GetMuseum(string topic, Action<List<Exhibit>> callback) {
        Debug.Log($"Making request to {_address}/museum/{topic}");
        UnityWebRequest www = UnityWebRequest.Get($"{_address}/museum/{topic}");

        yield return www.SendWebRequest();

        var rawExhibits = new List<RawExhibit>();
        if (www.isNetworkError) {
            Debug.Log($"Error: {www.error}");
        } else {
            rawExhibits = JsonConvert.DeserializeObject<List<RawExhibit>>(www.downloadHandler.text);
        }
        
        var exhibits = new List<Exhibit>();

        foreach (var exhibit in rawExhibits) {
            var displays = new List<Display>();

            var displayCount = exhibit.imageUrl.Count;
            var textSegmentLength = exhibit.text.Length / displayCount;
            Debug.Log($"Exchibit text len {exhibit.text.Length}");
            for (int index = 0; index < displayCount; ++index) {
                displays.Add(new Display(
                    exhibit.imageUrl[index],
                    exhibit.caption[index],
                    exhibit.text.Substring(index * textSegmentLength, textSegmentLength)
                ));
            }
            
            exhibits.Add(new Exhibit(
                exhibit.exhibit_name,
                displays
            ));
        }

        callback(exhibits);
    }
}