## jubilant-eureka
Tiny tools to create html pages for easy generating content for an chrome extension. Data is got from specific historical content sources. There are two files:

*finnametatofile.py*
gets data from API and generates intermediary .csv file 

*generatepages.py*
which generates html pages from the .csv file

(!) The output files are brutally *overwritten* so run in empty directory!



## Usage 

**Step1.**

    python finnametatofile.py  -i Mikkeli -o testfile.csv

Creates testfile.csv to current directory , while utilizing [Finna API](https://www.kiwi.fi/display/Finna/Finnan+avoin+rajapinta)
The -i defines the keyword, which is searched.

**Step2.** 

    python generatepages.py  -i testfile.csv -s finna
    
Creates 12 (or whatever is in MAXPAGES constant in script) HTML pages to current directory.

**Step3.** 

The .csv file can also be got from elsewhere, which can then be parsed in different way and allows continuing the numbering of the HTML pages onwards.

    python generatepages.py  -i mikkeli_clippings_sample.csv -s nlf -x 13

This generates pages continuing from given index (-x) , data is read from .csv  and the format expected is 'style' nlf (which generates bit different metadata).


## Notes

The scripts have been tested on Windows 7, with python 2.7.11 (Anaconda 4.0.0)


## Todo

* Could be simplified. 
* 2nd script assumes that .csv file have HTML encodings in place.
* Might croak if file sizes are not as expected (too few lines, etc.) 
* The output files are brutally *overwritten* so run in empty directory only!

## Example

Example of generated files can be found at:  [NLF_MIK_NEWSPICS repository ](https://github.com/TuulaP/NLF_Clippings_Extension/tree/master/nlf_mik_newspics)


----------
(These scripts are in different repo to enable easier packaging of the extension itself.)


> Written with [StackEdit](https://stackedit.io/).


