# x_scrapy
A scrapy for twitter. NOTE THAT X: The Individual API no longer provides access to follow-lookup endpoints.
And there are time and quantity limitations on the tweet-lookup endpoints.
There is the idea of using a personal crawler to get data.

# Prerequisites
* Twitter API Essential Access ([sign up here](https://t.co/signup))
* A Project and an App created [in the dashboard](https://developer.twitter.com/en/portal/dashboard)
* the package requirements to see the file: x_scrapy/requirements.txt
```bash
pip install -r requirements.txt
```

# dictionary
## data
Contains data that is used in both data acquisition methods and data analysis methods.
## source
The code of the method implementation.
### data_analysis
Code related to data analysis. And the result graph of the data analysis is included in the subdirectory
### data_collect_by_api
Use the official API provided by X to collect data.
