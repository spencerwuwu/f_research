# Finance Research   
## Installation
```
$ pip install -r requirements.txt
```
## Parser
### Amazon
#### Usage
```
$ python amazon.py "<Url>"
  *<Url> formate:
    link of the product ending with "&pageNumber=" discarding its value
    eg:
    https://www.amazon.com/Arlo-Wireless-Security-Detection-Included/product-reviews/B016LJMRCW/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=
```
Result stored in result_amazon.txt.

### Best Buy
#### Usage
```
$ python bestbuy.py "<Url>"
  *<Url> formate:
    link of the product ending with "&page=" discarding its value
    eg:
    "https://www.bestbuy.com/site/reviews/arlo-pro-2-camera-indoor-outdoor-wireless-720p-security-camera-system-white/5604500?page="
```
Result stored in result_bestbuy.txt.

