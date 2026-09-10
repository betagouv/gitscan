## Changelog : reva (30 derniers jours, au 08/09/2026)

### Résumé
Ce mois a été marqué par deux évolutions majeures : l'introduction de la gestion des "sous-comptes" pour la VAE Collective, permettant une délégation de gestion plus fine, et la refonte du processus de mise à jour des informations légales pour les organismes, visant à accroître leur autonomie tout en renforçant le contrôle administratif.

### Évolutions fonctionnelles
- **VAE Collective** : Mise en place complète de la gestion des sous-comptes, incluant la création, la liste des comptes, l'attribution de droits spécifiques et une interface de gestion dédiée.
- **Gestion des organismes (AAP)** : Nouveau parcours de mise à jour des informations légales permettant aux structures de modifier leurs données en autonomie. Les administrateurs disposent désormais d'outils pour valider ces changements ou notifier des motifs de non-conformité.
- **Tableaux de bord** : Possibilité d'afficher des tableaux de bord intégrés pour les gestionnaires de registres.
- **Sécurité** : Activation par défaut de l'authentification à deux facteurs (2FA) via code email lors de la création de compte.
- **Expérience Candidat** : Amélioration de la clarté des formulaires, de la terminologie et de l'affichage des données relatives aux organismes.

### Évolutions techniques
- **Architecture API** : Migration massive des résolveurs (candidatures, certifications, autorités) vers un nouveau système de gestion des politiques d'autorisation (`withPolicies`) pour une sécurité accrue.
- **Interopérabilité** : Migration de l'API France Compétences (RNCP) vers la version 4 et enrichissement des données d'identité avec l'intégration des codes pays INSEE.
- **Infrastructure & Sécurité** : Renforcement de la sécurité de Metabase (accès restreint au réseau privé) et mise à jour des configurations de buildpack pour Keycloak.
- **Qualité logicielle** : Augmentation significative de la couverture de tests, avec un focus particulier sur les règles d'autorisation complexes et les parcours de validation des données.
- **Base de données** : Correction de migrations Prisma.

### Autres changements
- Ajustements cosmétiques de l'interface utilisateur (espacements, mise en page des cartes de certification).
- Nettoyage du code et optimisation de l'ordre des imports.
