## Changelog : drive (30 derniers jours, au 01/10/2026)

### Résumé
Cette période a été marquée par un renforcement significatif de la sécurité et de la fiabilité du système de transfert de fichiers. Les améliorations se concentrent sur une meilleure gestion des droits d'accès lors de l'upload, une protection accrue contre les abus via la limitation de débit, ainsi que des optimisations de performance sur le backend et l'infrastructure de stockage local.

### Évolutions fonctionnelles
- **Gestion des droits d'importation** : Désactivation de la création de nouveaux documents pour les utilisateurs ne disposant pas des droits d'upload nécessaires.
- **Expérience utilisateur (UX)** : 
    - Correction de l'affichage de la vue "Récents" qui ne se mettait pas à jour automatiquement après une modification.
    - Amélioration de la gestion des langues du navigateur (correction pour les langues sans région spécifiée).
- **Visualisation de documents** : Correction du rendu des fichiers PDF (gestion des polices et des décodeurs `pdf.js`).

### Évolutions techniques
- **Sécurité et gestion des uploads** :
    - Mise en place d'une réservation de la taille de fichier déclarée avant l'autorisation de l'upload pour une meilleure gestion des ressources.
    - Implémentation d'une limitation de débit (*rate limiting*) sur les points de terminaison de création d'éléments pour prévenir les abus.
    - Nettoyage automatique des éléments en attente (*pending*) en cas d'échec de l'opération.
- **Performances et Backend** :
    - Optimisation de la vitesse de recherche de l'ancêtre lisible le plus élevé dans l'arborescence.
    - Introduction de la gestion du pool de connexions `psycopg` pour optimiser les interactions avec PostgreSQL.
- **Infrastructure et DevOps** :
    - Remplacement de MinIO par RustFS pour le stockage objet en environnement local.
    - Amélioration des déploiements Helm permettant la configuration de variables d'environnement spécifiques pour le backend.
    - Optimisation du processus d'installation des dépendances frontend via conteneur.
- **Sécurité (Mises à jour)** :
    - Application de correctifs de sécurité critiques sur plusieurs composants clés : Django, Next.js, PyJWT et Sharp.
- **Refactoring** :
    - Migration vers le package unifié `@gouvfr-lasuite/ui-components`.
    - Centralisation de la liste des langues dans la configuration i18n.

### Autres changements
- **Documentation** : Documentation des paramètres de permissions du backend et mise à jour des exemples pour le serveur de ressources.
- **Maintenance** : Nettoyage des scripts SQL, des règles Makefile et suppression de variables d'environnement inutilisées.
