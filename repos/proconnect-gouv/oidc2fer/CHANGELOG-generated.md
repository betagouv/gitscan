## Changelog : oidc2fer (30 derniers jours)

### Résumé
Cette version apporte principalement des améliorations de la configuration et de la gestion des identifiants SIRET pour les établissements universitaires. Une nouvelle version (v1.0.12) a été publiée avec des mises à jour des dépendances et des corrections mineures. Des améliorations de l'environnement de développement local et de l'infrastructure ont également été apportées.

### Évolutions fonctionnelles
- Correction de l'identification SIRET pour l'université d'Angers [#38](https://github.com/proconnect-gouv/oidc2fer/pull/38).
- Ajout de nouveaux identifiants SIRET pour plusieurs entités.
- Mise à jour de l'URL des métadonnées Renater pour assurer la synchronisation avec les informations les plus récentes.

### Évolutions techniques
- Mise à jour et verrouillage des actions GitHub pour une meilleure stabilité et sécurité.
- Mise à jour de Python vers la version 3.14.3.
- Mise à jour des dépendances Python.
- Suppression de `setup.py` et migration vers `pyproject.toml`.
- Ajout d'un healthcheck à la configuration Docker Compose pour une meilleure surveillance de l'application.
- Amélioration du script de démarrage du cluster local Kind.
- Correction de la référence à l'image Bitnami Redis.
- Publication de la version v1.0.12.

### Autres changements
- Mise à jour des secrets pour refléter les dernières modifications.
- Suppression des dépendances `setuptools`, `wheel` et `pip` de l'image Docker de production.
- Renommage du fichier `helmfile.yaml` pour la compatibilité avec helmfile 1.x.
