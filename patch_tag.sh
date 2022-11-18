pushd chess-openings-helmcharts
TAG=$1
yq -i '.image.tag = strenv(TAG)' ./nginx/values.yaml
git add -A
git commit -m "change tag to ${1}"
git push https://maciejgrosz:${2}@github.com/maciejgrosz/chess-openings-helmcharts.git
popd 