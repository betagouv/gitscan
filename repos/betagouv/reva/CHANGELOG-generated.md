## Changelog : reva (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes dans la gestion des AAPs avec l'introduction de la sélection des "formacodes" (v2) et un nouveau parcours de mise à jour des informations légales pour les structures. Le module "VAE Collective" est également enrichi avec une gestion plus fine des sous-comptes et des permissions. Parallèlement, une refonte profonde du système d'autorisation a été réalisée pour renforcer la sécurité et la fiabilité de l'accès aux données.

### Évolutions fonctionnelles
- **Gestion des AAPs et structures** :
    - Introduction de la sélection des "formacodes" (v2) dans les composants de certification et de périmètre d'accompagnement.
    - Mise en place d'un nouveau parcours de mise à jour des informations légales pour les structures AAP.
    - Ajout d'un bloc d'information légale sur la page "maison mère" des AAP.
- **VAE Collective** :
    - Ajout d'un onglet de gestion des comptes utilisateurs dans l'en-tête.
    - Implémentation de permissions affinées pour la gestion des cohortes (création, modification, suppression, consultation des statistiques).
- **Expérience Candidat** :
    - Amélioration de l'interface avec l'ajout de modales de confirmation lors de l'envoi de documents à l'autorité de certification.
    - Pré-sélection automatique de l'autorité de certification dans les fichiers PDF de décision de faisabilité lorsque celle-ci est renseignée.
    - Renforcement de la validation des formulaires (exigence du code postal pour l'adresse).
- **Corrections diverses** :
    - Correction de l'affichage de l'historique des décisions lorsque la date de mise à jour de l'AAP est manquante.
    - Résolution de bugs sur la mise à jour des autorités de certification et la préservation des données de formulaire lors des rafraîchissements de données.

### Évolutions techniques
- **Sécurité et Autorisation** :
    - Refonte majeure de l'API : migration massive des "resolvers" (candidatures, certifications, logs, rendez-vous, etc.) vers un nouveau système de gestion des politiques (`withPolicies`).
    - Renforcement de la couverture de tests de sécurité pour valider les droits d'accès sur l'ensemble du cycle de vie d'une candidature (jury, expérience, transfert de dossier, etc.).
    - Implémentation d'un nouveau modèle de rôles et de permissions spécifique au module "VAE Collective".
- **Infrastructure et Performance** :
    - Sécurisation de l'accès à Metabase via une restriction au niveau du reverse proxy (Traefik).
    - Optimisation des performances de l'interface d'administration via l'utilisation de requêtes GraphQL conditionnelles selon le profil utilisateur.
    - Optimisation des scripts de mise à jour de données par l'introduction du traitement par lots (batch processing).
- **Tests** :
    - Extension significative de la suite de tests d'intégration HTTP pour le package `reva-interop` (couverture des routes candidatures, jury, faisabilité, etc.).

### Autres changements
- **Maintenance** : Mise à jour des compatibilités navigateurs et nettoyage de constantes codées en dur dans l'API.
