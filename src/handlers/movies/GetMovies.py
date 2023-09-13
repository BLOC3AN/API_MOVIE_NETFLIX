from src.models.Mongodb import MongoHelper


class NormalizeData(MongoHelper): 
    def process():
        listMovies = MongoHelper.getDocumentsInCollection(MongoHelper, 'movies')
        listCast = []
        listGenres = []

        for count in range(len(listMovies)):
            for i in listMovies[count]['casts']:
                dictCast = MongoHelper.getDocumentInCollectionById(MongoHelper,"actor",i)
                listCast.append(dictCast)
            listMovies[count]['casts'] = listCast

        for count in range(len(listMovies)):
            for i in listMovies[count]['genres']:
                dictGenres = MongoHelper.getDocumentInCollectionById(MongoHelper,"genre",i)
                listGenres.append(dictGenres)
            listMovies[count]['genres'] = listGenres

        return listMovies
       
