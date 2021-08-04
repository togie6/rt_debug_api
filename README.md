# RT debug api
Used for a basic interactions with the RT API.

## Installation
```sh
git clone https://github.com/togie6/rt_debug_api.git
cd rt_debug_api/
virtualenv env --python=python3
source env/bin/activate
pip install -r requirements.txt
cp _keys.py keys.py 

# Fill in keys.py with your rt server details including user/pass
```

## create_ticket
Creates a basic ticket with dummy text data.

```sh
./createticket.py  --queue "Triage" --subject "Test Ticket" --requestor "user@/dev/null.com"
```