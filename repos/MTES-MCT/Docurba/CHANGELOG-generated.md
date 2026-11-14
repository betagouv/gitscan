## Changelog : Docurba (30 derniers jours, au 13 novembre 2026)

### Résumé
Cette période a été marquée par une refonte majeure de l'interface dédiée aux autorités territoriales et une amélioration significative de la gestion des procédures d'urbanisme. Les utilisateurs bénéficient désormais d'une meilleure visibilité sur les données (nouveaux types de documents, commentaires de dépôt) et d'une navigation plus fluide. En parallèle, la fiabilité du système a été renforcée par l'automatisation de contrôles de cohérence des données.

### Évolutions fonctionnelles
- **Refonte des autorités territoriales** : Design repensé des pages de détails, redirection automatique des anciennes pages vers la nouvelle structure, et intégration de GeoRisques comme vue par défaut.
- **Amélioration de la gestion des procédures** : 
    - Affichage des commentaires de dépôt et des détails des noms de procédures dans les tableaux.
    - Introduction de nouveaux types de documents pour mieux refléter les possibilités métier.
    - Meilleure gestion des filtres (notamment pour le PLUI) et affichage des informations relatives à la loi Huwart.
- **Gestion des droits et sécurité** : Ajout de droits spécifiques pour les administrateurs PAC et renforcement de l'authentification pour les procédures partageables.
- **Optimisation de la recherche** : Amélioration des requêtes sur les collectivités via la distinction entre les codes INSEE et SIREN.

### Évolutions techniques
- **Fiabilisation des données** : 
    - Mise en place de contrôles de cohérence sur les champs dénormalisés des procédures avec notification automatique sur Slack en cas d'anomalie.
    - Transition vers des types de documents dynamiques pour plus de flexibilité.
- **Optimisation Backend & API** : 
    - Migration des appels de données des collectivités vers Django pour une meilleure centralisation.
    - Création de nouveaux endpoints API pour le calcul dynamique des noms de procédures.
    - Amélioration des performances via la mise en cache de certains périmètres de procédures.
- **Infrastructure et CI/CD** : 
    - Optimisation du cycle de vie des "Review Apps" (planification de la désactivation nocturne et correction du processus de création/suppression).
    - Mise à jour de la configuration Scalingo.
- **Qualité du code** : 
    - Refactorisation des appels API dans Nuxt via l'utilisation de plugins.
    - Mise en conformité du code avec les standards de linting (Ruff).

### Autres changements
- Documentation de scripts internes et nettoyage des commandes de gestion (management commands) obsolètes.
