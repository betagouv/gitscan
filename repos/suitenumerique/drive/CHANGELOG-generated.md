## Changelog : drive (30 derniers jours, au 23 septembre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure du système de gestion des permissions et des restrictions, offrant un contrôle beaucoup plus fin sur la visibilité et l'accès aux dossiers. Parallèlement, des optimisations de performance et des améliorations de la stabilité (notamment via des tests de charge et une meilleure gestion des connexions à la base de données) ont été déployées pour renforcer la robustesse de la plateforme.

### Évolutions fonctionnelles
- **Gestion avancée des restrictions** :
    - Introduction d'un système permettant d'activer ou de désactiver des restrictions sur des dossiers.
    - Les dossiers restreints sont désormais exclus des résultats de recherche, des exports et de l'indexation.
    - Amélioration de la visibilité : les racines restreintes sont masquées dans les listes de premier niveau.
- **Sécurité et droits d'accès** :
    - Renforcement des contrôles lors de la création d'éléments à la racine du drive.
    - Blocage de la suppression de fichiers par un créateur n'ayant plus les droits d'accès nécessaires.
    - Meilleure gestion des droits de téléchargement (upload) pour l'affichage des nouveaux documents.
- **Expérience utilisateur (UI/UX)** :
    - Amélioration du rendu des documents PDF (gestion des polices et décodeurs).
    - Correction de la gestion des langues du navigateur pour une meilleure localisation.
    - Rafraîchissement automatique de la vue "Récents" après une modification de fichier.

### Évolutions techniques
- **Moteur de permissions et Backend** :
    - Refonte architecturale du système de permissions pour une meilleure modularité (séparation des méthodes de calcul des capacités).
    - Optimisation de la recherche des ancêtres de fichiers pour améliorer la rapidité du système.
    - Simplification du flux de traitement du backend.
- **Base de données et Performance** :
    - Implémentation d'un pool de connexions pour `psycopg` afin d'optimiser la gestion des requêtes SQL.
    - Intégration du suivi de performance via Sentry.
- **Tests et Qualité** :
    - Ajout de scénarios de tests de charge avec JMeter (scénarios de lecture intensive et sessions utilisateurs).
    - Amélioration de l'environnement de tests de bout en bout (E2E).
- **Infrastructure et Frontend** :
    - Migration vers les composants UI officiels de la suite gouvernementale (`@gouvfr-lasuite/ui-components`).
    - Mise à jour des configurations Helm et Docker (utilisation d'images Minio via quay.io).
    - Amélioration du processus de bootstrap pour l'installation des dépendances frontend.

### Autres changements
- **Documentation** : Mise à jour du README et documentation détaillée des paramètres de permissions du backend.
- **Nettoyage** : Suppression de variables d'environnement inutilisées (`DB_HOST`, `DB_PORT`) et mise à jour du changelog interne.
