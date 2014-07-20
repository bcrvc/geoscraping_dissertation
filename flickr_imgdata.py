#################################################################
# this code can be used for getting the image metadata          #
# from FLickr via their API - image search can be modified      #
# following this API method:                                    #
# https://www.flickr.com/services/api/flickr.photos.search.html #
# Using the flikckrapi Python module:                           #
# http://stuvel.eu/flickrapi                                    #
#################################################################

# prints xml data format: 

import flickrapi
import xml

api_key='********************************'
api_secret ='****************'
             
flickr = flickrapi.FlickrAPI(api_key,secret=api_secret)
r = flickr.photos_search(tags='*******', has_geo="1", extras='geo, license, date_upload, path_alias, url_n', per_page='250', page='**')
xml.etree.ElementTree.dump(r)

## or in json data format: 

# import flickrapi
# import json

# api_key='********************************'
# api_secret ='****************'
             
# flickr = flickrapi.FlickrAPI(api_key,secret=api_secret)
# r = flickr.photos_search(tags='*******', has_geo="1", extras='geo, license, date_upload, path_alias, url_n', per_page='250', page='**')
# print r
