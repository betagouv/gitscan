## Changelog : qualicharge (30 derniers jours, au 24 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'ouverture des données avec l'exportation des tarifs vers les services OpenData et sur l'amélioration de la précision des indicateurs de performance. La sécurité et la stabilité des processus automatisés ont également été renforcées.

### Évolutions fonctionnelles
- Exportation des tarifs vers le service OpenData via l'outil data7.
- Correction du calcul des indicateurs e2, e3 et e6 pour assurer la précision des résultats même en présence de statuts manquants.

### Évolutions techniques
- Renforcement de la sécurité par la correction de vulnérabilités liées à des dépendances transitives.
- Amélioration de la fiabilité des workflows GitHub Actions concernant l'amorçage (seeding) de la base de données pour Prefect.
- Mise à jour de la version de l'API vers la 0.35.1.
