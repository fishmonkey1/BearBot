from rest_framework.decorators import api_view
from rest_framework.response import Response

from bear_api.models import Report
from bear_api.modules.tweets import TweetsModule
from bear_api.serializers import ReportSerializer, SearchListSerializer
from bear_api.utils.auth import Auth
from bear_api.utils.constants import Constants
from bear_api.utils.logger import Logger

logger = None
twitter_api = None
twitter_module = None


@api_view(['GET'])
def lookup_user(request, *args, **kwargs):
    try:
        params = __get_whitelisted_params(request.query_params, args, kwargs)
        if params['account'] is not None:
            return Response({
                'searchedFor': params['account'],
                'users': twitter_module.find(params['account'], params['records'], params['page'])
            })
        else:
            raise Exception('Yo! I need the user account')
    except Exception as e:
        logger.log(str(e), Constants.FAILED_USER_SEARCH)
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def lookup_report(request, *args, **kwargs):
    try:
        report = Report.objects.get(id=int(kwargs['id']))
        return Response({'result': ReportSerializer(report).data})
    except Exception as e:
        logger.log(str(e), Constants.FAILED_REPORT_SEARCH)
        return Response({'error': 'Report Not Found'}, status=500)


@api_view(['POST'])
def generate_report(request, *args, **kwargs):
    try:
        report = __get_user_data(request.data)
        report['report'] = twitter_module.generate_analysis(report['user'], request.data['tweet_count'])
        save_report(report)
        return Response({'result': report})
    except Exception as e:
        logger.log(str(e), Constants.FAILED_REPORT)
        return Response({'error': 'Failed To Generate The Report'}, status=500)


@api_view(['GET'])
def fetch_search_list(request, *args, **kwargs):
    try:
        search_list = Report.objects.all()
        return Response({'result': SearchListSerializer(search_list, many=True).data})
    except Exception as e:
        logger.log(str(e), Constants.FAILED_RETRIEVENG_SEARCH_LIST)
        return Response({'error': 'Failed To Fetch The Search List'}, status=500)


def save_report(data):
    report = Report(
        user=data['user'],
        tweets=data['tweets'],
        followers=data['followers'],
        following=data['following'],
        verified=data['verified'],
        img=data['img'],
        description=data['description'],
        url=data['url'],
        analysis_positive=data['report']['analysis']['positive'],
        analysis_negative=data['report']['analysis']['negative'],
        analysis_neutral=data['report']['analysis']['neutral'],
        acceptance_positive=data['report']['acceptance']['positive'],
        acceptance_negative=data['report']['acceptance']['negative'],
        acceptance_neutral=data['report']['acceptance']['neutral']
    )

    report.save()


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
