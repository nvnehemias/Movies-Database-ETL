from imdb import IMDb


def my_result_search(title_name: str, movie_key: str = 'long imdb title') -> str:
    """This will search for a movie title on imdb's api
    
    Input: Movie Title as a string
    Returns: Movie object from IMDB
    """
    ia = IMDb()
    return ia.search_movie(title_name)[0][movie_key]

# assert my_result_search('Glass') == 'Glass (2019)'
# assert my_result_search('Glass','long imdb title') == 'Glass (2019)'
# assert my_result_search('Glass','year') == 2019

#--------------------------------------------------------------------------------------------------------------------------------

def multi_result_search(my_list: list, our_key) -> dict:
    """
    Inputs: Take in a list of title names and for our_keys input either a list or a single search key
    Outputs: Return a dictionary of results. 
    """
    title_result_list = []
    for title in my_list:
        title_result = {}
        if not type(our_key) == list:
            title_result[our_key] = my_result_search(title, our_key)
            title_result_list.append(title_result)
        else:
            for i in our_key:
                title_result[i] = my_result_search(title, i)
            title_result_list.append(title_result)
    return title_result_list
    print(title_result_list)
#--------------------------------------------------------------------------------------------------------------------------------   
# assert multi_result_search(['Glass', "Miss Bala", "What Men Want"]) ==  {'Glass':['Glass (2019)'], 'Miss Bala': ['Miss Bala (2019)'], 'What Men Want': ['What Men Want (2019)']}
# assert multi_result_search(['Glass']) == {'Glass':['Glass (2019)']}
# assert multi_result_search(['Glass'],['year']) == {'Glass':[2019]}
# assert multi_result_search(['Glass'],['long imdb title','year']) == {'Glass':['Glass (2019)', 2019]}
# assert multi_result_search(['Glass', "Miss Bala", "What Men Want"], ['long imdb title','year']) \
#     == {'Glass':['Glass (2019)', 2019], 
#         'Miss Bala': ['Miss Bala (2019)', 2019], 
#         'What Men Want': ['What Men Want (2019)', 2019]}

#--------------------------------------------------------------------------------------------------------------------------------
def const_cleanup(const_value):
    return const_value[10:-2]

assert const_cleanup('ObjectId("5d5ed05284296f90ef798a63")') == '5d5ed05284296f90ef798a63'