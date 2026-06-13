from rest_framework.exceptions import AuthenticationFailed
from .models import Empresa, Target


def get_empresa_from_headers(request):
    api_key = request.headers.get('X-Api-Key')

    if not api_key:
        raise AuthenticationFailed('Header X-Api-Key e obrigatorio.')

    try:
        empresa = Empresa.objects.get(hash=api_key)
    except Empresa.DoesNotExist:
        raise AuthenticationFailed('X-Api-Key invalida.')

    return empresa


def get_target_from_headers(request):
    empresa = get_empresa_from_headers(request)

    user_id = request.headers.get('X-User-Id')
    if not user_id:
        raise AuthenticationFailed('Header X-User-Id e obrigatorio.')

    target, created = Target.objects.get_or_create(
        empresa=empresa,
        user_id=int(user_id),
    )

    return target
