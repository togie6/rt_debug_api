# RT Create Ticket script

## Installation
Download a copy of the no_saml version of the repo 

```
git clone -b no_saml REPLACE_GIT_REPO.git
cd incident_report_form/
virtualenv env --python=python3
source env/bin/activate
pip install -r requirements.txt
cp _keys.py keys.py
```