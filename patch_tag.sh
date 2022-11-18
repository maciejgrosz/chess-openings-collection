pushd chess-openings-helmcharts
yq -i ".image.tag = ${1}" ./nginx/values.yaml
git add -A
git commit -m "change tag to ${1}"
git push https://maciejgrosz:${2}@github.com/maciejgrosz/chess-openings-helmcharts.git
popd 