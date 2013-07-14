lines = [
    'canada goose',  'canada goose',  'long-tailed jaeger',  'canada goose',
    'snow goose',    'canada goose',  'canada goose',        'northern fulmar'
]

seen = set()
for line in lines:
    seen.add(line.strip())

for bird in seen:
    print bird
