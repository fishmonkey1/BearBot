from rest_framework.views import APIView
from rest_framework.response import Response

from bear_api.utils.auth import Auth
from bear_api.utils.constants import Constants
from bear_api.utils.logger import Logger
from bear_api.modules.tweets import TweetsModule

logger = None
twitter_api = None
twitter_module = None


class Users(APIView):
    '''
        User APIView class that looks for the given user (Paginated)
    '''
    def get(self, request, *args, **kwargs):
        try:
            params = self.__get_whitelisted_params(request.query_params, args, kwargs)  # nopep8
            if params['account'] is not None:
                return Response({
                    'searchedFor': params['account'],
                    'users': twitter_module.find(params['account'], params['records'], params['page'])  # nopep8
                })
            else:
                raise Exception('Yo! I need the user account')
        except Exception as e:
            logger.log(str(e), Constants.RETRIEVENG_USER)
            return Response({'error': str(e)}, status=500)

    def __get_whitelisted_params(self, params, args, kwargs):
        queryp = dict({
            'account': kwargs['account'] if 'account' in kwargs else None,
            'records': params.get('records', 25),
            'page': params.get('page', 0)
        })

        return queryp


if twitter_api is None:
    logger = Logger()
    twitter_api = Auth().get_auth_connection()
    twitter_module = TweetsModule(twitter_api, logger)
