import os
import subprocess

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.before_request
def to_pdf():
  if 'toPdf' in request.args:
    url = f"{request.base_url.removesuffix('/pdf')}?hide_print_link=true"
    subprocess.call(['wkhtmltopdf', url, 'output.pdf'])
    request.args = {
      k:v for k,v in request.args.to_dict().items() if k != 'toPdf'
    }
    return redirect(url_for(request.endpoint))


@app.route('/')
def index():
  return render_template('index.html')


def run():
  os.environ['FLASK_ENV'] = 'development'
  app.run("0.0.0.0", debug=True)
