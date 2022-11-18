kubectl patch --local -f ./nginx/values.yaml -p '{"image":{"tag":"${1}"' -o yaml
pushd chess-openings-helmcharts
git add -A
git commit -m "change tag to ${1}"
git push https://maciejgrosz:${2}@github.com/maciejgrosz/chess-openings-helmcharts.git
popd 