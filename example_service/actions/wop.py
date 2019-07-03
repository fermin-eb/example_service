from conformity import fields

from pysoa.server.action import Action


class WopAction(Action):
    request_schema = fields.Dictionary({
        # Request bodies are always dictionaries. Here we say we want a dict with exactly one input
        'amazing': fields.Integer(),
    })

    response_schema = fields.Dictionary({
        'wop': fields.UnicodeString(),
    })

    def run(self, request):
        number_amazing = request.body['amazing']
        wop = 'wop' * number_amazing
        return {
            'wop': wop
        }
