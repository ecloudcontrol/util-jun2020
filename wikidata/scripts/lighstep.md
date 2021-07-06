//Run these commands in your terminal 

pip install opentelemetry-launcher

opentelemetry-bootstrap --action=install


//go to 
https://app.lightstep.com

//make an account then click on the gear on the lefthand side to get your access token 

//copy the token and run the command below replacing <ACCESS TOKEN> with the access token you got from lightstep 

export LS_ACCESS_TOKEN="<ACCESS TOKEN>"


//click on the hamburger icon and add a service called 'hello-client' and then run the command 
export LS_SERVICE_NAME="hello-client"



//then run this in your terminal
opentelemetry-instrument python3 wikiData.py

//on the lightstep click the clock on the left to see the latency logs

