import os
from neo4j import GraphDatabase as GDB,  basic_auth
from pandas import DataFrame as datapd


##### Database session
PWD = os.getenv('NEO4J_PWD', "")
drv = GDB.driver("bolt://localhost:7687", auth=basic_auth("neo4j",PWD)); # driver's database connection
ses = drv.session() #session opening


"""
 Attributes
 [FUNCTION]: clean()

 Parameters
 [RETURNS]: list
 [OUTPUT]: []

"""

def clean():
    query= """ MATCH (n) DETACH DELETE n"""
    print(ses.run(query).data())



"""
 Attributes
 [FUNCTION]: find_TOM()

 Parameters
 [RETURNS]: pandas DataFrame 
 [OUTPUT]: 

"""

def find_TOM():
    query = """MATCH (tom {name: 'Tom Hanks'}) RETURN tom"""
    data = datapd(ses.run(query).data())
    print(data)


if __name__ == "__main__":
    #clean()
    find_TOM()
