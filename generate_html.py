import markdown

with open('report.md', 'r') as f:
    report_md = f.read()

reportHTML = markdown.markdown(report_md)

with open('html/index.html', 'w') as f:
    f.write(reportHTML)
