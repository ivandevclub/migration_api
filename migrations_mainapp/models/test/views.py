from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError
from ..postgres.models import SocioPg

def testdb(request):
    try:
        with connections['postgres'].cursor() as cursor:
            cursor.execute('SELECT * FROM socios."Socio"')
            result = cursor.fetchall()
        return JsonResponse({"message": "Conexión a la base de datos PostgreSQL exitosa", "result": result}, status=200)
    except OperationalError as e:
        return JsonResponse({"error": str(e)}, status=500)
