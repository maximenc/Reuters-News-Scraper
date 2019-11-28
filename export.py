from datetime import datetime
from datetime import timedelta
import sys
import codecs
import argparse
import reuters
import re

def main(args):

    dstart = datetime.strptime(args.dstart, '%m-%d-%Y')
    dend = datetime.strptime(args.dend, '%m-%d-%Y')
    delta = dend - dstart
    ticker = args.ticker + ".O"

    print("TICKER: %s - FROM: %s TO: %s" % (ticker, dstart.strftime("%m-%d-%Y"), dend.strftime("%m-%d-%Y")))

    proxy = args.proxy

    if proxy != None and re.match(r'https://', proxy):
        proxy = {'https': proxy}
        print(proxy)
    elif proxy != None and re.match(r'http://', proxy):
        proxy = {'http': proxy}
        print(proxy)
    else:
        proxy = None
        print("Proxy not set")

    output_file = "%s_%s.csv" % (args.ticker, args.dstart)
    print("Saving to: \"%s\"" % output_file)
    output = codecs.open(output_file, "w+", "utf-8")
    output.write('\"date\",\"title\",\"url\",\"description\",\"text\"')

    for i in range(0,delta.days):

        date = dstart + timedelta(days=1) * i
        
        url = "https://www.reuters.com/finance/stocks/company-news/%s?date=%s" % (ticker, date.strftime("%m%d%Y"))
        list_ = reuters.scraper.scrape(url, proxy)

        print("Total articles: ", reuters.Article.artcl_count)

        for artcl in list_:
            artcl.title, artcl.link, artcl.descrp, artcl.text
            output.write(('\n\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"' % (date.strftime("%m-%d-%Y"), artcl.title, artcl.link, artcl.descrp, artcl.text) ))
    
            output.flush()
    output.close()

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--ticker", type=str, help="Company ticker \n ex: AAPL, FB, AMZN")
    argparser.add_argument("--dstart", type=str, default="07-06-2011", help="Starting date")
    argparser.add_argument("--dend", type=str, default=datetime.now().strftime("%m-%d-%Y"), help="End date")
    argparser.add_argument("--proxy", type=str,  default=None, help="Proxy: \"http(s)://IP:port\" ")

    args = argparser.parse_args()

    main(args)

