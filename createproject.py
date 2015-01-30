#!/usr/bin/python
'''
This file creates a template project containing a main.py file, a README.md and LICENSE file.

Author: Nicolas Inden
eMail: nicolas.inden@smashnet.de
GPG-Key: http://files.smashnet.de/pubkey.asc
Date: 2014-08-04
License: MIT License
'''
from configobj import ConfigObj
import argparse
import os
import sys
import time
import datetime

def createSampleReadme(progdir, projectname, config):
    print "Creating README.md"
    datestr = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
    year = datetime.datetime.fromtimestamp(time.time()).strftime('%Y')
    with open(os.path.join(progdir, "SampleREADME.smp"), 'r') as sampleinput:
        with open(projectname + "/" + "README.md", 'w') as readme:
            for line in sampleinput:
                line = line.replace("<title>", projectname)
                line = line.replace("<author>", config['author'])
                line = line.replace("<email>", config['email'])
                line = line.replace("<xmpp>", config['xmpp'])
                line = line.replace("<twitter>", config['twitter'])
                line = line.replace("<gpgid>", config['GPG']['id'])
                line = line.replace("<gpglink>", config['GPG']['link'])
                line = line.replace("<gpgfingerprint>", config['GPG']['fingerprint'])
                line = line.replace("<year>", year)
                readme.write(line)
            readme.close()
        sampleinput.close()
        
def createSampleMain(progdir, projectname, config):
    print "Creating main.py"
    datestr = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
    with open(os.path.join(progdir, "SampleMain.smp"), 'r') as sampleinput:
        with open(projectname + "/" + "main.py", 'w') as pyfile:
            for line in sampleinput:
                line = line.replace("<author>", config['author'])
                line = line.replace("<email>", config['email'])
                line = line.replace("<xmpp>", config['xmpp'])
                line = line.replace("<twitter>", config['twitter'])
                line = line.replace("<gpgid>", config['GPG']['id'])
                line = line.replace("<gpglink>", config['GPG']['link'])
                line = line.replace("<gpgfingerprint>", config['GPG']['fingerprint'])
                line = line.replace("<date>", datestr)
                pyfile.write(line)
            pyfile.close()
        sampleinput.close()
        
def createSampleConfig(progdir, projectname, config):
    print "Creating config.ini"
    datestr = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
    with open(os.path.join(progdir, "SampleConfig.smp"), 'r') as sampleinput:
        with open(projectname + "/" + "config.ini", 'w') as conffile:
            for line in sampleinput:
                line = line.replace("<projectname>", projectname)
                conffile.write(line)
            conffile.close()
        sampleinput.close()
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("projectname", help="The projects name")
    args = parser.parse_args()
    
    progdir = os.path.dirname(os.path.abspath(sys.argv[0]))
    config = os.path.join(progdir, "config.ini")
    print "Using config: %s" % config
    config = ConfigObj(config)
    
    # Create directory
    try:
        os.mkdir("./" + args.projectname)
    except:
        print "Directory already exists."
        exit(1)
        
    try:
        # Create README.md
        createSampleReadme(progdir, args.projectname, config)
        # Create python file
        createSampleMain(progdir, args.projectname, config)
        # Create config file
        createSampleConfig(progdir, args.projectname, config)
        
        print "Success! Find your project stub here: ./%s" % args.projectname
    except:
        print "Something went wrong :("