## Changelog : fabnum-cicd (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la standardisation de la construction des images Docker via l'adoption des normes OCI et sur l'amélioration de la fiabilité des workflows. Plusieurs corrections ont été apportées pour stabiliser les processus de scan de sécurité et de nettoyage des images.

### Évolutions fonctionnelles
- **build-docker** : Ajout de labels et d'annotations OCI standards, avec la possibilité pour l'utilisateur de les désactiver.
- **build-docker** : Le tag `TAG_SHORT_SHA` est désormais optionnel et désactivé par défaut.
- **update-helm-chart** : En mode local, le push s'effectue désormais avec l'application configurée.

### Évolutions techniques
- **scan-gitleaks** : Correction pour limiter le périmètre du scan à la référence (ref) actuellement extraite.
- **clean-images** : Le workflow ne s'interrompt plus si la suppression de la dernière version taguée d'un package échoue.
- **workflows** : Suppression du filtre de branche dans les liens pointant vers l'onglet de sécurité.
- **tests** : Amélioration de l'exécution des blocs de code extraits en utilisant directement le shell du runner.
- **actionlint** : Mise à jour de la configuration pour autoriser les labels `ubuntu-26.04`.

### Autres changements
- Documentation de la protection de la dernière version taguée dans le workflow `clean-images`.
- Documentation de l'entrée `TAG_SHORT_SHA` pour le workflow `build-docker`.
