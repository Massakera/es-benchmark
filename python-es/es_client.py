from elasticsearch import Elasticsearch

es = Elasticsearch()

def fetch_complex_query():
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "range": {
                            "number": {
                                "gte": 100,
                                "lte": 200
                            }
                        }
                    },
                    {
                        "match": {
                            "job": "engineer"
                        }
                    }
                ]
            }
        }
    }
    es.count(index="sample_data")
    print(es.search(index="sample_data", body=query))


    return es.search(index="sample_data", body=query)

result = fetch_complex_query()
print(result)

