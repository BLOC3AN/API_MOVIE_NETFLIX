from src.models.Mongodb import MongoHelper

class NormalizeData(MongoHelper):
    def process():
        listMovies = MongoHelper.getDocumentsInCollection(MongoHelper, 'genre')
        print(listMovies)
        return listMovies

