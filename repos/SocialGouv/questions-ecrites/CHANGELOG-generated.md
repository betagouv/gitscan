## Changelog : questions-ecrites (30 derniers jours, au 2026-06-16)

### Résumé
Cette mise à jour apporte des améliorations à l'ingestion et à la recherche des questions écrites.  Les agents de l'administration pourront désormais filtrer les attributions par identifiant de bureau et bénéficier d'une extraction plus robuste des informations des questions de l'Assemblée Nationale. Des optimisations et des corrections ont également été apportées pour améliorer la qualité des données et la maintenance du projet.

### Évolutions fonctionnelles
- Possibilité de filtrer les attributions par identifiant de bureau via l'API `get_attributions` [#39](https://github.com/SocialGouv/questions-ecrites/pull/39).
- Amélioration de l'extraction de l'objet des questions parlementaires de l'Assemblée Nationale, notamment pour les balises `<analyses><analyse>`.
- Récupération des questions individuelles (singulières) de l'Assemblée Nationale et du Sénat.

### Évolutions techniques
- Amélioration des identifiants des réponses pour une meilleure traçabilité.
- Suppression du code lié aux clusters de questions (`question_clusters`) pour simplifier le code et réduire la complexité.

### Autres changements
- Ajout d'informations sur l'utilisation de `kubectl` dans le fichier README pour faciliter le déploiement et la gestion de l'application.
- Corrections suite aux retours de `revu-bot` sur la PR [#39](https://github.com/SocialGouv/questions-ecrites/pull/39).
