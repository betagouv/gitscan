# Synthèse d'activité : dnum-mi (du 05/10 au 12/10)

## Résumé de l'activité
L'activité de l'organisation a été marquée par des étapes de maturité importantes pour plusieurs projets clés. [test-app](/repos/dnum-mi/test-app) a franchi un cap majeur avec le passage en version 1.0.0, tandis que [referentiel-applications](/repos/dnum-mi/referentiel-applications) a considérablement enrichi ses capacités fonctionnelles, notamment via de nouveaux outils d'exportation et d'administration.

Parallèlement, l'expérience utilisateur et la fiabilité des outils ont été renforcées : [vue-dsfr](/repos/dnum-mi/vue-dsfr) a optimisé la gestion des icônes pour les environnements modernes, [a11y-toolkit](/repos/dnum-mi/a11y-toolkit) est passé en phase fonctionnelle avec l'ajout de modes de consultation d'accessibilité, et [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode) a intégré des capacités d'assistance par intelligence artificielle.

## Sécurité
- **Gestion des accès et authentification** : Migration vers l'utilisation de GitHub Apps pour renforcer la sécurité des workflows de déploiement dans [test-helm](/repos/dnum-mi/test-helm) et [test-app](/repos/dnum-mi/test-app).
- **Protection des données et des secrets** : 
    - Centralisation et sécurisation des secrets via une API Vault dans [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode).
    - Durcissement des accès dans [referentiel-applications](/repos/dnum-mi/referentiel-applications) via la validation JWT, le masquage de jetons et la limitation de l'impersonation.
- **Sécurisation des déploiements** : Utilisation de "trusted publishers" pour sécuriser les publications dans [ds-api-client](/repos/dnum-mi/ds-api-client).

## Autres changements notables
- **Optimisation CI/CD et Infrastructure** :
    - Amélioration de la robustesse des pipelines et de la gestion des releases (support GitHub App, gestion de la concurrence) dans [test-app](/repos/dnum-mi/test-app), [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) et [ds-api-client](/repos/dnum-mi/ds-api-client).
    - Modernisation des environnements de build et de déploiement (passage à pnpm, Node 24, standards OCI pour Docker) dans [vue-dsfr](/repos/dnum-mi/vue-dsfr) et [fabnum-cicd](/repos/dnum-mi/fabnum-cicd).
    - Refonte de l'infrastructure conteneur et des processus de démarrage dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique).
- **Évolutions des données et API** :
    - Mise à jour majeure des schémas GraphQL et ajout d'un module de gestion locale dans [ds-api-client](/repos/dnum-mi/ds-api-client).
    - Actualisation massive des sources de données gouvernementales dans [dashlord-extended](/repos/dnum-mi/dashlord-extended).

## Dépôts les plus actifs
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Ajout de fonctionnalités d'exportation (Excel, PowerPoint), de recherche et d'un panneau d'administration.
- [test-app](/repos/dnum-mi/test-app) : Passage en version 1.0.0 et optimisation de l'automatisation et de la sécurité.
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes (mode hors-ligne, SSR) et stabilisation de l'infrastructure de build.
- [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode) : Intégration d'agents IA (Claude Code) et amélioration des outils de diagnostic système.
- [ds-api-client](/repos/dnum-mi/ds-api-client) : Mise à jour des schémas GraphQL et amélioration de la CI/CD.
- [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) : Synchronisation avec l'amont et renforcement des standards de construction Docker/OCI.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Implémentation du flux d'acceptation des CGU et mise à jour de l'infrastructure Docker.
- [a11y-toolkit](/repos/dnum-mi/a11y-toolkit) : Mise en place de la chaîne CI/CD et ajout de nouveaux outils de consultation d'accessibilité.
- [test-helm](/repos/dnum-mi/test-helm) : Sécurisation des processus d'automatisation et de déploiement.
- [dashlord-extended](/repos/dnum-mi/dashlord-extended) : Maintenance et actualisation des URLs des sources de données.
