# CSV to Trello
> Import tasks stored in CSV to Trello

Import tasks in CSV format (export from Jira, Asana) to Trello. Well documented script for custom migrations. 

## Installation

OS X & Linux & Windows:

```sh
pip install -r requirements.txt
```

## Usage example

First you need to obtain Trello credentials. Go to https://trello.com/app-key. 
Copy **key** and swap with *API_KEY* placeholder in script. 
Next click **token** link below and generate OAuth token. Swap with **TOKEN** placeholder in script.


Setup Trello board. Add desired columns and labels. Find Trello board id in URL. 
For example: *https://trello.com/b/7x0OkEEI/test* then your board ID is *7x0OkEEI*
Swap with **BOARD_ID** placeholder in script.

Setup columns to list mapping. You need to obtain list ids and map in code to your desired columns. 
*TODO: Implement mapping with dict*

Labels mapping works the same way as columns. It depends on use case

Run script
```sh
python import.py
```

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.0.1
    * WIP. Working import with column mapping and labels

## Meta

Piotr Pilis – piotr@piotr.pl

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/yourname/pilis](https://github.com/pilis/)

## Contributing

1. Fork it (<https://github.com/pilis/csv-to-trello/fork)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request