#!/bin/sh

psql baltrad -U baltrad <<EOF
delete from bdb_files cascade;
EOF

\rm -f /opt/baltrad/bdb_storage/*.h5

