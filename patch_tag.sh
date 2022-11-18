pushd chess-openings-helmcharts
IM_TAG=$1
yq -i '.image.tag = strenv(IM_TAG)' ./nginx/values.yaml
yq -i '.image.tag = strenv(IM_TAG)' ./nginx/charts/chess/values.yaml
git add -A
git commit -m "change tag to ${1}"
git push https://maciejgrosz:${2}@github.com/maciejgrosz/chess-openings-helmcharts.git
popd 