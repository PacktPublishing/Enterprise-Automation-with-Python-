from jinja2 import Template

template = Template('Hello {{ name }}!')
print(template.render(name='John Doe'))


t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
print(t.render())

