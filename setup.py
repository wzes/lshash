from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["things/*"]

setup(name = "lshash",
    version = "1.0",
    description = "lshash for py3",
    author = "xuantang",
    author_email = "xuantang.cun@gmail.com",
    url = "http://wzescxt.com",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = [""],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'package' : files },
    #'runner' is in the root.
    #scripts = ["test.py"],
    long_description = """Really long text here.""" 
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
)
