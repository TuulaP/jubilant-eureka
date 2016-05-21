#!/usr/bin/env python
# -*- coding: utf-8 -*-

# gets few theme based images from Finna and creates a csv list of them to be used later.
# -i  gives the keyword to searchfor
# -o  filename where data is written

from urllib import urlopen
import pprint
import simplejson as json
import sys
import unicodecsv
import random
import os.path


finnarecord    = "https://finna.fi/Record/"
finnapicprefix = "https://api.finna.fi"
url            = 'https://api.finna.fi/v1/search?filter[]=online_boolean:"1"&filter[]=format:"0/Image/"&lookfor="'
CSVSEP = ","
QUOTE  = '"'
EMPTY  = "-"
WANT   = 12


def seekFinna(topic):

    result = urlopen(url+topic).read()
    result = json.loads(result)
    result = result.get('records')

    #print "data searched:" + url + topic + "\n"
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(result)

    random.shuffle(result) # randomize list order to get different set later on.
    resultArr = []

    for resultSet in result[0:WANT]:  #gets the needed fields from json to variables

        picId=finnarecord + resultSet['id']

        image = resultSet['images'][0]
        picLoc = finnapicprefix + image

        rights = resultSet['imageRights']

        #this could be done elsewhere
        picRights = "<a target=\"_new\" href=\""+ rights['link'] +"\">" + rights['copyright'] + "</A><br>"+ rights['description'][0]
        picRights= picRights.encode('ascii','xmlcharrefreplace')

        picTitle = resultSet['title']

        picOrg = resultSet['buildings'][0:2]
        picOrgs  = ""
        for subOrg in picOrg:
            picOrgs += subOrg['translated'] + "/"

        #Not all images have author, but tries to get them when they exist. Assuming only 1 in images
        try:
            picAuthor = resultSet['nonPresenterAuthors'][0]['name'].encode('ascii','xmlcharrefreplace')
        except:
            picAuthor = EMPTY

        resultArr.append([picLoc,picTitle,picId,picAuthor,picOrgs[:-1],picRights])


    return resultArr


def saveToCSV (filename, text):

    with open (filename, 'wb') as csvfile:
        f = unicodecsv.writer(csvfile, delimiter=CSVSEP)
        for row in text:
            f.writerow(row)


    return filename






if __name__ == "__main__":


    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("-i", "--input", type="string", dest="theme",help="Theme or keyword", metavar="theme")
    parser.add_option("-o", "--output", type="string", dest="output",help="outputfile", metavar="theme")

    (options, args) = parser.parse_args()


    if (len(options.theme)==0):
        print("Please give a theme (keyword) to search for with -i parameter")
        sys.exit()

    if (options.output==None):
        print("Please give output file name with option -o")
        sys.exit()

    if os.path.isfile(options.output) :
        print("Warning, %s file exists, please give output file name with option -o") % options.output
        sys.exit()


    resultsArr = seekFinna(options.theme)

    if len(resultsArr) > 0 :
        saveToCSV(options.output, resultsArr)
        print("File %s written.") % options.output


