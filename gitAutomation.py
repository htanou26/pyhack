from github import Github

# Remplacez ces valeurs par vos propres informations d'authentification GitHub
username = 'votre_nom_utilisateur'
password = 'votre_mot_de_passe_ou_token'

# Initialisez l'objet Github
g = Github(username, password)

# Remplacez 'nom_du_repositoire' par le nom de votre référentiel
repository_name = 'nom_du_repositoire'

# Créez un nouveau référentiel
user = g.get_user()
repo = user.create_repo(repository_name)

# Créez un fichier README.md
content = "Bonjour, c'est un exemple de fichier README créé automatiquement."
repo.create_file("README.md", "Initial commit", content)

# Créez une demande de tirage (pull request)
branch = repo.get_branch("main")
new_branch = repo.create_git_ref("refs/heads/feature-branch", branch.commit.sha)
repo.create_pull(
    title="Ajouter une fonctionnalité",
    body="Voici une nouvelle fonctionnalité que j'ajoute au référentiel.",
    base="main",
    head="feature-branch"
)

# Fusionnez la demande de tirage
pull_request = repo.get_pulls(base="main")[0]
pull_request.merge()

print("Opérations GitHub automatisées avec succès!")
