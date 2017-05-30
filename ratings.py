"""Restaurant rating lister."""

def get_ratings(your_file):
    """takes restaurants, ratings from a file and adds them to a dict"""
    text_file = open(your_file)
    restaurant_ratings = {}
    #for each line in text file, remove /n and split it at the :
    for line in text_file:
        line = line.rstrip()
        restaurant, rating = line.split(':')
        #define the 1st and second items as key/value pairs and add to dict
        restaurant_ratings[restaurant] = rating

        #return restaurant_ratings

# while True:
    user_restaurant = raw_input("What's your favorite restaurant? (press q to quit) ")
    # if user_restaurant == 'q':
    #        break
    user_rating = raw_input("How do feel about it on a scale of 1-10? ")
    restaurant_ratings[user_restaurant] = user_rating


#def sort_ratings(restaurant_ratings):
   # """to sort dict into alphabetical order"""
    #sort library keys into a list
    sorted_restaurant_ratings = sorted(restaurant_ratings)  
    #for each restaurant in the list
    for restaurant in sorted_restaurant_ratings:
        #print restaurant from list
        #and value associated with the restuarant key from dict
        print "{} is rated at a {}".format(restaurant,
                restaurant_ratings[restaurant])




get_ratings('scores.txt')
#sort_ratings('restaurant_ratings')
