from src.models.Mongodb import MongoHelper

class NormalizeData():
    def process():
        listMovies = MongoHelper.getDocumentsInCollection(MongoHelper, 'movies')
        print(listMovies)
        return listMovies

