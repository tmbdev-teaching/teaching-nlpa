def stag(wt):
    w,t = wt
    if t=="Unk": return "<i>[{}]</i>".format(w)
    if t=="AT": return "<font size=-2>{}</font>".format(w)
    if t=="IN": return "<font color='#c08000' size=+2>{}</font>".format(w)
    if t=="CS": return "<font color='purple' size=+1>{}</font>".format(w)
    if t=="CC": return "<font color='purple' size=+1>{}</font>".format(w)
    if t[0]=="N": return "<font color='blue' size=+1>{}</font>".format(w)
    if t[:2]=="PP": return "<font color='#8080ff' size=+1>{}</font>".format(w)    
    if t[:2]=="DO" or t[:2]=="EX" or t[:2]=="HV" or t[:2]=="MD": 
        # do, be, have, modal
        return "<font color='red'>{}</font>".format(w)
    if t[0]=="V": 
        return "<font color='red' size=+2>{}</font>".format(w)
    if "JJ" in t: return "<font color='green'>{}</font>".format(w)
    if "RB" in t and "WRB" not in t: 
        return "<font color='#00c080''>{}</font>".format(w)
    return w

def stags(tagged):
    return " ".join([stag(x) for x in tagged])

def mstags(sentences):
    return "<p />\n".join(stags(s) for s in sentences)
