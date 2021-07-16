from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def employeeList(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def employeeById(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def employeeCreate(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def employeeUpdate(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def employeeDelete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return Response('Deleted!')
