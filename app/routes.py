from flask import render_template,request #tedirect,url_for,
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


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
    query = gql (
        """ 
        query{
  allLabtests {
    edges {
      node {
        testType
        testmnemonics
        testName
        testPrice
        testTAT
      }
    }
  }
}
        """
    )
    # Execute the query on the transport
    result = client.execute(query)
    if request.method=='POST':
        return render_template('index.html', result=result)
    rowList = []
    for item in result['allLabtests']['edges']:
        rowList.append(item['node'])
        print(item['node'])
    #print(result)
    return  render_template('index.html', rowList=rowList )


@app.route('/labsession',methods=['GET','POST'])
def labsession():
    testDataColumns = ['testType', 'testmnemonics', 'testName', 'testPrice', 'testTAT]']
    query = gql (
        """ 
        query{
  allLabtests {
    edges {
      node {
        testType
        testmnemonics
        testName
        testPrice
        testTAT
      }
    }
  }
}
        """
    )
    # Execute the query on the transport
    result = client.execute(query)
    if request.method=='POST':
        return render_template('labsession.html', result=result)
    rowList = []
    for item in result['allLabtests']['edges']:
        rowList.append(item['node'])
        print(item['node'])
    #print(result)
    return  render_template('labsession.html', rowList=rowList )

@app.route('/patients',methods=['GET','POST'])
def patients():
    testDataColumns = ['testType', 'testmnemonics', 'testName', 'testPrice', 'testTAT]']
    query = gql (
        """ 
        query{
  allPatients {
    edges {
      node {
        patientID,patientSex, patientType,patientPhonenumber
        patientTitle, patientLastname, patientFirstname,
        ageGrade, patientpersonalEnroledby
      }
    }
  }
}
        """
    )
    # Execute the query on the transport
    result = client.execute(query)
    if request.method=='POST':
        return render_template('patients.html', result=result)
    rowList = []
    for item in result['allPatients']['edges']:
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
  allTransactions {
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
    result = client.execute(query)
    if request.method=='POST':
        return render_template('transactions.html', result=result)
    rowList = []
    for item in result['allTransactions']['edges']:
        rowList.append(item['node'])
        print(item['node'])
    #print(result)
    return  render_template('transactions.html', rowList=rowList )
