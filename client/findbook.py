import sys, amazon

# Display author's name nicely.
def prettyName(arg):
    if type(arg) in (list, tuple):
        arg = ', '.join(arg[:-1]) + ' and ' + arg[-1]
    return arg

if __name__ == '__main__':

    # Get information.
    key, asin = sys.argv[1], sys.argv[2]
    amazon.setLicense(key)
    items = amazon.searchByASIN(asin)

    # Display information.
    for item in items:
        productName = item.ProductName
        ourPrice = item.OurPrice
        authors = prettyName(item.Authors.Author)
        print '%s: %s (%s)' % (authors, productName, ourPrice)
