from pymongo import MongoClient


def connect_to(bbdd = "airegas"):
    host = "localhost"
    puerto = "27017"
    '''
    usuario = "usuario"
    pwd = "pwd"   
    '''
    #cliente = MongoClient("mongodb://{}:{}@{}:{}".format(usuario, palabra_secreta, host, puerto))
    cliente = MongoClient("mongodb://{}:{}".format( host, puerto))

    return cliente[bbdd]

def get_last_update(db):
    """
    funcion que recupera la fecha de la ultima actualizacion de la entidad
    para despues consumir en el api rest de airegas

    db.calendar.where("_id").eq("2020010100001").limit(100)
    db.calendar.find().max(ts)
    db.calendar.find( ,{max(ts):1} )
        """
    pass