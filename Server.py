import bottle
import json
import App
@bottle.route("/")
def serve_html():
  return bottle.static_file("index.html",root="")
@bottle.route("/frontend")
def serve_front_end_js():
  return bottle.static_file("front_end.js",root="")
@bottle.route("/serve_AJAX")
def serve_AJAX():
  return bottle.static_file("ajax.js",root="")
@bottle.post('/donut')
def serve_donut():
  decoding = bottle.request.body.read().decode()
  load_content=json.loads(decoding)
  year1=load_content["year_start"]
  year2=load_content["year_end"]
  pydictionary={"year_start":year1,"year_end":year2}
  newdata=App.data_by_subject(pydictionary)
  print(newdata)
  return json.dumps(newdata)
@bottle.post('/donut2')
def serve_donut2():
  decoding = bottle.request.body.read().decode()
  load_content=json.loads(decoding)
  year1=load_content["year_start"]
  year2=load_content["year_end"]
  pydictionary={"year_start":year1,"year_end":year2}
  newdata=App.avilability_(pydictionary)
  print(newdata)
  return json.dumps(newdata)