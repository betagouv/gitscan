# Buildpack Sites Conformes

Télécharge le code de [Sites Conformes](https://github.com/numerique-gouv/sites-conformes)
dans l’application au moment du build. Le build lui-même est fait par les buildpacks apt et Python
listés après celui-ci :

```
https://github.com/incubateur-ademe/sites-conformes-buildpack.git
https://github.com/Scalingo/apt-buildpack.git
https://github.com/Scalingo/python-buildpack.git
```

Point de départ prêt à l’emploi : [sites-conformes-scalingo](https://github.com/incubateur-ademe/sites-conformes-scalingo).

| Variable | Rôle |
|---|---|
| `SITES_CONFORMES_VERSION` | Version à déployer : `4.3.1`, `v4.3.1` ou `latest` (défaut, dernière release hors pré-versions) |
| `HOST_URL`, `ALLOWED_HOSTS` | Par défaut le domaine Scalingo de l’app (`<app>.<région>.scalingo.io`). À définir une fois un nom de domaine branché |
| `GITHUB_TOKEN` | Facultatif, évite la limite de l’API GitHub quand la version vaut `latest` |
| `BUILDPACK_DEBUG` | Affiche les commandes exécutées |

Les fichiers du dépôt de l’application ne sont jamais écrasés par ceux de Sites Conformes.

Test : `./test.sh` (voir l’en-tête pour le lancer sous Docker depuis macOS).
