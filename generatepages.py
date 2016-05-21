#!/usr/bin/env python

#script to generate the html files for the chrome extension

import sys
import csv
from optparse import OptionParser

MAXPAGES = 12

PAGEBASE = '''<html><head><link rel="stylesheet" type="text/css" href="page.css">
<title>New Tab</title>
</head>
<style type="text/css">
html {
   background: url("LINK1") no-repeat 0% 0% fixed; background-size: contain;
}
</style>


'''



def readCSV (filename):

    result=[]
    with open(filename, 'r') as csvfile:
        res = csv.reader(csvfile)

        for row in res:
            result.append(row)

#    print result

    return result


def saveToFile (filename, text):

    #print("Data: "+string+": tofile:"+filename+".")

    f = open(filename, 'w')
    f.write(str(text))
    f.close

    return filename




if __name__ == "__main__":

    parser = OptionParser()

    parser.add_option("-i", "--input",  type="string", dest="input", help="Input file name", metavar="input")
    parser.add_option("-s", "--source", type="string", dest="source", help="Source", metavar="source")
    parser.add_option("-x", "--index",  type="int", dest="index", help="Page generation index", metavar="index")


    (options, args) = parser.parse_args()

    if (not options.input):
        print("Please give the input file! \nData is expected in order of picLoc,picTitle,picId,picAuthor,picOrg,picRights")
        sys.exit(1)
    if (not options.source):
        options.source='nlf'


    rows    = readCSV(options.input)
    newpage = PAGEBASE
    imageid = 0

    if (options.index!=None):
        imageid = options.index-1


    if (len(rows) < MAXPAGES):
        print("Input file %s contains too few lines." % options.input)
        sys.exit()


    for row in rows[0:MAXPAGES]:
        newpage = newpage.replace("LINK1", row[0] )

        if options.source=='nlf':
            newpage +="<body><div class=\"image\"></div>" #add logo

            newpage+="<h1><span><a href=\"%s\">%s</A></span></h1>" % (row[1], row[2])  # link to clipping, title
            newpage+="<h2><span>%s, no. %s, p. %s</span></h2>\n" % (row[4],row[5],row[8])   # title , number, page
            newpage+="<h2><span>Pvm: "+row[6]+"</span></h2>\n"
            newpage+="<h2><a href=\"%s\">Koko sivu</A>" % row[7]+"</h2>"
            newpage+="<h2><span><a href=\"%s\">Lis&auml;&auml; aiheesta</A>"% row[3] +"</span></h2>\n"

        else:
            #could use some page gen. engine :)
            picLink = "<a href=\""+row[2]+"\"/>"+row[2]+" (&#128279;)</a>"

            newpage+="<h1>%s</h1>" % row[1]
            newpage+="<h2><span>%s</span></h2>\n" % picLink
            newpage+="<h2><span>%s</span></h2>\n" % row[3]
            newpage+="<h2><span>%s</span></h2>\n" % row[4]
            newpage+="<h3>%s</h3>" % row[5]


        imageid+=1
        filename = "%04d" % imageid  + ".html"
        saveToFile(filename,newpage)
        newpage=PAGEBASE


    print "%d files generated." % imageid



