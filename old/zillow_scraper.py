#!/usr/bin/env python3

from lxml import html
import requests
import unicodecsv as csv
import argparse

def parse(zipcode, pricemin, pricemax, hometype):
  url = joinurl(zipcode, pricemin, pricemax, hometype)
  url = 'https://www.zillow.com/homes/for_rent/San-Mateo-CA-94404/apartment_duplex_type/97704_rid/495085-742628_price/2000-3000_mp/37.583561,-122.225218,37.525519,-122.314396_rect/13_zm/'
  filter = 'newest'
  if filter=="newest":
    url = "https://www.zillow.com/homes/for_sale/{0}/0_singlestory/days_sort".format(zipcode)
  elif filter == "cheapest":
    url = "https://www.zillow.com/homes/for_sale/{0}/0_singlestory/pricea_sort/".format(zipcode)
  else:
    url = "https://www.zillow.com/homes/for_sale/{0}_rb/?fromHomePage=true&shouldFireSellPageImplicitClaimGA=false&fromHomePageTab=buy".format(zipcode)

  print("Fetching: " + url)
  for i in range(5):
    # try:
    headers= {
          'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'accept-encoding':'gzip, deflate, sdch, br',
          'accept-language':'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
          'cache-control':'max-age=0',
          'upgrade-insecure-requests':'1',
          'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    print(response.status_code)
    parser = html.fromstring(response.text)
    print(response.text)
    search_results = parser.xpath("//div[@id='search-results']//article")
    properties_list = []

    for properties in search_results:
      raw_address = properties.xpath(".//span[@itemprop='address']//span[@itemprop='streetAddress']//text()")
      raw_city = properties.xpath(".//span[@itemprop='address']//span[@itemprop='addressLocality']//text()")
      raw_state= properties.xpath(".//span[@itemprop='address']//span[@itemprop='addressRegion']//text()")
      raw_postal_code= properties.xpath(".//span[@itemprop='address']//span[@itemprop='postalCode']//text()")
      raw_price = properties.xpath(".//span[@class='zsg-photo-card-price']//text()")
      raw_info = properties.xpath(".//span[@class='zsg-photo-card-info']//text()")
      raw_broker_name = properties.xpath(".//span[@class='zsg-photo-card-broker-name']//text()")
      url = properties.xpath(".//a[contains(@class,'overlay-link')]/@href")
      raw_title = properties.xpath(".//h4//text()")

      address = ' '.join(' '.join(raw_address).split()) if raw_address else None
      city = ''.join(raw_city).strip() if raw_city else None
      state = ''.join(raw_state).strip() if raw_state else None
      postal_code = ''.join(raw_postal_code).strip() if raw_postal_code else None
      price = ''.join(raw_price).strip() if raw_price else None
      info = ' '.join(' '.join(raw_info).split()).replace(u"\xb7",',')
      broker = ''.join(raw_broker_name).strip() if raw_broker_name else None
      title = ''.join(raw_title) if raw_title else None
      property_url = "https://www.zillow.com"+url[0] if url else None
      is_forsale = properties.xpath('.//span[@class="zsg-icon-for-sale"]')
      properties = {
              'address':address,
              'city':city,
              'state':state,
              'postal_code':postal_code,
              'price':price,
              'facts and features':info,
              'real estate provider':broker,
              'url':property_url,
              'title':title
      }
      if is_forsale:
        properties_list.append(properties)
    return properties_list
    # except:
    #   print ("Failed to process the page",url)

def joinurl(zipcode, pricemin, pricemax, hometype):
  hometype = str(hometype)
  hometype = hometype.replace('apartment', 'apartment_duplex_type')
  hometype = hometype.replace('house', 'house,mobile,land_type')
  hometype = hometype.replace('condo', 'condo_type')
  hometype = hometype.replace('townhome', 'townhouse_type')
  return('https://www.zillow.com/homes/for_rent/'
          + zipcode
          + '/'
          + hometype
          + '/'
          + str(pricemin)
          + '-'
          + str(pricemax)
          + '_mp')


if __name__=="__main__":
  argparser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
  argparser.add_argument('zipcode', help = "zipcode you're interested in finding a home")
  argparser.add_argument('pricemin', help = 'minimum price')
  argparser.add_argument('pricemax', help = 'maximum price')
  hometype_help = """
    Comma separated list of types you're interested in
    Types of homes are:
    apartment
    house
    condo
    townhome
    """
  argparser.add_argument('hometype', help = hometype_help, default = 'apartment')
  #argparser.add_argument('hometype', nargs='*', help = hometype_help, default ='apartment')
  args = argparser.parse_args()
  zipcode = args.zipcode
  pricemin = args.pricemin
  pricemax = args.pricemax
  hometype = args.hometype
  print ("Fetching data for %s"%(zipcode))
  scraped_data = parse(zipcode, pricemin, pricemax, hometype )
  print ("Writing data to output file")
  with open("properties-%s.csv"%(zipcode), 'wb')as csvfile:
    fieldnames = ['title','address','city','state','postal_code','price','facts and features','real estate provider','url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in  scraped_data:
      writer.writerow(row)
