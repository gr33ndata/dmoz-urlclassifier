DMOZ URL Classifier
===================

DMOZ is the largest, most comprehensive human-edited directory of the Web. It was historically known as the Open Directory Project (ODP). It contains a categorized list of Web URLs. Their listings are updated on a monthly bases and published in [RDF files](http://rdf.dmoz.org/rdf/).

In my [research project](http://tarekamr.appspot.com/msc/presentation), I work on classifying web-pages based on their URLs only, hence DMOZ dataset is one of the datasets I use in my research. 

If you are going to download their RDF files, you can find to scripts here that are useful to you.

* dmoz2csv.py: This scripts converts their RDF data into a CSV file. Each line of CSV file contains a uniqie ID, URL and the category of that URL as seen in DMOZ.

* csv2traintest.py: Then this script can take the resulting CSV from above and convert it into training and test datasets as explained by [Bykan et al](http://dl.acm.org/citation.cfm?id=1526880).

Feeding "csv2traintest.py" on "dmoz0409.csv" will result in producing 15 training and test file pairs.

      
Contacts
--------
 
+ Name: [Tarek Amr](http://tarekamr.appspot.com/)
+ Twitter: [@gr33ndata](https://twitter.com/gr33ndata)
