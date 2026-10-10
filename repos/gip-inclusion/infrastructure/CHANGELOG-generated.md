## Changelog : infrastructure (30 derniers jours, au 06/10/2026)

### Résumé
Ce mois a été marqué par un travail intensif sur le déploiement de l'infrastructure dédiée au projet "emplois-cnav". L'essentiel des efforts a porté sur la mise en place de l'architecture de base (réseau, bases de données, Kubernetes) et le renforcement de la sécurité via une meilleure gestion des secrets et des accès.

### Évolutions fonctionnelles
- **Amélioration de la messagerie** : Optimisation de la fiabilité des emails via Brevo grâce à l'ajout de nouveaux enregistrements DNS (authentification du sous-domaine 'reply' et activation du service de parsing entrant).

### Évolutions techniques
- **Déploiement de l'infrastructure "emplois-cnav"** : Mise en place complète des modules fondamentaux, incluant :
    - Le cluster Kubernetes et le registre de conteneurs.
    - Le réseau (configuration avec doubles réseaux privés) et l'instance VPN Strongswan.
    - Les modules de bases de données et d'instances Windows (OGC).
    - La gestion des identités (IAM) et la configuration de la base de données Authentik.
- **Sécurité et gestion des secrets** :
    - Intégration de SOPS pour sécuriser les entrées sensibles de Terraform.
    - Mise en place du module Secret Manager et sécurisation des secrets de la base de données Authentik.
    - Renforcement des permissions IAM pour permettre aux développeurs la gestion locale de certaines ressources d'état et l'accès aux versions antérieures de l'état pour "emplois-cnav".
    - Correction de dérives de permissions sur les bases de données pour assurer la cohérence des droits.
- **CI/CD et maintenance de l'infrastructure** :
    - Mise à jour de la version de Terraform dans la chaîne de CI (passage à la version 1.16.5).
    - Assouplissement de la version du fournisseur Scaleway pour faciliter les mises à jour.

### Autres changements
- Mise à jour de la documentation technique Terraform.
