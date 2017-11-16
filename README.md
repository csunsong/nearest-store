
Geodistance search based on haversine great-cirle formula, adapted from: https://gist.github.com/rochacbruno/2883505. 

Program accepts inputs as either address or zip code, which is converted to geo coordinates used to calculate distance and search for the nearest address in a list of stores. 

The search implementation itself uses a greedy style algorithm, which starts at the max distance (global radius), and retains the lesser value at each iteration in the `closest_distance` variable. 

 #### Instructions to run: ####
* Requires use of Python 3.x 
* cd into directory
* From within a virtualenv, install the requirements: 
`pip install -r requirements.txt`

* Example usage: 
`python main.py --address="1770 Union St, San Francisco, CA 94123"` 

* Search by zip: 
`python main.py --zip=94115` 

* Search by km: 
` python main.py --address="1770 Union St, San Francisco, CA 94123" --units=km`

* With JSON output: 
`python main.py --address="1770 Union St, San Francisco, CA 94123" --output=json` 

* Run tests: `python tests.py`
