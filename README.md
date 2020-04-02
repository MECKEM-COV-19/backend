# Corona Symptoms Tracker - Backend

This is the backend repository for the Corona Symptoms Tracker project `MECKEM-COV-19`. Started on the #wirvsvirus hackathon of the german federal government and continued since then.

## Getting Started

### Prerequisites

This is a python project using Django(2.1.1) + PostgreSQL.

Please install `python` 3+ and `pip` on your system as well as `docker`.


### Installing

```
pip install -r requirements.txt
```



### Run
To start the `Mongodb` database you have to run `docker-compose up`.

To start the python application start:
```
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
```

### Debug Database
The docker-compose file also includes a database viewer called Mongo Express to easily query and change the database. Go to `localhost:8081` and login.

## Deployment

Add additional notes about how to deploy this on a live system

## APIs  
url : __/database/patient-data__

_POST_:
Request:
```json
{
    "zipCode": ,
    "numberOfFlatmates": 
}
```
Result:
```json
{
    "email": "yourmail",
    "patientId": "yourid",
    "zipCode": "yourzip",
    "numberOfFlatmates":"yournumberofflatmates" 
}
```

_GET_:
Request:
```json
{
    "email": "yourmail",
    "patientId": "yourid",
    "zipCode": "yourzip",
    "numberOfFlatmates":"yournumberofflatmates" 
}
```


url : __/database/daily-data/__

_POST_:
Body:
```json
{
    "isCovidPositive": ,
    "temperature": "float",
    "hasChills": ,
    "isFeelingWeak": ,
    "hasBodyAches":,
    "generalFeeling": ('critical','critical'),('bad','bad'),('normal','normal'),('good','good'),
    "cough": ('dry','dry'),('produtive','productive'),('none','none'), 
    "hasSniff": ,
    "hasDiarrhea": ,
    "hasThroatPain": ,
    "hasHeadache": ,
    "isEasierOutOfBreath": ,
    "wasRiskzoneLastTwoWeeks": ,
    "hadContactLastTwoWeeks": ,
    "breathingPattern":('normal','normal'),('biots','biots'),('kussmaul','kussmaul'),('cheynestokes','cheynestokes'),('idontknow','idontknow')
}
```

## Built With

* [Python 3](https://www.python.org/) - The programming language used
* [Django](https://www.djangoproject.com/) - The webframework
* [PostgreSQL](https://rometools.github.io/rome/) - Database solution

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


