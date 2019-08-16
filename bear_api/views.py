from rest_framework.decorators import api_view
from rest_framework.response import Response

from bear_api.models import Report
from bear_api.modules.tweets import TweetsModule
from bear_api.serializers import ReportSerializer
from bear_api.utils.auth import Auth
from bear_api.utils.constants import Constants
from bear_api.utils.logger import Logger

logger = None
twitter_api = None
twitter_module = None


@api_view(['GET'])
def lookup_user(request, *args, **kwargs):
    try:
        params = __get_whitelisted_params(request.query_params, args, kwargs)  # nopep8
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


@api_view(['GET'])
def lookup_report(request, *args, **kwargs):
    try:
        report = Report.objects.get(id=int(kwargs['id']))
        return Response({'result': ReportSerializer(report).data})
    except Exception as e:
        logger.log(str(e), Constants.RETRIEVENG_USER)
        return Response({'error': 'Report Not Found'}, status=500)


@api_view(['POST'])
def generate_report(request, *args, **kwargs):
    report = __get_user_data(request.data)
    report['analysis'] = twitter_module.generate_analysis(report['user'], request.data['tweet_count'])  # nopep8
    return Response({'result': report})


def __get_whitelisted_params(params, args, kwargs):
    return dict({
        'account': kwargs['account'] if 'account' in kwargs else None,
        'records': params.get('records', 25),
        'page': params.get('page', 0)
    })


def __get_user_data(data):
    return {
        'user': data['user'],
        'url': data['url'],
        'img': data['img'],
        'description': data['description'],
        'tweets': data['tweets'],
        'verified': data['verified'],
        'followers': data['followers'],
        'following': data['following']
    }

if twitter_api is None:
    logger = Logger()
    twitter_api = Auth().get_auth_connection()
    twitter_module = TweetsModule(twitter_api, logger)
