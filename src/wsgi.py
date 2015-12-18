import falcon


class Resource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = 'I will fuck you'

app = falcon.API()

resource = Resource()

app.add_route('/api', resource)