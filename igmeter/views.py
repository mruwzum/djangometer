from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import shuffle
import os, sys
from .forms import *
import sqlite3
from difflib import SequenceMatcher
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_FOLDER = os.path.join(BASE_DIR)
from igmeter.InstaMeter import *
from django.http.response import StreamingHttpResponse
from io import StringIO as StringIO 
from django.http import HttpResponse

from xlsxwriter.workbook import Workbook


# Just reads the results out of the dictionary. No real logic here.

def index(request):
    im = InstaMeter(username='elenabravoarche')
    im.analyze_profile()

    # listaResultado.append(im.print_top_liked())
    # listaResultado.append(im.print_top_commented())
    # listaResultado.append(im.print_top_viewed())
    context = {'res': im.print_account_statistic()}
    return render(request, 'igmeter/index.html',context)
# Create your views here.

def download_csv(request):
    with open('Statistics_of_@elenabravoarche.xlsx', 'rb') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Statistics_of_@elenabravoarche.xlsx'
    return response

