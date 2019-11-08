## Introduction

We currently have two web service versions to allow individuals and institutions to interact with the HIVDB drug resistance interpretation program through an API:

### Sierra Web Service 2: 2016 – present

Sierra Web Service 2 is a [GraphQL](http://graphql.org/)\-based web service which outputs JSON results. This page summarizes how to use this web service. It is preferable to version 1.1 because it is actively maintained. It is also easier to begin using and to customize. For now users do not need to register for this web service. Users can write a software client in any language that provides web service libraries. We currently have one client library in Python and will be creating additional ones in Java and Perl in the future.

### Sierra Web Service 1.0/1.1: 2005 – 2017

[Sierra Web Service 1.1](/page/webservice-1.1/) is a SOAP web service which outputs XML results. Users must register with us to obtain a key which they then submit with their sequence requests. Users also require a software client which wraps the connection to the server running the web service and software to parse the XML output. Users can write a software client in any language that provides web service libraries. However, we have provided two client libraries in Java and Perl.

## Migration from 1.0/1.1 to 2

The new Sierra Web Service 2 is actively maintained, comes with more flexibility and provides more analysis details than Sierra Web Service 1.0/1.1. To encourage and help 1.0/1.1 users to migrate to 2, we provide this API comparison spreadsheet ([download]($$CMS_PREFIX$$downloads/webservice/comparison-v1-and-v2.xlsx)) which documented all corresponding data paths between 1.0/1.1 and 2.

## Usage

With the powerful query language GraphQL, Sierra Web Service 2 allows users/clients to obtain data and customize data schema to exactly what they need. It is easy to make requests to a GraphQL server and there are [plenty of GraphQL client libraries in many languages](//github.com/chentsulin/awesome-graphql#libraries). To assist users, we have already provided one client library written in Python. Additionally, if you would like to create your own data schema (i.e., one that differs from the default all-encompassing schema), we have set up an in-browser Editor that helps you to create variations on the default schema.

### Python Client

SierraPy, the Python client provides a handy command line tool that allows users to obtain analysis reports for sequences or mutations. Default data schemas are shipped with this client and are accessible at [GitHub](//github.com/hivdb/sierra-client/tree/master/python/sierrapy/fragments). SierraPy also contains a SierraClient class for Python developers.

Your computer must have [Python (2.7, 3.5 or 3.6)](//www.python.org/) and the package management tool [pip](//github.com/pypa/get-pip) installed. Once you get the prerequisites installed, just type this command to install SierraPy:

[](!gist:philiptzou/da49a5ccedb168944a22d6e63221a508)

Please visit [SierraPy’s readme page](//github.com/hivdb/sierra-client/tree/master/python) for the usage of command line tool.

### In-Browser Editor

This editor utilizes [GraphiQL](//github.com/graphql/graphiql), an in-browser IDE for GraphQL, which provides an interactive interface for users to view our API and then customize their data schema. Here are two example queries for users to get started:

1.  [**Example for sequence analysis**](/page/graphiql/?example=sequenceAnalysis). This example accepts several sequences as the input and returns the sequence alignments, quality assessments, pretty pairwise alignments, and drug resistance interpretations from the web service.
2.  [**Example for mutations analysis**](/page/graphiql/?example=mutationsAnalysis). This example accepts several mutations as the input and returns the quality assessments and drug resistance interpretations from the web service.

### Minimal Working Examples

#### JavaScript (ECMAScript 6)
[](!gist:philiptzou/93019da458c429b3a13513ba9b79407c)

#### Python with SierraPy Client
[](!gist:philiptzou/c76a5bd7a669391594103cc8013c7b5d)

#### Python with Requests
[](!gist:philiptzou/e97dc111c85c35c2db8aab957f7cb03b)

## Logging and Privacy Policy

Our policy is based on the [NLM's policy](//www.nlm.nih.gov/privacy.html).

Stanford HIV Resistance Database provides web services and related pages as a public service to educational institutions. We do not collect personal information about you when you visit our sites unless you choose to provide that information to us.

### Information Collected and Stored Automatically

Of the information we learn about you from your visit to our sites or access our services, we store only the following: the IP address from which you access the Internet, the date and time, the Internet address of the website from which you linked directly to our site, and the browser or client used to access our server. This information is used to measure the number of visitors to the various sections of our site and identify system performance or problem areas. We also use this information to help us expand the coverage of the sites and to make the site more useful. Stanford HIV Resistance Database periodically deletes its web logs.

### Personally Provided Information

If you choose to provide us with personal information by sending an email, or by filling out a form with your personal information and submitting it through our website, we use that information to respond to your message and to help us provide you with information or material that you request. The personal information provided will be kept confidential and will not be made available to third parties.
