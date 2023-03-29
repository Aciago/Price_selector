# Price Selector
 bot for scraping ammo data and finding best deals

Problem:
Huge number of online shops offer various types of .22 LR ammunition. Some give discounts on large orders, some offer free shipping, others offer low prices but no discounts. I would like to automate the process of finding best deals.
Ideally universal scraper for multitude of websites, but easier option to start with would be a best deal for each individual website and comparison afterwards.

Plan:
1) Scrape data from various sources
2) Collect data in one place, converting into a complete price breakdown (ammo itself, shipping, discounts, etc).
3) Return a result in a form of specific offer to buy from (shop, link, ammo, price, etc)

ideas to implement:
- total cost column (price + delivery)
- cost per round\shot (divide total cost by number of rounds in a box)
- try to get proper name of Manufacturer AND product name (e.g. CCi Standard Velocity or CCi Blazer)
