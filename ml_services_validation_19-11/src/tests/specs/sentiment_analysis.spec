# Sentiment Analysis
Tags: ml

This test case handles the verification and validation of the model behind the Sentiment Analysis that is part of the 
service that we're developing and deploying.

## Endpoint Verification
Tags: functional, verification

Verify if the endpoint that allows interaction with Sentiment Analyzer is properly defined based on specifications. It 
must provide a query parameter **text** that acts as the input of the model and it cannot be empty. The response must 
be a JSON containing three attributes: **text**, **score** and **sentiment**.

* Request sentiment analysis with text "Perdy is testing this" returns "200"
* Response schema contains attributes
    |Attribute|
    |---------|
    |text     |
    |score    |
    |sentiment|
* Request sentiment analysis with text "" returns "400"


## Model Validation
Tags: ml, validation

Validate the model predictions against a set of fixed data. This data set must contains a minimum list of well-known 
pairs of input and output to check that after retraining the model it will continue behaving the same way against these 
inputs.

* Analyze and validate the following texts <table:data/sentiment_analysis.csv>

