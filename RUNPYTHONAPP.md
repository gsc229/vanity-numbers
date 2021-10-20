#### Other Pages:
- [Overview](README.md)
- [CloudFormation Instructions](CLOUDFORMATION.md)
- [Contact Flow Instructions](CONTACTFLOW.md)
- [Managing The Project (Trello Board)](https://trello.com/b/MtaGkEdG/voicefoundry-code-challenge)
- [Blockers (Trello Board)](https://trello.com/b/MtaGkEdG/voicefoundry-code-challenge)

### On this Page:

- [Pipenv](#pipenv-environment-manager)
- [Environment](#setting-environemt-variables)
- [Running Tests](#testing-the-application)
- [Approach](#approach)



## Running the Python Application Locally
#### Pipenv Environment Manager
**<span style="font-size:.8rem">To skip this step see:</span>**    [setting environment variables](#setting-environemt-variables)

[Pipenv Documentation](https://pipenv.pypa.io/en/latest/install/)
You can use pip to install Pipenv
[Install Instructions](https://pypi.org/project/pipenv/)
```
$ pip install --user pipenv
```
After install run:
```
$ pipenv shell
```
When shell is running, from the same terminal run:
```
$ pipenv install
```
 This will install all the dependencies in the Pipfile
 You can now use all the normal python commands from inside the pipenv shell (The only depencies needed are the one's to run data generators, which isn't need because number_map has already been created.)

## Setting Environemt Variables

Since my friends and family probably wouldn't appreciate me pushing their phone numbers to GitHub, I made the following environment variables:
```
TEST_NUMBER_1
TEST_NUMBER_2
TEST_NUMBER_3
TEST_NUMBER_4
TEST_NUMBER_5
```
You can set those same variables in a .env file in the root. 

***If you want to skip setting up Pipenv***, you can hard code your own phone number variables in the test_phone_numbers list in time_test.py.

Valid phone number strings take the form 1-555-555-5555, +15555555555. As long as they have 11 numbers total and 1 as the country code they will pass validation.

## Testing The Application

There are a number of tests you can run inthe pipenv shell:
```
$ python time_test.py
```
```
$ python test_find_vanity_numbers.py
```
```
$ python test_get_response_message.py
```
```
$ python test_validate_phone.py
```
```
$ python test_word_groups.py
```

## Approach

Rather than writing an algorithm that randomly generates letters associated with digits on a phone dial pad, I decided to use a list of common words. I wrote a function, fetch_word_list.py (vanitynumbers/data) which queries [Words API](https://www.wordsapi.com/#). 

I used the following query:

```
querystring = {"letterPattern":"^[a-zA-Z]+$", "lettersmin":"2", "lettersMax":"7", "limit":"56000"}
```

A list of words with only alpha characters that were between 2 and 7 letters long yeilded roughly 56,000 words. I wrote a funcion, generate_number_map.py, that encoded each word into their dial-pad digit representations and saved them in a python dictionary, number_map.py. The number-strings (varying in lenght of 2-7 numbers) served as the keys and a list of all the words that could be made from the same number sequence served as the value. Having the number map saved in memory as a dicitonary gave me quick access to the values (O(1)).

```
"7237842": ["SCEPTIC"]
```

```
"22766": ["AARON", "ACRON", "BARON", "BASON", "CAPON", "CAROM"],
```
```
"224": ["AAH", "BAG", "BAH", "BAI", "BCH", "CBI"]
```
In find_vanity_numbers.py, I broke the phone number down to number-strings and found matches to words between 2 and 7 letters long. I ranked all the vanity number results by longest word (they were already ordered alphabetically) and returned the top five. 


