# install dependencies
pip install -r build.sh


python manage.py collectstatic --no-input
#run migration
python manage.py migrate


