# backend

This is the backend for Meckem-19.

It is build on Django(2.1.1) + PostgreSQL

The run locally:

```
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate 
python manage.py runserver

```

## macOS

On macOS, make sure that `postgresql` is installed. You can install it via brew with the following command. `brew install postgresql`

## APIs  
url : __/database/patient-data__

_POST_:
Set body as :
```json
{
    "zipCode": ,
    "numberOfFlatmates": 
}
return :

```json
{
    "email": "yourmail",
    "patientId": "yourid",
    "zipCode": "yourzip",
    "numberOfFlatmates":"yournumberofflatmates" 
}
```
_GET_:

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
Set body as:

```
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

else if boolean
```
