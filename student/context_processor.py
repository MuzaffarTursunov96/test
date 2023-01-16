from student.models import Student


def get_pictures(request):
  student =Student.objects.get(user=request.user)
  return {'student':student}