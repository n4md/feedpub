# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404 ##ADDED get_object_or_404 12.5.18@5:22a
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse ##ADDED HttpResponseRedirect, JsonResponse 12.5.18@5:22a

###ORIGINAL###
## Create your views here.
#def index(request):
#    return HttpResponse("Hello, world! This is our first view.")

##ADDED all below 12.5.18@5:24a
from django.urls import reverse
from django.template import loader
from django.utils import timezone
from django.core import serializers
import datetime
import operator
import uuid
import json
import sqlite3

from .models import Feed, Feeditem

# Create your views here.
def index(request):
    latest_feed_list = Feed.objects.order_by('-lastUpdate')[:5]
    template = loader.get_template('feedpub/index.html')
    context = {
        'latest_feed_list': latest_feed_list,
    }
    return HttpResponse(template.render(context, request))

def alexafile(request, feed_id):
    feed_dict = {}
    conn = sqlite3.connect('db.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT uid, updateDate, titleText, contentText, streamUrl, redirectionUrl FROM feedpub_feeditem WHERE feed_id = ? ORDER BY updateDate DESC LIMIT 5', (feed_id,))
    tuple_list = c.fetchall()
    #print(tuple_list[0][0])
    conn.close()
    for item in tuple_list:
        feed_dict[item[0]] = {
            "uid": item[0],
            "updateDate": item[1],
            "titleText": item[1].isiso(),
            "mainText": item[3],
            "streamUrl": item[4],
            "redirectionUrl": item[5]
        }
        print(item[0] + item[1] + item[2] + item[3] + item[4] + item[5])
    dict_list = list(feed_dict.values())
    #print(feed_dict)
    #return JsonResponse(dict_list, safe=False)
    return HttpResponse(json.dumps(dict_list, ensure_ascii=False, encoding="utf-8"), content_type="application/json; charset=utf-8")

def googlefile(request, feed_id):
    response = "You're looking at the Google file for feed id = %s" % feed_id
    return HttpResponse(response)

def feed(request, feed_id):
    #Make list of all feed items that belong to the feed_id
    #feedobj = Feed.objects.get(id = feed_id)
    feeditem_list = Feeditem.objects.filter(feed = feed_id).order_by('-updateDate')[:5] #TODO Optimize this logic
    #feeditem_list = list_a.sort(key=updateDate, reverse=False)
    #auths = Author.objects.order_by('-score')[:30]
    #ordered = sorted(auths, key=operator.attrgetter('last_name'))
    #filtered_feeditem_list = []
    #for item in feeditem_list:
    #    if str(feedobj.feedName) == str(item.feed):
    #        filtered_feeditem_list.append(item)

    template = loader.get_template('feedpub/feed.html')
    context = {
        'feeditem_list': feeditem_list,
    }
    return HttpResponse(template.render(context, request))

def feeditem(request, feeditem_id):
    return HttpResponse("You're looking at feed item id = %s" % feeditem_id)

def newitem(request):
    feed_list = Feed.objects.all()
    template = loader.get_template('feedpub/newitem.html')
    #latest_feed_list = Feed.objects.order_by('-lastUpdate')[:5]
    context = {
        'feed_list': feed_list
    }
    return HttpResponse(template.render(context, request))

def createnewitem(request, newitem_id):
    if request.method == 'POST':
        n = newitem(request.POST)
        if n.is_valid():
            uid = str(uuid.uuid4())
            timestamp = time.time()
            updateDate = str(datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))
            titleText = 'Test Titles 2'
            streamUrl = ''
            mainText = 'Test contents 2'
            redirectionUrl = ''
