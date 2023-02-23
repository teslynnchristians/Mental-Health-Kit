#!/usr/bin/python3
"""creates a flask Blueprint and imports all views which use Blueprint"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.user import *
from api.v1.views.user/email import *
from api.v1.views.community tab import *
from api.v1.views. messagesimport *
from api.v1.views.suggestions import *
from api.v1.views.journaling import *
