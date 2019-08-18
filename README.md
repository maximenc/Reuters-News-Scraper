

# Reuters Company News Scraper

A python script that scrapes company news from Reuters. 
The author bears no responsibility for any misuse of the tool. (See [Reuters Terms of use](https://www.reuters.com/terms-of-use))


### Details
For a given date, Reuters returns 10 relevant news articles related to a ticker. (The ticker corresponding to a firm can be found on [NASDAQ's web site](https://www.nasdaq.com/screening/company-list.aspx)).

The script "export.py" creates a .csv file named "data/TICKERNAME_DATE.csv" which contains the following fields  

```
| date       | title                                | url                    | description            |  text                  |
*------------*--------------------------------------*------------------------*------------------------*------------------------*
| 07-06-2011 | Samsung estimates Q2 profit down ... | https://www.reuters... | SEOUL, July 7 Samsu... | * Sees Q2 op profit... |
| 07-06-2011 | Hackers expose flaw in Apple iPad... | https://www.reuters... | * They could develo... | * Criminal hackers ... |
| 07-07-2011 | RIM says adds 1 million EMEA subs... | https://www.reuters... | TORONTO BlackBerry ... | A person poses whil... |
| 07-07-2011 | Apple's app downloads race ahead,... | https://www.reuters... | NEW YORK Apple Inc ... | A woman walks past ... |
| ...        | ...                                  | ...                    | ...                    | ...                    |
```


### Requirement 

+ Python 3

+ Beautiful Soup

+ Python's "requests" library


```
    $ pip install bs4
    $ pip install requests
```

## Usage


+ Help:
```
    $ python export.py -h
```

+ Command lines must have a TICKER argument:
```
    $ python export.py --ticker "AAPL"
```

+ A date range can also be passed (MM-DD-YYYY format). The default date range is from 07-06-2011 to the current day.
```
    $ python export.py --ticker "AAPL" --dstart "07-06-2011" --dend "01-01-2012"
```

+ A proxy can be used. Format: "http(s)://IP:port". 
For an authentification: "http(s)://USERNAME:PASSWORD@IP:PORT"


```
    $ python export.py --ticker "AAPL" --proxy "http(s)://IP:PORT"


    $ python export.py --ticker "AAPL" --proxy "http(s)://USERNAME:PASSWORD@IP:PORT"
```