from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from template.account.account_protocol import AccountProtocol

protocol = AccountProtocol()

@api_view(['POST'])
def account_login(request):
    # request.data로 POST JSON 본문을 바로 받음 (request.POST는 form 데이터에서만 동작)
    req_data = request.data  # dict 타입
    result = protocol.account_login_req_controller(req_data)
    return Response(result)

@api_view(['POST'])
def account_block(request):
    req_data = request.data
    result = protocol.account_block_req_controller(req_data)
    return Response(result)