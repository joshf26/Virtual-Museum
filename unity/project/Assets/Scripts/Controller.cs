using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class Controller : MonoBehaviour {
    public string address;

    public GameObject topicObject;
    public Transform topicsList;
    
    List<Topic> _topics;
    Network _network;
    
    void Awake() {
        _network = new Network(address);

        _topics = _network.get_topics();

        foreach (var topic in _topics) {
            Image image = MakeTopic(topic.name);
            StartCoroutine(GetTexture(topic.imageUrl, image));
        }
    }
    
    IEnumerator GetTexture(string url, Image image) {
        UnityWebRequest www = UnityWebRequestTexture.GetTexture(url);

        yield return www.SendWebRequest();

        if(www.isNetworkError) {
            Debug.Log(www.error);
        } else {
            Texture2D webTexture = ((DownloadHandlerTexture)www.downloadHandler).texture;
            image.sprite = Sprite.Create(
                webTexture, 
                new Rect(0.0f, 0.0f, webTexture.width, webTexture.height), 
                new Vector2(0.5f, 0.5f),
                100.0f
            );
        }
    }

    Image MakeTopic(string topicName) {
        var newTopic = Instantiate(topicObject, topicsList);
        newTopic.GetComponentInChildren<Text>().text = topicName;
        return newTopic.GetComponentInChildren<Image>();
    }

    public void GenerateMuseum(string topic) {
        List<Exhibit> museum = _network.get_museum(topic);

        foreach (var exhibit in museum) {
//            MakeTopic(exhibit.name, exhibit);
        }
        
        // TODO: Generate museum from exhibit list.
    }
}
