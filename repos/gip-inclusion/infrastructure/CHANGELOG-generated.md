## Changelog : infrastructure (30 derniers jours, au 13 octobre 2026)

### Résumé
Ce mois a été marqué par un déploiement majeur de l'infrastructure dédiée à l'environnement "emplois-cnav", incluant la mise en place complète des réseaux, du cluster Kubernetes et des bases de données. Parallèlement, la sécurité a été renforcée par l'intégration de nouveaux outils de gestion de secrets et l'optimisation de la gestion des domaines et du DNS.

### Évolutions fonctionnelles
- **Gestion des domaines** : Récupération du domaine `inclusion.gouv.fr` pour l'utilisation de Bitwarden.
- **Authentification** : Configuration de la base de données pour le service Authentik dans l'environnement emplois-cnav.

### Évolutions techniques
- **Déploiement de l'environnement "emplois-cnav"** : Mise en place complète de l'infrastructure comprenant :
    - Réseau (double réseau privé).
    - Cluster Kubernetes et registre de conteneurs.
    - Modules de bases de données et de gestion de secrets.
    - Instance VPN (Strongswan) et instances Windows (OGC).
- **DNS & Messagerie** : 
    - Configuration des enregistrements DNS pour les services Brevo (parsing entrant et authentification du sous-domaine 'reply').
    - Mise en place de la configuration DNS pour emplois-cnav.
- **Sécurité & IAM** :
    - Implémentation de SOPS pour la sécurisation des entrées Terraform sensibles.
    - Gestion des secrets pour ArgoCD et Authentik.
    - Optimisation des permissions IAM (accès local pour les développeurs, gestion des droits sur les bases de données et application IAM pour l'API-Relay).
- **Maintenance & CI/CD** :
    - Mise à jour régulière de la version de Terraform utilisée dans la CI.
    - Verrouillage et mise à jour des fournisseurs (providers) Terraform.

### Autres changements
- Mise à jour de la documentation technique via `terraform-docs`.
