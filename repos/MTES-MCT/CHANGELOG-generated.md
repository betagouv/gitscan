# Synthèse d'activité : MTES-MCT (du 01/07 au 15/08)

## Résumé de l'activité
L'activité de l'organisation cette période est marquée par une forte dynamique de modernisation des interfaces et une extension des capacités d'analyse de données. Les plateformes de gestion environnementale et de l'eau ([partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration), [fisheries-and-environment-data-warehouse](/repos/MTES-MCT/fisheries-and-environment-data-warehouse)) se renforcent avec l'intégration de nouvelles sources de données et de connecteurs.

Parallèlement, les outils liés à l'habitat et à l'urbanisme ([otelo](/repos/MTES-MCT/otelo), [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend), [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant)) bénéficient de refontes ergonomiques majeures et de nouvelles fonctionnalités métier, comme l'autovalidation ou la gestion de scénarios guidés. Enfin, une attention particulière est portée à la robustesse des infrastructures de formation ([parcours-r](/repos/MTES-MCT/parcours-r)) et à la sécurisation des accès API.

## Sécurité
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Correction d'une vulnérabilité potentielle liée aux webhooks propriétaires.
- [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr) : Correction de vulnérabilités via la mise à jour des dépendances.
- [histologe](/repos/MTES-MCT/histologe) : Analyse post-mortem suite à une vulnérabilité.
- [potentiel](/repos/MTES-MCT/potentiel) : Renforcement des permissions sur les routes Next.js.
- [ecobalyse-runner](/repos/MTES-MCT/ecobalyse-runner) : Mise en place d'une authentification par token pour sécuriser l'accès à l'API.
- [mon-devis-sans-oublis-frontend](/repos/MTES-MCT/mon-devis-sans-oublis-frontend) : Amélioration de la sécurité via le contrôle des versions de dépendances critiques.

## Autres changements notables
- **Modernisation des architectures et frameworks** :
  - [vizeau](/repos/MTES-MCT/vizeau) : Migration vers un nouveau système de routage.
  - [rapportnav2](/repos/MTES-MCT/rapportnav2) : Mise à jour majeure vers Spring Boot 4.1.0 et React Router 8.
  - [partaj](/repos/MTES-MCT/partaj) : Passage à React 18 et mise à jour de la pile technologique (Tanstack Query).
  - [ecobalyse](/repos/MTES-MCT/ecobalyse) : Fusion des dépôts de données et du front-end avec migration vers une base de données dédiée.
  - [carbure](/repos/MTES-MCT/carbure) : Refonte de l'architecture des modèles de sites et des structures de données.
- **Optimisation des infrastructures et CI/CD** :
  - [monitor-field](/repos/MTES-MCT/monitor-field) : Automatisation des builds Android (EAS) et intégration de SonarQube/Codecov pour la qualité du code.
  - [parcours-r](/repos/MTES-MCT/parcours-r) : Adaptation des workflows pour l'intégration avec le SSP Cloud.
  - [prelevements-deau-web](/repos/MTES-MCT/prelevements-deau-web) : Mise en place de déploiements automatisés sur Scaleway et intégration de Sentry.

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo), [otelo-front](/repos/MTES-MCT/otelo-front) et [otelo-back](/repos/MTES-MCT/otelo-back) : Refonte complète de la page de résultats et amélioration de la planification territoriale.
- [mobilic](/repos/MTES-MCT/mobilic) et [mobilic-api](/repos/MTES-MCT/mobilic-api) : Introduction de nouveaux processus métier (demandes de détachement, contestations) et amélioration des rapports d'activité.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Évolutions sur la gestion des SIRET et la visibilité du registre.
- [ecobalyse](/repos/MTES-MCT/ecobalyse) et [ecobalyse-data](/repos/MTES-MCT/ecobalyse-data) : Enrichissement massif du catalogue de données et nouveaux formats d'import/export.
- [parcours-r](/repos/MTES-MCT/parcours-r) et ses modules : Mise à jour globale de l'environnement R (4.6.0) et des pipelines de déploiement.
- [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) : Amélioration de l'accessibilité (DSFR) et ajout de la gestion des sites favoris.
