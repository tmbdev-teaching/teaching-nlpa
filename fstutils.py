# -*- coding: utf-8 -*-

from pylab import *
import openfst
from openfst import StdVectorFst as FST
from openfst import LogVectorFst as LFST

ASCII = openfst.SymbolTable("ASCII")

for i in range(127):
    if i==0:
        ASCII.AddSymbol("ϵ",i)
    elif i<=32: 
        ASCII.AddSymbol("$%02x"%i,i)
    else:
        ASCII.AddSymbol(chr(i),i)

def minimize(fst):
    dfst = FST()
    openfst.Determinize(fst,dfst)
    openfst.Minimize(dfst)
    return dfst

def log_minimize(fst):
    dfst = LFST()
    openfst.Determinize(fst,dfst)
    openfst.Minimize(dfst)
    return dfst

def show_fst(fst):
    import pydot,pylab
    graph = pydot.Dot(rankdir="LR")
    isyms = fst.InputSymbols()
    if not isyms: isyms = ASCII
    osyms = fst.OutputSymbols()
    if not osyms: osyms = ASCII
    for s in range(fst.NumStates()):
        if s==fst.Start():
            n = pydot.Node("%d"%s,shape="box")
            graph.add_node(n)
        if fst.IsFinal(s):
            l = '"'
            l += "%d"%s # node id
            if fst.Final(s).Value()!=0.0: # optional non-zero accept cost
                l += "/%s"%fst.Final(s).Value()
            l += '"'
            n = pydot.Node("%d"%s,label=l,penwidth="3")
            graph.add_node(n)
        for t in range(fst.NumArcs(s)):
            a = fst.GetArc(s,t)
            l = '"'
            l += '%s'%isyms.Find(a.ilabel)
            if a.olabel!=a.ilabel: l += ":%s"%osyms.Find(a.olabel)
            v = a.weight.Value()
            if v!=0.0: l += "/%s"%v
            l += '"'
            n = a.nextstate
            e = pydot.Edge("%d"%s,"%d"%n,label=l)
            graph.add_edge(e)
    graph.write_png("/tmp/_test.png")
    pylab.gca().set_xticks([]); pylab.gca().set_yticks([])
    pylab.clf()
    pylab.imshow(pylab.imread("/tmp/_test.png"))   

def fstsize(fst):
    edges = 0
    for s in range(fst.NumStates()):
        edges += fst.NumArcs(s)
    return fst.NumStates(),edges
