#----------------------------------------------------------------------
#This utility sets up the python configuration files so as to
#allow Python to find files in a specified directory, regardless
#of what directory the user is working from.  This is typically
#used to create a directory where the user will put resources shared
#by many Python scripts, such as courseware modules
#
#----------------------------------------------------------------------
#Usage:
#    (1) Put a copy of this file (setpath.py) in the directory
#        you want to share
#
#    (2) Execute setpath.py, either by opening it and running it
#        in Canopy, or from the command line by changing director
#        to the directory you want to share and then typing
#                        python setup.py
#        If you run it by opening it in the Canopy editor you need to
#        select the directory popup menu item that tells Canopy to
#        change the working directory to the Editor directory.
#        in Canopy, the working directory always appears at the upper
#        right corner of the Python interpreter window. 
#
#----------------------------------------------------------------------
#Notes:
#
#    This will create a startup file which will properly 
#    initialize ipython (whether used directly or via Enthought
#    Canopy) to find your files, and will do that regardless
#    of your operating system.
#
#    If you are using a Linux or Mac OSX operating system, it
#    will also edit your .cshrc and .bash_profile shell startup
#    scripts to set the environment variable PYTHONPATH so that
#    any version of the python interperter started from the 
#    command line (i.e. whether ipython or python) will find
#    the shared files.  This feature will not work on
#    Windows operating systems, so Windows users should start
#    either start up python by clicking on the Canopy app, or
#    by starting ipython from the command line. It is possible
#    to set the PYTHONPATH environment variable in Windows,
#    but this script does not yet implement that feature. 
#
#    Note that it is also possible to manually set up a temporary
#    shared path (for example /home/MyModules) in a given script 
#    by executing the lines:
#
#    import sys
#    sys.path.append('home/MyModules')
#
#    where you would replace '/home/MyModules') with the
#    actual full path to the directory you want on your own
#    system
#----------------------------------------------------------------------
import os,glob,platform

#Utility function to return an acceptable filename for the
#startup file
def makeFileName(startupDir):
    files = glob.glob(os.path.join(startupDir,'*.py'))
    #Make a startup filename that doesn't already exist
    for i in range(10000):
        if i<100:
            fname = '%02d-startup.py'%i
        else:
            fname ='%04d-startup.py'%i
        fname = os.path.join(startupDir,fname)
        if not fname in files: break
    return fname
#
#--------Main program starts here
#
#Get current path
curPath = os.getcwd()
#Get home directory
home = os.path.expanduser('~')
#
#If this is a Linux or Mac OS X system, edit the
#shell initialization files to set the PYTHONPATH environment
#variable
if ( (platform.system()=='Darwin') or ('inux' in platform.system())):
    #We are on a Linux or Mac system. Edit Shell startup files
    print 'This is a Linux or Mac system. Adding path to shell startup scripts'
#
    #csh script: (Note, should also do this for .tcshrc if it exists)
    cshFile = os.path.join(home,'.cshrc')
    print 'csh family -- Editing '+cshFile
    #Make backup copy of file
    os.system('cp %s %s'%(cshFile,cshFile+'.setPathBackup'))
    #Append line to set PYTHONPATH
    outfile = open(cshFile,'a')
    outfile.write('#Line added by setPath.py. Original in %s\n'%(cshFile+'.setPathBackup'))
    #Note: the double quotes allow paths to contain spaces
    outfile.write('setenv PYTHONPATH \"%s:$PYTHONPATH\"\n'%curPath)
    outfile.close()
#
    #bash script (ToDo: also edit .profile, for sh users)
    bashFile = os.path.join(home,'.bash_profile')
    print 'sh family -- Editing '+bashFile
    #Make backup copy of file
    os.system('cp %s %s'%(bashFile,bashFile+'.setPathBackup'))
    #Append line to set PYTHONPATH
    outfile = open(bashFile,'a')
    outfile.write('#Line added by setPath.py. Original in %s\n'%(bashFile+'.setPathBackup'))
    #Note: the double quotes allow paths to contain spaces
    outfile.write('export PYTHONPATH=\"%s:$PYTHONPATH\"\n'%curPath)
    outfile.close()
 
#
#
#Set paths for ipython startup. This takes care of starting up ipython from
#double-clicking the Canopy app on any operating system
#
profilepath = os.path.join(home,'.ipython/profile_default/startup')
if os.path.isdir(profilepath):
    fname = makeFileName(profilepath)
else:
    print "Could not find .ipython startup directory. Exiting."
    exit(1)
#
#Write the startup file
contents = 'import sys \nsys.path.append(\'%s\')\n'%curPath
outfile = open(fname,'w')
outfile.write(contents)
outfile.close()