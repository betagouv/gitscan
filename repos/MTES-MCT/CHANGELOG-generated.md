# Synthèse d'activité : MTES-MCT (du 15/04 au 23/04/2026)

## Résumé de l'activité
L'activité récente de l'organisation MTES-MCT se concentre sur l'amélioration continue de ses outils et plateformes, avec un accent particulier sur l'expérience utilisateur et la qualité des données. Plusieurs dépôts ont bénéficié de corrections de bugs, d'optimisations de performance et d'ajouts de nouvelles fonctionnalités. On note des avancées significatives dans les domaines de la gestion des données environnementales (monitorfish, ecobalyse, fisheries-and-environment-data-warehouse), du suivi des déchets (trackdechets), de la gestion du territoire (dialog, potentiel, acceslibre) et de la simplification des démarches administratives (otelo, dossier-facile-frontend). L'intégration de nouvelles sources de données et l'amélioration de la sécurité sont également des thèmes récurrents.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction de vulnérabilités XSS dans [envergo](/repos/MTES-MCT/envergo).
- Renforcement de la sécurité avec vérification de la revendication `organizational_unit` dans [monitorenv](/repos/MTES-MCT/monitorenv).
- Ajout d'une limite de complexité pour les requêtes GraphQL dans [mobilic-api](/repos/MTES-MCT/mobilic-api).
- Ajout des en-têtes HTTP `Referrer` et `crossOrigin` dans [trackdechets](/repos/MTES-MCT/trackdechets).

## Autres changements notables
- Dockerisation de l'application [partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration) pour simplifier le déploiement.
- Refonte de l'authentification dans [ecobalyse](/repos/MTES-MCT/ecobalyse) avec suppression de l'authentification par cookie.
- Migration vers pnpm pour la gestion des dépendances dans [verseau2](/repos/MTES-MCT/verseau2).
- Intégration de GitLab CI dans [partaj](/repos/MTES-MCT/partaj) pour améliorer l'intégration continue.
- Mise à jour majeure de Flask dans [mobilic-api](/repos/MTES-MCT/mobilic-api).

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo) : Refonte significative du tableau de bord et ajout de nouvelles fonctionnalités de gestion des utilisateurs et des données.
- [monitorfish](/repos/MTES-MCT/monitorfish) : Corrections de bugs et ajout de nouvelles catégories d'infractions, ainsi que des améliorations cartographiques.
- [dialog](/repos/MTES-MCT/dialog) : Amélioration de la gestion des arrêtés, intégration de nouvelles sources de données et ajout de notifications Mattermost.
- [mobilic-api](/repos/MTES-MCT/mobilic-api) : Corrections de bugs, améliorations de sécurité et mise à jour de Flask.
- [acceslibre](/repos/MTES-MCT/acceslibre) : Implémentation de la génération de PDF pour les ERP et amélioration de l'API pour les widgets.
