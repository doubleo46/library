Data migration from postgres to elastic

data is transffered live from postgres to elastic using kafka and related connectors.
Connectors are implemented using docker from lenses.io
https://lenses.io/downloads/lenses-download-ok/

wal2json along with postgres replication is required for this entire pipeline to work.
.so file for postgres 9.6
