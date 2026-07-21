# Python Report generation is used using Report Creator library. 

# Self - contained -> includes base-64 encoded images. 
# versatile -> viewable in any web browser and easily printed to PDF 
# Images 
# data virualization / charts 
# customizable -> markdown support within components and labels/descriptions or other components. 
# flexible layouts -> components can be arranged horizontally or vertically or even as interactive side presentation. 

import report_creator as rc
import plotly.express as px

with rc.ReportCreator(title="My Network Report", description="A sample Report") as report: 
    view = rc.Block(
        rc.Heading("Sample Network Information", level=1),
        rc.Markdown("This is a simple report using **Report Creator**"),
        rc.Group(
            rc.Metric(heading="Records", value="1,024"),
            rc.Metric(heading="Accuracy", value="98.6", unit="%"),

        ),
        rc.Bar(px.data.medals_long(), x="nation", y="count", dimension="medal",
               label="Olympic Medals"),

    )
    report.save(view, "pyreport.html")
