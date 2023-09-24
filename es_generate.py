from elasticsearch import Elasticsearch, helpers
import random
import faker

fake = faker.Faker()

es = Elasticsearch()

def generate_data():
    for _ in range(1000000):  # Adjust the number based on your needs
        yield {
            "_index": "sample_data",
            "_source": {
                "name": fake.name(),
                "address": fake.address(),
                "date_of_birth": fake.date_of_birth().isoformat(),
                "email": fake.email(),
                "job": fake.job(),
                "number": random.randint(1, 1000)
            }
        }

helpers.bulk(es, generate_data())
