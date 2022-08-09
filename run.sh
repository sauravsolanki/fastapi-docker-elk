docker-compose -f docker-compose.yml \
  -f extensions/apm-server/apm-server-compose.yml \
  -f extensions/curator/curator-compose.yml \
  -f extensions/enterprise-search/enterprise-search-compose.yml \
  -f extensions/filebeat/filebeat-compose.yml \
  -f extensions/heartbeat/heartbeat-compose.yml \
  -f extensions/logspout/logspout-compose.yml \
  -f extensions/metricbeat/metricbeat-compose.yml \
  -f webapp/webapp-compose.yml up --build -d
