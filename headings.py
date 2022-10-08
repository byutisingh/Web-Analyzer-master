#import downloader as dd
import analyzer as an
data="<p><h1>gvhghgfhgfhf</h1></p> <h2>visohfl</h2><p>hfslks</p>"
headings=an.GetHeadings(data)
print(headings[0].text)
