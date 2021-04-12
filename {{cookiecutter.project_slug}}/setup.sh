virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
{% if cookiecutter.react == "True" -%}
npm i
{%- endif %}

rm setup.sh