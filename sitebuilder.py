
# A Flask app for building the website from Markdown
# ideas from: https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/

# Apr 05, 2015,  @akaak

import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

# Top nav bar links. path : link-desc
app.config['navigation'] = {"page1" : "Page1 Link", "page2" : "Page2 Link" }

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html', page=page)

if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		app.run(port=8000)
