## Changelog : Docurba (30 derniers jours, au 19 novembre 2026)

### Résumé
Ce mois a été marqué par une refonte importante de l'interface de gestion des autorités territoriales et une amélioration significative de la fiabilité des données. L'expérience utilisateur a été enrichie par de nouveaux outils de filtrage et de sélection, tandis que l'administration du système a été renforcée pour offrir un meilleur contrôle sur les dossiers et les utilisateurs.

### Évolutions fonctionnelles
- **Refonte de l'interface des autorités territoriales** : Redesign complet des pages de détails et des sous-pages, avec une vue par défaut personnalisée selon le profil de l'utilisateur.
- **Amélioration de la gestion des procédures** :
    - Affichage des commentaires de dépôt et des détails des noms de procédures dans les tableaux.
    - Ajout de nouveaux filtres (notamment pour les PLUI) et distinction précise entre les codes INSEE et SIREN.
    - Affichage de nouvelles informations contextuelles (EPCI à fiscalité propre, informations liées à la loi Huwart).
- **Optimisation de l'ergonomie (Nuxt)** :
    - Ajout de fonctions de sélection/désélection globale dans l'édition des PAC.
    - Amélioration de l'alignement visuel et de la lisibilité des tableaux.
    - Gestion des erreurs lors de la récupération des noms de procédures.

### Évolutions techniques
- **Renforcement de l'administration (Django Admin)** :
    - Extension des droits de gestion pour le personnel (suppression d'utilisateurs, de procédures, d'événements, d'invitations et de projets).
    - Amélioration de la recherche par email de l'utilisateur sur plusieurs objets.
- **Fiabilisation et intégrité des données** :
    - Mise en place de contrôles automatiques de cohérence des procédures avec notifications Slack en cas d'anomalies détectées.
    - Amélioration de la gestion des suppressions en cascade (objets liés et profils utilisateurs).
    - Renforcement de la sécurité des données (RLS) sur les enquêtes.
- **Optimisation de l'architecture** :
    - Migration des appels de données des collectivités vers l'API Django pour une meilleure centralisation.
    - Refonte des modèles de données pour les procédures et les autorités territoriales.
    - Amélioration des performances via l'utilisation de champs mis en cache.
- **DevOps et CI/CD** :
    - Optimisation du cycle de vie des "Review Apps" (automatisation de la désactivation et gestion des tokens).
    - Ajout de nouvelles commandes Makefile pour faciliter les opérations de maintenance.

### Autres changements
- **Maintenance du code** : Nettoyage et documentation des commandes de gestion (management commands) et suppression des scripts obsolètes.
- **Qualité logicielle** : Mise en conformité du code avec les standards de linting (Ruff).
