# Script to download any needed dependencies or programs
# for the admin tool to work correctly


$initPyScript   = $(python logger.py)
$filterPyScript = $(python filter.py)

echo "Starting Script.."
echo "$initPyScript"

echo "Filtering Script"
echo "$filterPyScript"
