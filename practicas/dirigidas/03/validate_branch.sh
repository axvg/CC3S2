branch=$(git rev-parse --abbrev-ref HEAD)

re='^(feature|hotfix)\/[A-Z]{2,5}-[0-9]+-[a-z0-9]+(-[a-z0-9]+)*$'

if [[ ! $branch =~ $re ]]; then
    echo "Nombre de rama invválido: $branch"
    echo "Formato correcto: feature/ABC-123-description"
    exit 1
fi