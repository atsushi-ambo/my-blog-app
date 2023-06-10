#!/bin/sh
# wait-for.sh

set -e

host="$1"
shift
cmd="$@"

until PING=`mysqladmin ping -h"$host"` && echo "$PING" | grep "mysqld is alive" > /dev/null; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"
exec $cmd
