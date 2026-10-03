# Synthèse d'activité : dnum-mi (du 01/08 au 24/08/2026)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une montée en maturité significative de plusieurs projets clés, notamment avec le passage en version 1.0.0 de [test-app](/repos/dnum-mi/test-app) et l'enrichissement des outils d'accessibilité avec [a11y-toolkit](/repos/dnum-mi/a11y-toolkit). Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, comme l'implémentation d'un système de gestion des conditions générales d'utilisation dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) ou la mise à jour des sources de données pour [dashlord-extended](/repos/dnum-mi/dashlord-extended).

Parallèlement, l'organisation renforce ses standards techniques et la fiabilité de ses services, notamment via l'amélioration de la gestion des icônes pour un usage hors-ligne dans [vue-dsfr](/repos/dnum-mi/vue-dsfr) et la standardisation des processus de construction d'images Docker dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd).

## Sécurité
- Renforcement majeur de la sécurité dans [referentiel-applications](/repos/dnum-mi/referentiel-applications) : protection contre les injections SQL, les attaques SSRF, l'escalade de privilèges et sécurisation de l'isolation des données par périmètre.
- Migration vers une authentification par GitHub App et application du principe de moindre privilège pour sécuriser les workflows de [test-helm](/repos/dnum-mi/test-helm) et [test-app](/repos/dnum-mi/test-app).
- Correction de vulnérabilités identifiées dans les modules de [ds-api-client](/repos/dnum-mi/ds-api-client).

## Autres changements notables
- Standardisation des images Docker vers les normes OCI dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd).
- Évolution de l'infrastructure de build et de la gestion des icônes (support SSR/SSG et mode hors-ligne) pour [vue-dsfr](/repos/dnum-mi/vue-dsfr).
- Mise en place d'une chaîne CI/CD complète et de tests d'accessibilité automatisés pour [a11y-toolkit](/repos/dnum-mi/a11y-toolkit).
- Intégration de fonctionnalités liées aux agents d'IA et activation des serveurs LSP dans [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode).

## Dépôts les plus actifs
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes et stabilisation de l'infrastructure de build.
- [test-app](/repos/dnum-mi/test-app) : Passage en version 1.0.0 et renforcement de l'automatisation et de la sécurité.
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Refonte de l'interface d'administration et sécurisation critique du système.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Implémentation du flux complet de gestion des CGU.
- [a11y-toolkit](/repos/dnum-mi/a11y-toolkit) : Structuration du projet et ajout de fonctionnalités d'accessibilité.
