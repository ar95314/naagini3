m=raw_input()
"""if all(c in '01' for c in m):
    print "Yes"
else:
    print "No"
    """
if not(m.translate(None,'01')):
    print "Yes"
else:
    print "No"
