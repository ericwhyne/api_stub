import logging
from flask import Flask
from flask.ext.restful import Api, Resource, reqparse
from flask.ext.restful.representations.json import output_json
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

output_json.func_globals['settings'] = {'ensure_ascii': False,
                                        'encoding': 'utf8'}

app = Flask(__name__)
api = Api(app)

logging.basicConfig(format='%(levelname)s %(asctime)s %(filename)s %(lineno)d: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class StubAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # Takes a single argument, content, and coerces its type to a list
        self.reqparse.add_argument('content', type=list, location='json')
        super(StubAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        content = args['content']

        logger.info('Started processing content.')
        try:
            # Modify this portion to work with your unique code
            temp_output = []
            for x in content:
                temp_output.append(x['HOLD_KEY'])
            logger.info('Finished processing content.')
        except Exception as e:
            # If something goes wrong, log it and return nothing
            logger.info(e)
            # Make sure to update this line if you change the variable names
            temp_output = {}

        return temp_output


api.add_resource(StubAPI, '/')

if __name__ == '__main__':
    # Fires up a server on port 5000 at '/'
    # i.e., http://localhost:5000/
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()
