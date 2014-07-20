from xml.dom import minidom
xmldoc = minidom.parse('******.xml')
itemlist = xmldoc.getElementsByTagName('****') 
print len(itemlist)
print itemlist[0].attributes['****'].value
for s in itemlist :
    print s.attributes['****'].value
