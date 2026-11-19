# Sites Conformes sur Scalingo

[![Déployer sur Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://dashboard.scalingo.com/create/app?source=https://github.com/incubateur-ademe/sites-conformes-scalingo#main)

Ce dépôt ne contient pas le code de [Sites Conformes](https://github.com/numerique-gouv/sites-conformes) :
au déploiement, le [buildpack Sites Conformes](https://github.com/incubateur-ademe/sites-conformes-buildpack)
télécharge la version indiquée par la variable `SITES_CONFORMES_VERSION`.

Le bouton crée l’application, sa base PostgreSQL et ses variables d’environnement.
Les images et documents sont stockés dans la base de données (`SF_USE_DB_STORAGE=True`) :
aucun service externe n’est nécessaire pour démarrer. Au-delà de 1 Go de médias
ou pour un site à fort trafic, passer sur un stockage S3 en ajoutant à l’app les
[variables `S3_*`](https://numerique-gouv.github.io/sites-conformes/deploiement/variables-environnement.html) : S3 est alors prioritaire.

Un nginx est placé devant gunicorn (`servers.conf.erb`, `bin/start`) : il sert les fichiers
statiques et garde en cache les médias stockés en base, pour ne pas lire PostgreSQL à chaque image.

## Mettre à jour

1. Changer `SITES_CONFORMES_VERSION` (ex : `4.3.1`, ou `latest` pour la dernière version publiée).
2. Relancer un déploiement depuis le tableau de bord Scalingo.

Les migrations de base de données sont jouées automatiquement après le déploiement.
Revenir à une version antérieure demande de restaurer une sauvegarde de la base.

Ces applications peuvent être tenues à jour automatiquement par
[scalingo-watcher](https://github.com/incubateur-ademe/scalingo-watcher).

## Personnaliser

Un fichier ajouté à ce dépôt remplace celui du code de Sites Conformes au même chemin.
