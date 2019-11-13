import mysql.connector
import yaml
import os
from django.conf import settings

basepath=settings.BASE_DIR

#basepath = os.path.abspath('..').replace('\\', '/'


def getConnection():
    cnx = mysql.connector.connect(user='cresta', password='nttdata@123',
                                  host='10.235.21.28', database='AITestEngine')
    return cnx
