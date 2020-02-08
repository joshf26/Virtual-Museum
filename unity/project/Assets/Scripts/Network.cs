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
    
    public IEnumerator GetMuseum(string topic, Action<List<Exhibit>> callback) {
        Debug.Log($"Making request to {_address}/museum/{topic}");
        UnityWebRequest www = UnityWebRequest.Get($"{_address}/museum/{topic}");

        yield return www.SendWebRequest();

        var rawExhibits = new List<Dictionary<string, object>>();
        if (www.isNetworkError) {
            Debug.Log($"Error: {www.error}");
        } else {
            Debug.Log(www.downloadHandler.text);
            rawExhibits = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(www.downloadHandler.text);
        }
        
        var exhibits = new List<Exhibit>();

        foreach (var exhibit in rawExhibits) {
            var displays = new List<Display>();

            for (int index = 0; index < ((List<string>)exhibit["imageUrl"]).Count; ++index) {
                displays.Add(new Display(
                    ((List<string>)exhibit["imageUrl"])[index],
                    ((List<string>)exhibit["caption"])[index],
                    (string)exhibit["text"]
                ));
            }
            
            exhibits.Add(new Exhibit(
                (string)exhibit["exhibit_name"],
                displays
            ));
        }
        
        // TODO: Perform network request and format results.
//        var displays = new List<Display>();
//        displays.Add(new Display(
//            "https://www.biography.com/.image/t_share/MTE4MDAzNDEwNzg5ODI4MTEw/barack-obama-12782369-1-402.jpg",
//            "Obama",
//            "He's a cool fella"
//        ));
//        displays.Add(new Display(
//            "https://smhttp-ssl-42830.nexcesscdn.net/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/d/g/dg65639_3.jpg",
//            "Minecraft Steve",
//            "He do be chillin doe"
//        ));
//        exhibits.Add(new Exhibit("Text Exhibit 1", displays));
        
        callback(exhibits);
    }
}