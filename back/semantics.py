from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint
import json
import urllib.parse
import urllib.request
import config
import logging

def get_description_of_the_movie(movie_title):
    api_key = config.api_key
    query = movie_title
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 1,
        'indent': True,
        'key': api_key,
        'types': ['Movie'],
    }
    url = service_url + '?' + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read())
    try:
        return response['itemListElement'][0]['result']['detailedDescription']['articleBody']
    except:
        return None

def return_correct_thumbnail(url):
    return url.replace("Special:FilePath", "en:Special:Filepath")

def return_movies():
    sparql = SPARQLWrapper('https://dbpedia.org/sparql')
    sparql.setQuery('''
    SELECT DISTINCT ?film, ?abstract, ?titleMovie, (GROUP_CONCAT(DISTINCT ?actors; SEPARATOR=" / ") AS ?actors), ?country, ?image
    WHERE {
            ?film rdf:type dbo:Film .
            ?film rdfs:comment ?abstract .
            ?film dbp:name ?titleMovie .
            ?film dbp:starring ?actors .
            ?film dbp:country ?country .
            ?film dbo:thumbnail ?image .
            FILTER ( LANG ( ?titleMovie ) = 'en' )  .
            FILTER ( LANG ( ?abstract ) = 'en' ) 
    } ORDER BY RAND()
    LIMIT 1000
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()

    try:
        return qres['results']["bindings"]
    except BaseException:
        logging.exception("An exception was thrown!")
        return None

# print(return_movies())

# print(get_description_of_the_movie("The Notebook"))

