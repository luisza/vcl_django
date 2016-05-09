#!/bin/bash



#python manage.py graph_models --pydot -a -g -o my_project_visualized.png

function graph(){
	python manage.py graph_models --pydot $1 -o pngs/$1.png
}
graph authentication
graph compute
graph core
graph image
graph logs
graph managementnode
graph nat
graph openstack
graph provisioning
graph reservations
graph scheduling
graph authorization
