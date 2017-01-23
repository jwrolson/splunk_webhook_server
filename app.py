#!/usr/bin/env python
import json
import flask as f
import splunklib.client as client
import splunklib.results as results

app = f.Flask(__name__)

def get_splunk_data(sid):
	job = service.job(sid=sid)
	rr = results.ResultsReader(job.results())
	return rr

@APP.route("/splunk/webhook", methods=['POST'])
def splunk_webhook():
	webhook = f.request.json
	sid = webhook.get('sid')
	splunk_data = get_splunk_data(sid)
	return ""

@APP.route("/healthcheck", methods=['GET'])
def healthcheck():
	return('Alive')

if __name__ == "__main__":
	try:
		service = client.connect(host='https://splunk/',
								 port=8089,
								 username='admin',
								 password='changeme',
								 autologin=True)
		app.run(host='0.0.0.0', 
				threaded=True)

	except (KeyboardInterrupt, SystemExit):
		service.close()
