# Synthèse d'activité : dnum-mi (du 01/08 au 24/08/2026)

## Résumé de l'activité
L'activité de l'organisation a été marquée par des avancées majeures tant sur le plan fonctionnel que sur la maturité des produits. Le passage à la version 1.0.0 de [test-app](/repos/dnum-mi/test-app) et l'élargissement significatif du périmètre de surveillance avec [dashlord](/repos/dnum-mi/dashlord) renforcent la fiabilité et la couverture des services suivis. Parallèlement, l'expérience utilisateur est améliorée via de nouvelles fonctionnalités de conformité dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) et l'intégration d'outils d'accessibilité dans [a11y-toolkit](/repos/dnum-mi/a11y-toolkit).

Les efforts de développement se sont également portés sur l'optimisation des outils de conception, notamment avec une gestion optimisée des icônes pour le mode hors-ligne dans [vue-dsfr](/repos/dnum-mi/vue-dsfr) et l'amélioration de l'expérience de développement via l'intégration d'agents d'IA dans [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode).

## Sécurité
- Renforcement de l'authentification et prévention de l'escalade de privilèges dans [referentiel-applications](/repos/dnum-mi/referentiel-applications).
- Migration vers l'authentification par GitHub App et application du principe de moindre privilège pour sécuriser les processus de [test-helm](/repos/dnum-mi/test-helm) et [test-app](/repos/dnum-mi/test-app).
- Correction de vulnérabilités identifiées dans les modules de [ds-api-client](/repos/dnum-mi/ds-api-client).

## Autres changements notables
- Modernisation des chaînes CI/CD et adoption des standards OCI pour les images Docker dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd).
- Mise à jour majeure de l'infrastructure de build (passage à pnpm et Node 24) pour [vue-dsfr](/repos/dnum-mi/vue-dsfr).
- Refonte de la gestion des sources de données et des scans pour [dashlord-extended](/repos/dnum-mi/dashlord-extended).
- Mise en place de la chaîne de tests automatisés et de la CI/CD pour [a11y-toolkit](/repos/dnum-mi/a11y-toolkit).

## Dépôts les plus actifs
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes (SSR/hors-ligne) et stabilisation de l'infrastructure de build.
- [test-app](/repos/dnum-mi/test-app) : Passage en version 1.0.0 et optimisation massive de l'automatisation et de la sécurité.
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Évolutions fonctionnelles importantes (administration, recherche, export) et durcissement de la sécurité.
- [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) : Synchronisation majeure avec l'amont et amélioration des standards de publication Docker.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Implémentation complète du système de gestion et d'acceptation des CGU.
