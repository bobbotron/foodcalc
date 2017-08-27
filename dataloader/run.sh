#!/bin/sh

env

cat > ~/.pgpass << EOF
db:5432:fooddb:foodcalcuser:0p9o8i7U
EOF

chmod 0600 ~/.pgpass

echo "Waiting for database"
dockerize -wait tcp://db:5432
sleep 1
echo "Database online"

echo "Creating table structure"
psql -f /data/tables.sql -w -U foodcalcuser -h db fooddb

python /scripts/loaddata.py
