# Run the Python script to render the Jinja template 

# Summary for Core Jinja syntax delimiters 

# {{ expression }} : Prints the expression or variable output in Jinja to the final text 

# {% statement %} : Runs the control structure logic like loops (for) or decisions (if)
# 
# {# comment #} : Internal comments which are dropped entirely during generation and wont appear in the final file. 
# 
 
from jinja2 import Environment, FileSystemLoader

# 1. configure Jinja to load templates from the root or templates directory

env = Environment(loader=FileSystemLoader("templates"))

# 2. load the specific jinja template file 

template = env.get_template("profile.html")

# 3. Define the dynamic data payload 

data = {
    "user_name" : "Cisco_Device",
    "is_premium" : True, 
    "achievements": ["Advanced Routers", "Completed configurations", "SLA support"]
}

# 4. Render the template by passing the data variables 

rendered_html = template.render(**data)

# 5. print the output or save it to a new file 

print(rendered_html)

# optional: Save the Jinja rendered dynamic results directly into a file 

with open("output.html", "w", encoding="utf-8") as file:
    file.write(rendered_html)