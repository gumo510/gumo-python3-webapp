#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Gumo'

' url handlers '

from coroweb import get, post
from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
