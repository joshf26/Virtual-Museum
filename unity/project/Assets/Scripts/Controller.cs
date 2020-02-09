using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;
using Random = UnityEngine.Random;

public class Controller : MonoBehaviour {
    public string address;

    public GameObject menu;
    public GameObject player;
    public GameObject fillerObject;
    public GameObject exhibitObject;
    public GameObject displayObject;
    public GameObject topicObject;
    public Transform topicsList;
    
    Network _network;

    Vector3[] _offsets = {
        Vector3.forward * 30,
        Vector3.right * 30,
        Vector3.back * 30,
        Vector3.left * 30
    };

    private List<Vector3> _displayOffsets;
    private List<Vector3> _displayRotation;
    
    void Awake() {
        _network = new Network(address);

        StartCoroutine(_network.GetTopics(TopicsReady));
    }

    void resetArrays() {
        _displayOffsets = new List<Vector3> {
            new Vector3(13.9f, 0, 9),
            new Vector3(13.9f, 0, -9),
            new Vector3(-13.9f, 0, 9),
            new Vector3(-13.9f, 0, -9),
            new Vector3(9, 0, -13.9f),
            new Vector3(-9, 0, -13.9f),
            new Vector3(9, 0, 13.9f),
            new Vector3(-9, 0, 13.9f)
        };
    
        _displayRotation = new List<Vector3> {
            new Vector3(0, 0, 0),
            new Vector3(0, 0, 0),
            new Vector3(0, 180, 0),
            new Vector3(0, 180, 0),
            new Vector3(0, 90, 0),
            new Vector3(0, 90, 0),
            new Vector3(0, -90, 0),
            new Vector3(0, -90, 0)
        };
    }

    public void TopicsReady(List<Topic> topics) {
        foreach (var topic in topics) {
            Image image = MakeTopic(topic.name);
            StartCoroutine(GetTexture(topic.imageUrl, sprite => {
                image.sprite = sprite;
            }));
        }
    }
    
    public void ChooseTopic(string topic) {
        Debug.Log($"Choosing topic {topic}.");

        GenerateMuseum(topic);
        
        menu.SetActive(false);
        player.SetActive(true);
    }
    
    IEnumerator GetTexture(string url, Action<Sprite> callback) {
        UnityWebRequest www = UnityWebRequestTexture.GetTexture(url);

        yield return www.SendWebRequest();

        if (www.isNetworkError) {
            Debug.Log(www.error);
        } else {
            Texture2D webTexture = ((DownloadHandlerTexture)www.downloadHandler).texture;
            callback(Sprite.Create(
                webTexture, 
                new Rect(0.0f, 0.0f, webTexture.width, webTexture.height), 
                new Vector2(0.5f, 0.5f),
                100.0f
            ));
            
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
        if (_displayOffsets.Count == 0) {
            return;
        }
        
        var randomIndex = Random.Range(0, _displayOffsets.Count);
        var offset = _displayOffsets[randomIndex];
        var rotation = _displayRotation[randomIndex];

        _displayOffsets.RemoveAt(randomIndex);
        _displayRotation.RemoveAt(randomIndex);
        
        var newDisplay = Instantiate(displayObject, position + offset, Quaternion.Euler(rotation));

        foreach (var textComponent in newDisplay.GetComponentsInChildren<TextMesh>()) {
            textComponent.text = textComponent.name == "Body Text" ? display.text : display.imageCaption;

            int index = 70;
            while (index < textComponent.text.Length) {
                textComponent.text = textComponent.text.Insert(index, "\n");
                index += 70;
            }
        }

        StartCoroutine(GetTexture(display.imageUrl, sprite => {
            newDisplay.GetComponentInChildren<SpriteRenderer>().sprite = sprite;
        }));
    }

    void MakeExhibit(Vector3 position, Exhibit exhibit) {
        resetArrays();
        
        Instantiate(exhibitObject, position, Quaternion.identity);

        foreach (var display in exhibit.displays) {
            MakeDisplay(position, display);
        }
    }

    public void GenerateMuseum(string topic) {
        StartCoroutine(_network.GetMuseum(topic, museum => {
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
        }));
    }
}
