from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Robot
from .forms import RobotForm


@login_required(login_url='login')
def robot(request):
    
    robot = Robot.objects.all()
    robot_count = robot.count()

    context = {'robot': robot, 'robot_count': robot_count}

    return render(request, 'pages/robot/robot.html', context)

@login_required(login_url='login')
def add_robot(request):    
    forms = RobotForm()
    if request.method == 'POST':
        forms = RobotForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('robot')
    robot = Robot.objects.all()
    context = {'forms': forms, 'robot': robot}
    
    return render(request, 'pages/robot/add_robot.html', context)

def edit_robot(request, robotname):
    robotName = Robot.objects.get(name=robotname)
#    print("ROBOT NAME", robotName)

    robot_info_form = RobotForm(instance=robotName)
    
    if request.method == 'POST':
        robot_info_form = RobotForm(request.POST, instance=robotName)
    
        if robot_info_form.is_valid():
            robot_info = robot_info_form.save(commit=False)
            robot_info.save()
            return redirect('robot')
    
    context = {
        'robot_info_form': robot_info_form
        }
    
    return render(request, 'pages/robot/edit_robot.html', context)

def delete_robot(request, robotname):
    try:
        robot = get_object_or_404(Robot, name=robotname)
        robot.is_delete = True
        robot.save()
        # Redirect to some appropriate URL after successful deletion
        return redirect('robot')  # Assuming 'robot_list' is the name of the URL pattern for listing robots
    except Robot.DoesNotExist:
        # Handle the case where the robot does not exist
        return HttpResponse("Robot not found", status=404)
    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred:", e)
        return HttpResponse("An error occurred", status=500)
