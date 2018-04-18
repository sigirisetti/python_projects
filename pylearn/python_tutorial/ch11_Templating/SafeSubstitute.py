from string import Template

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')

print(t.safe_substitute(d))