from flask import Flask, request, sessions, redirect, url_for,\
        abort, render_template, flash, Blueprint, escape, Response
from app.database import db_session
from app.models.services import Service
import json
import ast


main = Blueprint('main', __name__)


@main.route('/api/json', methods=['GET'])
def show_all():
    s = Service.query.all()
    templist = []
    for n in s:
        templist.append({'id':n.id, 'name':n.name, 'description':n.description, 'primary_support':n.primary_support})
    js = json.dumps(templist)

    resp = Response(js, status=200, mimetype='application/json')

    return resp

@main.route('/api/new', methods=['GET', 'POST'])
def new_item():

    data = ast.literal_eval(json.dumps(request.json))
    s = Service(name=str(data['name']), description=str(data['description']), primary_support=str(data['primary_support']))
    db_session.add(s)
    db_session.commit()
    return 'Success'
