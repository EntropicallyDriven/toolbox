# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:29:37 2017

@author: Joshua
"""

import re
import numpy as np

class node:
    def __init__(self, tag, mods, content=None, subs=[]):
        self.tag = tag
        
        self.content = content
        self.subs = subs[:]
        for x in subs:
            x.sups.append(self)
        self.sup = None
        
        self.mods = {}
        if mods is not '':
            mods = re.sub('"','',mods)
            mods = mods.split(' ')
            for mod in mods:
                res = re.search('(.+)=(.+)',mod)
                if res is not None:
                    self.mods[res.group(1)] = res.group(2)


    def __str__(self):
        return self.tag
    
    def __repr__(self):
        return self.tag

    def linksub(self,sub):
        self.subs.append(sub)
        sub.sup = self

    def addcontent(self,cont):
        self.content = cont
    
    def prunesup(self):
        self.sup = None

def buildtree(raw):
    tag = re.compile('<(?P<tag>[^>]+)\s*(?P<mods>[^>]*)>(?P<content>.*?)</(?P=tag)>(?P<remain>.*)')
    thislevel = tag.search(raw)
    
    if thislevel is not None:
        thistag = thislevel.group('tag')
        mods = thislevel.group('mods')
        content = thislevel.group('content')
        
        thisnode = node(thistag, mods, content)
        
        nextcons = []
           
        while content is not '':
            nextlevel = tag.search(content)
            if nextlevel is not None:
                remain = nextlevel.group('remain')
                content = re.sub(remain, '', nextlevel.group())
                nextcons.append(content)
                content = remain
            else:
                content = ''        
        
        for con in nextcons:
            newnode = buildtree(con)
            if newnode is not None:
                thisnode.linksub(newnode)
            
        return thisnode
        
    else:
        return None
    
def findtag(tree,tag):
    matches = []
    if tree.subs is not []:
        for leaf in tree.subs:
            if leaf.tag == tag:
                matches.append(leaf)
            if leaf.subs is not []:
                submatches = findtag(leaf,tag)
                if submatches is not []:
                    for x in submatches:
                        matches.append(x)
    return matches

def getHeaders(file):
    file.seek(0)
    record = file.read()
    
    spaces = re.compile(r'([\t,\n])')
    glob = re.sub(spaces, '', record)
    tree=buildtree(glob)
    
    datatag = findtag(tree, 'dataPoints')[0]
    headers = []
    for sub in datatag.subs:
        if 'startPosition' in [x.tag for x in sub.subs]:
            headers.append('XRD_'+sub.mods['axis'])
        elif sub.tag in ['beamAttenuationFactors', 'intensities']:
            headers.append('XRD_'+sub.tag)
    #headers.append('XRD_FullConfig')
    return headers
    
def getData(file):
    file.seek(0)
    record = file.read()
    
    spaces = re.compile(r'([\t,\n])')
    glob = re.sub(spaces, '', record)
    tree=buildtree(glob)
    
    datatag = findtag(tree, 'dataPoints')[0]
    data = []
    for sub in datatag.subs:
        if 'startPosition' in [x.tag for x in sub.subs]:
            start = float(sub.subs[0].content)
            end = float(sub.subs[1].content)
            length = len(findtag(tree, 'intensities')[0].content.split(' '))
            data.append(np.linspace(start,end,length))
        elif sub.tag in ['beamAttenuationFactors', 'intensities']:
            val = sub.content.split(' ')
            val = [float(x) for x in val]
            data.append(val)
    return data
   

   