from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pages.models import Robot
from pages.forms import RobotForm

@login_required(login_url='login')
def home_page(request):
    
    robot = Robot.objects.all()
    robot_count = robot.count()

    context = {'robot': robot, 'robot_count': robot_count}
 
    return render(request, 'home.html', context)


