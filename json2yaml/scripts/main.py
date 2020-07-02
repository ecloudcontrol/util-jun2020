import yaml # yaml and json converter
from flask import Flask, render_template, request #website builder
import json # formats json output

app=Flask(__name__) # defines the website

@app.route("/")
def landing_page():# for the blank url it returns the homepage html with buttons making viewers choose 
    return render_template("landing_pg.html")

@app.route("/yamaltojson")
def yaml_land_page():# if the user wants a json file they will get sent to this page from the json button
    return render_template("y2j_landing.html")

@app.route("/jsontoyaml")
def json_land_page(): # if the user wants a yaml file they will get sent to this page from the yaml button
    return render_template("j2y_landing.html")



@app.route("/y2j", methods=['POST'])
def convert_2_json():# when the user presses convert button they are sent to this html page
    yaml_=request.form["yaml_text"]# the user's input is stored in the yaml_ variable    
    json_ = json.dumps(yaml.safe_load(yaml_), indent=4) # pyyaml loads the yaml file then converts it to json
    #then json.dumps correctly formats the json output with proper indentation
    return render_template("json_home.html", conved_json =json_) #gives the user their a json file
@app.route("/j2y", methods=['POST'])
def convert_2_yaml():
    json_=request.form["json_text"]#gets the json file
    yaml_ = yaml.dump(yaml.safe_load(json_),default_flow_style=False, sort_keys=False)#formats the json file then converts it into yaml
    #then it is formatted with sort_keys function
    return render_template("yaml_home.html", convt= yaml_) # the html for the output and yaml file is sent to the html code








if __name__ == '__main__':
    app.debug = True #website is called and starts a server
    app.run()
