## Changelog : potentiel (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, l'équipe a déployé des améliorations significatives sur la gestion des demandes d'abandon de projets, l'importation de données via DN, et la gestion des signalements PPA. Des corrections de bugs et des optimisations de sécurité ont également été apportées, ainsi que des améliorations d'accessibilité et de l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Possibilité pour les utilisateurs de déclarer un état PPA lors d'une demande d'abandon de projet. [#4206](https://github.com/MTES-MCT/potentiel/issues/4206)
- Import des données fournisseur lors de l'importation de candidatures via DN. [#4207](https://github.com/MTES-MCT/potentiel/issues/4207)
- Possibilité pour l'administration d'annuler un signalement PPA. [#4204](https://github.com/MTES-MCT/potentiel/issues/4204)
- Ajout de la possibilité de modifier uniquement le SIRET d'un projet. [#4225](https://github.com/MTES-MCT/potentiel/issues/4225)
- Ajout des coordonnées géodésiques aux projets. [#4191](https://github.com/MTES-MCT/potentiel/issues/4191)
- Intégration des valeurs par défaut pour le coefficient K. [#4160](https://github.com/MTES-MCT/potentiel/issues/4160)
- Import de renouvellement et de puissance initiale avec DN et mise à jour des exports. [#4200](https://github.com/MTES-MCT/potentiel/issues/4200)
- Ajout de la possibilité de demander une mainlevée suite à un abandon de projet. [#4209](https://github.com/MTES-MCT/potentiel/issues/4209)
- Ajout de la fonctionnalité de signalement PPA (DREAL/DGEC). [#4192](https://github.com/MTES-MCT/potentiel/issues/4192)

### Évolutions techniques
- Mise à jour des dépendances Next.js, React et React-DSFR pour corriger des failles de sécurité. [#4195](https://github.com/MTES-MCT/potentiel/issues/4195)
- Correction des erreurs de `pg_notify` et gestion des événements avec des payloads conséquents. [#4237](https://github.com/MTES-MCT/potentiel/issues/4237)
- Suppression des utilisations de `getContext` du package `@potentiel-applications/request-context` dans le SSR. [#4224](https://github.com/MTES-MCT/potentiel/issues/4224)
- Ajout d'un helper server only pour gérer les feature flags côté SSR. [#4218](https://github.com/MTES-MCT/potentiel/issues/4218)
- Ajout de la variable d'environnement `AWS_REGION` nécessaire pour le s3Schema de la partie CLI. [#4188](https://github.com/MTES-MCT/potentiel/issues/4188)
- Ajout d'un nouveau rôle "admin" et transformation de l'ancien rôle "admin" en "dgec". [#4183](https://github.com/MTES-MCT/potentiel/issues/4183)
- Refactor de la GRD, tests, requêtes et ajout d'un test. [#4201](https://github.com/MTES-MCT/potentiel/issues/4201)

### Autres changements
- Corrections de typos, d'éléments de design et d'erreurs liées à la mainlevée et aux attestations. [#4198](https://github.com/MTES-MCT/potentiel/issues/4198)
- Amélioration de l'accessibilité avec l'ajout de liens ARIA aux listes réclamer, documents et utilisateurs. [#4186](https://github.com/MTES-MCT/potentiel/issues/4186)
- Correction d'un bug concernant les notifications de rappel aux GRD. [#4180](https://github.com/MTES-MCT/potentiel/issues/4180)
- Correction de l'export lauréat et ajout des coordonnées à NomEtLocalitéLauréatImportés-V1. [#4232](https://github.com/MTES-MCT/potentiel/issues/4232)
- Correction d'un problème où la suppression d'un GRD sans email de contact pouvait échouer si aucune modification n'était apportée au formulaire. [#4229](https://github.com/MTES-MCT/potentiel/issues/4229)
- Correction d'un test flaky concernant la modification du site de production. [#4240](https://github.com/MTES-MCT/potentiel/issues/4240)
- Ajout de la raison dans les items d'historique. [#4238](https://github.com/MTES-MCT/potentiel/issues/4238)
- Mise à jour des redirections des emails vers les bonnes URLs. [#4239](https://github.com/MTES-MCT/potentiel/issues/4239)
- Ajout de titre manquant et uniformisation. [#4228](https://github.com/MTES-MCT/potentiel/issues/4228)
- Mise à jour des CSP pour Crisp. [#4212](https://github.com/MTES-MCT/potentiel/issues/4212)
- Utilisation de vérifications de variable d'env sur les différents scripts @potentiel/cli. [#4211](https://github.com/MTES-MCT/potentiel/issues/4211)
- Correction de l'import DN : date échéance GF. [#4197](https://github.com/MTES-MCT/potentiel/issues/4197) et [#4200](https://github.com/MTES-MCT/potentiel/issues/4200)
- Correction d'erreurs de suppression et de lister les raccordements pour les projets abandonnés.
- Ajout de ref joue PPE2 Eolien p11. [#4184](https://github.com/MTES-MCT/potentiel/issues/4184)
