using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class Controller : MonoBehaviour {
    public string address;

    public GameObject menu;
    public GameObject player;
    public GameObject fillerObject;
    public GameObject exhibitObject;
    public GameObject topicObject;
    public Transform topicsList;
    
    Network _network;
//    private Dictionary<string, Sprite> _imageCache;

    Vector3[] _offsets = new Vector3[4] {
        Vector3.forward * 30,
        Vector3.right * 30,
        Vector3.back * 30,
        Vector3.left * 30
    }; 
    
    void Awake() {
        _network = new Network(address);

        StartCoroutine(_network.GetTopics(TopicsReady));
    }

    public void TopicsReady(List<Topic> topics) {
        foreach (var topic in topics) {
            Image image = MakeTopic(topic.name);
            StartCoroutine(GetTexture(topic.imageUrl, image));
        }
    }
    
    public void ChooseTopic(string topic) {
        Debug.Log($"Choosing topic {topic}.");

        GenerateMuseum(topic);
        
        menu.SetActive(false);
        player.SetActive(true);
    }
    
    IEnumerator GetTexture(string url, Image image) {
        UnityWebRequest www = UnityWebRequestTexture.GetTexture(url);

        yield return www.SendWebRequest();

        if (www.isNetworkError) {
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
        newTopic.GetComponent<Button>().onClick.AddListener(delegate {
            ChooseTopic(topicName);
        });
        return newTopic.GetComponentInChildren<Image>();
    }

    void MakeDisplay(Vector3 position, Display display) {
        
    }

    void MakeExhibit(Vector3 position, Exhibit exhibit) {
        Instantiate(exhibitObject, position, Quaternion.identity);
    }

    public void GenerateMuseum(string topic) {
        List<Exhibit> museum = _network.get_museum(topic);

        var exhibitPositions = new HashSet<Vector3>();

        foreach (var exhibit in museum) {
            Vector3 position = Vector3.zero;

            while (exhibitPositions.Contains(position)) {
                position = exhibitPositions.ElementAt(Random.Range(0, exhibitPositions.Count - 1));
                
                var random = Random.Range(0, 3);
                position += _offsets[random];
            }

            exhibitPositions.Add(position);
            MakeExhibit(position, exhibit);
        }

        // Close all the gaps.
        foreach (var exhibitPosition in exhibitPositions) {
            foreach (var offset in _offsets) {
                var gapPosition = exhibitPosition + offset;
                if (!exhibitPositions.Contains(gapPosition)) {
                    var fillerPosition = (exhibitPosition + gapPosition) / 2;

                    Vector3 rotation;
                    var heading = fillerPosition - exhibitPosition;
                    if (heading.x < 0)
                        rotation = new Vector3(0, 0, -90);
                    else if (heading.x > 0)
                        rotation = new Vector3(0, 0, 90);
                    else if (heading.z < 0)
                        rotation = new Vector3(0, 90, 90);
                    else
                        rotation = new Vector3(0, 90, -90);
                    
                    fillerPosition.y = 3;
                    Instantiate(fillerObject, fillerPosition, Quaternion.Euler(rotation));
                }
            }
        }
    }
}
