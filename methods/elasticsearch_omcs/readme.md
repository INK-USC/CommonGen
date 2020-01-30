## Installation

* ```pip install elasticsearch```
* [Download](https://www.elastic.co/downloads/elasticsearch) and unzip the Elasticsearch official distribution.
* Run ```bin/elasticsearch``` 
* Run ```curl -X GET http://localhost:9200/```

## Data downloading
The OMCS corpus can be downloaded at [here](https://s3.amazonaws.com/conceptnet/downloads/2018/omcs-sentences-free.txt).

## Building index
We need to first split dataset into many smaller chunk files.
```
split -l 50000 ./omcs-sentences-free.txt -d -a 2 omcs_
python index_es.py
```

## Quering related sentences
```
python search_cs.py
```
