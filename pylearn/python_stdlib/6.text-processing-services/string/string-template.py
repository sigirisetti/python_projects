from string import Template
import sys

s = Template('$who likes $what')
s.substitute(who='tim', what='kung pao')

d = dict(who='tim')


#Template('Give $who $100').substitute(d) #invliad place holder


try:
    print(Template('$who likes $what').substitute(d))
except:
    print("Exception : ", sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])


print(Template('$who likes $what').safe_substitute(d))