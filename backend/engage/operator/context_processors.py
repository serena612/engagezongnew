from engage.operator.models import Operator


def region(request):
    return {'region': request.region}


def operator(request):
    return {'operator': Operator.objects.filter(region=request.region).first()}
