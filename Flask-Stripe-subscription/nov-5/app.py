#rahul pandit

#verify account and save
#https://www.youtube.com/watch?v=Y9EpPc19xjw

#https://www.youtube.com/watch?v=oZwyA9lUwRk

#refrence 
#https://stripe.com/docs/api/charges/create
#

from flask import Flask, render_template, url_for, request, abort
import stripe
import json

# settings.py
from dotenv import load_dotenv
load_dotenv()
# ===================================
import os
import time


app = Flask(__name__)
app.config['STRIPE_PUBLIC_KEY'] = os.getenv("STRIPE_PUBLIC_KEY")
app.config['STRIPE_SECRET_KEY'] = os.getenv("STRIPE_SECRET_KEY")


planData={"Basic":"price_1Hk5NrBZLa0Pd5BpUOpNfvjM","Enterpreneur":"price_1Hk5OoBZLa0Pd5Bp5HjPBeLE","Professional":"price_1Hk5PUBZLa0Pd5BpaP4XeifN"}

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route('/SelectPlanForSubscription')
@app.route('/')
def index():
	return render_template('index.html')
	

@app.route('/Subscription/checkout',methods=['GET','POST'])
def Subscriptioncheckout():
	if request.method=='POST':
		amount=request.form['price']
		workspace=request.form['workspace']
		SubscriptionPlan=request.form['SubscriptionPlan']

		print(SubscriptionPlan+"-----------------------------------------")

		return render_template('form.html',amount=amount,workspace=workspace,SubscriptionPlan=SubscriptionPlan)
	else:
		return render_template("index.html")
	


@app.route('/charge',methods=['GET','POST'])
def charge():
	if request.method=='POST':

		email='rahul@metaorigins.com'
		amount=int(request.form['amount'])


		SubscriptionPlanType=request.form['SubscriptionPlan'] #exm basic premieum...


		customer=stripe.Customer.create(
			email=email,
			name=request.form['Nickname'],
			source=request.form['stripeToken'],
		  description=request.form['address'],
		  # address=request.form['address']
		)


		# create subscription here


		subscriptionData=stripe.Subscription.create(
		  customer=customer,
		  items=[
		    {"price": planData[SubscriptionPlanType]}, #get id from planData using SubscriptionPlanType key
		  ],
		)


		# print(subscriptionData)

		json_object = json.dumps(subscriptionData, indent = 4) 

		subscriptionData=dict(subscriptionData)

		print(type(subscriptionData))
		print("-------------------------------------------------------------")
		print(subscriptionData['id'])

		subscrID = subscriptionData['id']; 
		custID = subscriptionData['customer']; 
		planID = subscriptionData['plan']['id']; 
		planAmount = (subscriptionData['plan']['amount']/100); 
		planCurrency =subscriptionData['plan']['currency']; 
		planinterval = subscriptionData['items']['data'][0]['price']['recurring']['interval']
		PlanName=SubscriptionPlanType
		planIntervalCount = subscriptionData['plan']['interval_count'];
		created = time.strftime("%D %H:%M", time.localtime(int(subscriptionData['created'])));
		current_period_start = time.strftime("%D %H:%M", time.localtime(int(subscriptionData['current_period_start']))) 
		current_period_end = time.strftime("%D %H:%M", time.localtime(int(subscriptionData['current_period_end'])))
		status = subscriptionData['status']; 


		JsonData={"planPrice":amount,"statusMsg":"Your Subscription Payment has been Successful!","subscrID":subscrID,"custID":custID,"planID":planID,"planAmount":planAmount,"planCurrency":planCurrency,"planinterval":planinterval,"PlanName":PlanName,"planIntervalCount":planIntervalCount,"created":created,"current_period_start":current_period_start,"current_period_end":current_period_end,"status":status}

		# {"created":created,"current_period_start":current_period_start,"current_period_end":current_period_end,"status":status}

		
		  
		# Writing to sample.json 
		with open("./static/subscriptionData.json", "w") as outfile: 
		    outfile.write(json_object) 
		    

		return render_template('thanks.html',charge=JsonData)

	return render_template('index.html')
	



if __name__ == '__main__':
	app.run(debug=True)



