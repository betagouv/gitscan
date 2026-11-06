## Changelog : data-inclusion (30 derniers jours, au 05/11/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la sécurisation des accès et l'optimisation des flux de données. Les utilisateurs bénéficient d'une recherche sémantique enrichie, tandis que l'infrastructure et les pipelines ont été consolidés pour gagner en fiabilité, en performance et en sécurité.

### Évolutions fonctionnelles
- **Recherche améliorée** : Intégration de l'affichage des services à distance dans la recherche sémantique.
- **Validation des données** : Renforcement des contrôles sur les fichiers téléchargés (vérification stricte des formats et des tailles de fichiers).

### Évolutions techniques
- **Sécurité et API** : 
    - Sécurisation de l'authentification (expiration systématique des jetons, gestion optimisée des scopes).
    - Protection de la confidentialité (retrait des jetons des logs et des événements Sentry).
    - Durcissement des règles de sécurité réseau (limitation des hôtes autorisés et routage via Traefik).
- **Pipelines de données** : 
    - Optimisation et nettoyage des flux par la suppression d'ingestions et de champs inutilisés (notamment le module *monenfant* et certains champs *Dora* ou *Carif-Oref*).
    - Ajout de mécanismes de validation des archives avant extraction.
- **Infrastructure et Déploiement** : 
    - Mise à jour des composants critiques (PostgreSQL 18, Terraform, Traefik).
    - Affinement des permissions de stockage (politiques de buckets plus restrictives pour les données *marts* et *raw*).
    - Optimisation des processus de build (déploiement par digest et suppression d'images API inutilisées).
- **Développement et CI/CD** : 
    - Mise en place d'un environnement dbt isolé via `make`.
    - Stabilisation des dépendances critiques.

### Autres changements
- **Documentation** : Refonte complète de la documentation du dépôt.
- **Processus** : Mise à jour des workflows de développement (ajout du rôle de relecteur et intégration de configurations pour Claude Code).
