## Changelog : reva (30 derniers jours, au 16 septembre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape majeure avec le déploiement des fonctionnalités de gestion des "VAE Collectives", incluant la création de sous-comptes et une gestion fine des droits d'accès. L'expérience des candidats a été améliorée, notamment pour les dossiers dématérialisés, tandis que les outils d'administration ont été renforcés pour offrir plus d'autonomie aux organismes et une meilleure gestion des informations légales.

### Évolutions fonctionnelles
- **Gestion des VAE Collectives** : 
    - Mise en place de la gestion des sous-comptes (création, consultation, recherche et gestion des droits d'accès par cohorte).
    - Ajout de nouvelles pages dédiées à la gestion des comptes utilisateurs et aux droits d'accès.
- **Parcours Candidat** : 
    - Amélioration du parcours de dématérialisation permettant de modifier les objectifs et les expériences si le dossier est incomplet.
    - Corrections sur le parcours de faisabilité et amélioration de la clarté des libellés.
- **Administration & Organismes (AAP)** : 
    - Autonomie accrue des organismes pour la mise à jour de leurs informations générales.
    - Nouveaux tableaux de bord pour les gestionnaires de registre.
    - Amélioration du processus de validation des informations légales, incluant la possibilité de notifier des motifs de non-conformité.
- **Sécurité** : 
    - Généralisation de l'authentification à deux facteurs (2FA) par email pour les comptes.

### Évolutions techniques
- **API & Données** : 
    - Migration de l'API France Compétences (RNCP) de la version 2 vers la version 4.
    - Intégration des codes INSEE et des codes pays dans les schémas GraphQL.
    - Ajout d'un script pour l'anonymisation complète de la base de données.
- **Architecture** : 
    - Refonte du système de gestion des droits pour les collectifs (passage d'un modèle de permissions à un modèle de rôles).
    - Migration des résolveurs d'autorisation vers une nouvelle logique centralisée (`withPolicies`).
- **Infrastructure** : 
    - Sécurisation de l'accès à Metabase via un réseau privé et un proxy.
    - Ajustements de la configuration Traefik et Keycloak (gestion des checksums).

### Autres changements
- Augmentation significative de la couverture de tests (API, Administration et Candidat).
- Améliorations de l'interface utilisateur (espacements, design des cartes, gestion des états de chargement).
- Nettoyage du code et réorganisation de l'ordre des imports.
