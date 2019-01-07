from flask import Flask, jsonify, make_response, url_for
from flask_httpauth import HTTPBasicAuth
from sqlalchemy import * 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Starting application')

Base = declarative_base()
Tablename = 'mytable'

class MyTable(Base):
    __tablename__ = Tablename
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    value = Column(String(100))

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return "<MyTable(%s, %s)>\n" % (self.name, self.value)

# main calculator class
class Calculator(object):

    def add(self,x,y):
       return x+y 

class DBTest():
    def init(self):
        # configure database connection
        try:
            print('start init')
            self.engine = create_engine('mysql://root:password1@db/testowa1')
            self.Session = sessionmaker(bind=self.engine)
            self.session = self.Session()
        except Exception, e:
            logger.error('cannot connect to database: %s' % e)
            print('cannot connect')

    def get_values(self):
        try:
            self.init()
            records = self.session.query(MyTable).filter(MyTable.id==28).limit(1).all()
            return str(records)
        except Exception,e:
            logger.error('get_values: cannot connect to database: %s' % e)
            return 'Cannot connect to database\n'

application = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == "blam":
        return 'python'
    return None

@auth.error_handler
def unauthorised():
    return make_response(jsonify({'error':'Unauthorised access'}),401)

@application.route('/')
def index():

    logger.info('Getting / ')
    return "Hello world\n"

@application.route('/add/<int:number1>/<int:number2>')
@auth.login_required
def count(number1,number2):
    calc = Calculator()
    mynumber = calc.add(number1,number2)
    return jsonify(mynumber) 

@application.route('/hellodb')
def hellodb():

    logger.info('getting /hellodb')
    try:
        dbtest = DBTest()
        records = dbtest.get_values()
        return records
    except Exception,e:
        logger.error("error: %s" % e)
        return 'Cannot connect to database\n'

@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),200)

if __name__ == "__main__":
    application.run(host='0.0.0.0',port='5555',debug=True)
