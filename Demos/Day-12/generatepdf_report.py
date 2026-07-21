# convert the HTML to PDF files using Python reports. 

# Use Jinja2 templates to inject the data into an HTML skeleton, then export it using WeasyPrint. 

from jinja2 import Template 
from weasyprint import HTML 

#1. Define the HTML structure and CSS styles 

html_template = """
<html>
<head>
 <styles>
  body { font-family: Arial, sans-serif; margin: 40px; color: #333;}
  h1 {color: #0056b3; border-bottom; 2px solid #0056b3;}
  table {width: 100%; border-collapse: collapse: margin-top: 20px;}
  th, td {border:1px solid #ddd; padding: 12px; text-align: left;}
  th {background-color: #f2f2f2; }
  </style>
  </head>
  <body>
   <h1> Network System Status Report </h1>
   <p> Generated for : <strong> {{ Company Name }} </strong></p>
   <table>
    <tr><th> Metric </th><th> Value </th></tr>
    {% for key, val in metrics.items() %}
    <tr><td>{{ key }}</td><td> {{ val }}</td></tr>
    {% endfor %}
</table>
</body>
</html> 
"""

# 2. Inject the raw data 
data = {
    "company_name" : "Cisco corp",
    "metrics": {"Device Uptime": "99.98%", "Active Users Connected": "1", "Errors": "3"}

}
rendered_html = Template(html_template).render(data)

#3. Export directly the report into PDF format 
HTML(string=rendered_html).write_pdf("device_report.pdf")