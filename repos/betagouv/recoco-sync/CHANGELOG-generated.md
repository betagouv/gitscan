## Changelog : recoco-sync (30 derniers jours, au 16 septembre 2026)

### Résumé
Les récentes évolutions se sont concentrées sur le renforcement de la sécurité et de la confidentialité des données, ainsi que sur l'amélioration de la fiabilité du traitement des tâches en arrière-plan.

### Évolutions techniques
- **Gestion des tâches** : Optimisation de la gestion des tâches asynchrones via l'utilisation de Celery.
- **Sécurité et Authentification** : 
    - Renforcement de la sécurité de l'authentification en sécurisant les horodatages (timestamps) pour empêcher leur réutilisation.
    - Amélioration de la configuration de sécurité concernant les hôtes autorisés (`ALLOWED_HOSTS`).
- **Confidentialité** : Protection des données personnelles en empêchant leur transmission vers l'outil de suivi d'erreurs Sentry.

### Autres changements
- **Base de données** : Amélioration de la clarté des migrations en ajoutant des descriptions manquantes.
