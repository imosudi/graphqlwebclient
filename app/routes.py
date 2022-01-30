from flask import render_template,request #tedirect,url_for,
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

import asyncio

import json

from . import app

# Selecting transport with a defined url endpoint
#URL = "https://countries.trevorblades.com"
URL = "http://localhost:8091/graphql-query"

transport = AIOHTTPTransport(url=URL)


# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query


@app.route('/',methods=['GET','POST'])
def home():
    testDataColumns = ['testType', 'testmnemonics', 'testName', 'testPrice', 'testTAT]']
    currentID = "SOLOL-202110FI005"
    query = gql (
        """ 
        query{
          patientDetails (
            filters : {
              patientID : "%s"
            }
          )
          {
            edges {
              node { 
                patientID
                patientLastname
                patientFirstname
                patientDateofBirth
                ageGrade
                patientSex
                patientType
                patientCompanyname
              
              } 
            } 
          },
          laboratoryTests { 
            edges { 
              node { 
                testId
                testName
                testBottleType
                testPrice
                testmnemonics
                testTAT
                testDetails
                testType
              } 
            } 
          }
        }
        """ %(currentID)
      )
    # Execute the query on the transport
    try:
      result = client.execute(query)
    except asyncio.TimeoutError:
      return {"result": f"timeout error on {URL}"}
    #result = client.execute(query)
    if request.method=='POST':
        return render_template('index.html', result=result)
    rowList = []
    for item in result['laboratoryTests']['edges']:
        rowList.append(item['node'])
        #print(item['node'])
    #print(result)
    patient = result['patientDetails']['edges']
    current_patient = patient[-1]['node']
    return  render_template('index.html', rowList=rowList )


@app.route('/labsession',methods=['GET','POST'])
def labsession():
    testDataColumns = ['testType', 'testmnemonics', 'testName', 'testPrice', 'testTAT]']
    currentID = "SOLOL-202110FI005"
    query = gql (
        """ 
        query{
          patientDetails (
            filters : {
              patientID : "%s"
            }
          )
          {
            edges {
              node { 
                patientID
                patientLastname
                patientFirstname
                patientDateofBirth
                ageGrade
                patientSex
                patientType
                patientCompanyname
              
              } 
            } 
          },
          laboratoryTests { 
            edges { 
              node { 
                testId
                testName
                testBottleType
                testPrice
                testmnemonics
                testTAT
                testDetails
                testType
              } 
            } 
          }
        }
        """ %(currentID)
      )
    # Execute the query on the transport
    try:
      result = client.execute(query)
    except asyncio.TimeoutError:
      return {"result": f"timeout error on {URL}"}
    #result = client.execute(query)
    if request.method=='POST':
        return render_template('labsession.html', result=result)
    rowList = []
    for item in result['laboratoryTests']['edges']:
        rowList.append(item['node'])
        #print(item['node'])
    #print(result)
    patient = result['patientDetails']['edges']
    current_patient = patient[-1]['node']
    print(current_patient)
    return  render_template('labsession.html', current_patient = current_patient,  rowList=rowList )

@app.route('/patients',methods=['GET','POST'])
def patients():
    testDataColumns = ['testType', 'testmnemonics', 'testName', 'testPrice', 'testTAT]']
    query = gql (
        """ 
        query{
          patientDetails {
            edges {
              node {
                patientID
                patientSex
                patientTitle
                patientLastname
                patientFirstname
                patientDateofBirth
                ageGrade
                patientEmail
                patientPhonenumber
                patientwhatsappnumber
              }
            }
          }
        }
        """
      )
    # Execute the query on the transport
    try:
      result = client.execute(query)
    except asyncio.TimeoutError:
      return {"result": f"timeout error on {URL}"}
    #result = client.execute(query)
    if request.method=='POST':
        return render_template('patients.html', result=result)
    rowList = []
    for item in result['patientDetails']['edges']:
        rowList.append(item['node'])
        print(item['node'])
    #print(result)
    return  render_template('patients.html', rowList=rowList )

@app.route('/transactions',methods=['GET','POST'])
def transactions():
    testDataColumns = ['testType', 'testmnemonics', 'testName', 'testPrice', 'testTAT]']
    query = gql (
        """ 
        query{
  transactionDetails {
    edges {
      node {
        CurrentpatientID, barcode, fullName, regtype,  sex, billto, 
        testscheduletype,subtotal, discount, total, paymentmethod, payment,
        referenceOrchange, sessionconfirm, paymentconfirm, cashier,
        invoicetestname, invoiceprice, transactTime, phlebotomyProcessed 
        paymentupdateamount, paymentupdateby, paymentupdateTime
      }
    }
  }
}
        """
    )
    # Execute the query on the transport
    try:
      result = client.execute(query)
    except asyncio.TimeoutError:
      return {"result": f"timeout error on {URL}"}
    #result = client.execute(query)
    result_string = json.dumps(result, indent=2)
    #print(result_string )
    if request.method=='POST':
        return render_template('transactions.html', result=result)
    rowList = []
    #stringList = []
    for item in result['transactionDetails']['edges']:
        rowList.append(item['node'])
       # print(item['node'])
    '''for item in result_string: 
      stringList.append(item)
      #print(type(item))'''
          
    #print(result)
    return  render_template('transactions.html', rowList=rowList )
