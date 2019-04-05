classification project - Nicole Garza and Steven Garis

Link to google slides - https://docs.google.com/presentation/d/10syzCnT3vCkFuxtQEs9QZUAqrF9AITtrn2VJ1P38cxE/edit?usp=sharing

Data Dictionary: 
house_hold_type_id: the combination of partner and dependents.
    partner=yes, dependents=yes: 3
    partner=yes, dependents=no: 2
    partner=no, dependents=no: 0
    partner=no, dependents=yes: 1

streaming_services: the combination of streaming_tv and streaming_movies.
    streaming_tv=yes, streaming_movies=yes: 3
    streaming_tv=yes, streaming_movies=no: 2
    streaming_tv=no, streaming_movies=yes: 1
    streaming_tv=no, streaming_movies=no: 0

tenure_year: tenure divided by 12

churn: 
    no= 0
    yes= 1

phone_info: the combination of phone_service and multiple_lines.
    phone_service= Yes multiple_lines= Yes: 2
    'phone_service= No multiple_lines = No: 0
    phone_service= Yes multiple_lines= No: 1

online_security_backup: the combination of online_security and online_backup.
    internet service= no, internet service= no: 0
    online_security= no, online_backup= no: 1
    online_security= no, online_backup= yes: 2
    online_security= Yes, online_backup= No: 3
    online_security= Yes, online_backup= Yes: 4

instructions on using python script:
    import these files:
        -prep
        -acquire
        -env

    call the get_telco_function from the acquire.py file and assign it to a variable: 
        df = acquire.get_telco_data()

    use the prep_telco function from the prep.py file to prepare the data and reassign it to the original variable:
        df = prep.prep_telco(df)
