classification project - Nicole Garza and Steven Garis<br />

Link to google slides - https://docs.google.com/presentation/d/10syzCnT3vCkFuxtQEs9QZUAqrF9AITtrn2VJ1P38cxE/edit?usp=sharing<br />

Data Dictionary: 
house_hold_type_id: the combination of partner and dependents: <br />
    partner=yes, dependents=yes: 3<br />
    partner=yes, dependents=no: 2<br />
    partner=no, dependents=no: 0<br />
    partner=no, dependents=yes: 1<br />

streaming_services: the combination of streaming_tv and streaming_movies:<br />
    streaming_tv=yes, streaming_movies=yes: 3<br />
    streaming_tv=yes, streaming_movies=no: 2<br />
    streaming_tv=no, streaming_movies=yes: 1<br />
    streaming_tv=no, streaming_movies=no: 0<br />

tenure_year: <br />
    tenure divided by 12<br />

churn: <br />
    no= 0<br />
    yes= 1<br />

phone_info: the combination of phone_service and multiple_lines:<br />
    phone_service= Yes multiple_lines= Yes: 2<br />
    'phone_service= No multiple_lines = No: 0<br />
    phone_service= Yes multiple_lines= No: 1<br />

online_security_backup: the combination of online_security and online_backup<br />
    internet service= no, internet service= no: 0<br />
    online_security= no, online_backup= no: 1<br />
    online_security= no, online_backup= yes: 2<br />
    online_security= Yes, online_backup= No: 3<br />
    online_security= Yes, online_backup= Yes: 4<br />

instructions on using python script:<br />
    import these files:<br />
        -prep<br />
        -acquire<br />
        -env<br />

    call the get_telco_function from the acquire.py file and assign it to a variable:
        df = acquire.get_telco_data()

    use the prep_telco function from the prep.py file to prepare the data and reassign it to the original variable:
        df = prep.prep_telco(df)
