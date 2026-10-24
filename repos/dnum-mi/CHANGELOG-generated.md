# Synthèse d'activité : dnum-mi (du 01/06 au 31/10)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une montée en maturité significative de plusieurs produits clés. Le passage à la version 1.0.0 de [test-app](/repos/dnum-mi/test-app) et l'implémentation d'un système complet de gestion et de validation des conditions générales d'utilisation dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) témoignent d'une volonté de stabiliser les services et de renforcer la conformité.

Parallèlement, l'accent mis sur l'accessibilité numérique, notamment via les évolutions de [referentiel-applications](/repos/dnum-mi/referentiel-applications) et le développement de [a11y-toolkit](/repos/dnum-mi/a11y-toolkit), renforce l'engagement de l'organisation envers l'inclusion. Enfin, la fiabilité des données a été consolidée par la mise à jour des schémas GraphQL dans [ds-api-client](/repos/dnum-mi/ds-api-client) et l'actualisation des sources de données pour [dashlord-extended](/repos/dnum-mi/dashlord-extended).

## Sécurité
- Renforcement de la sécurité des accès via la migration vers les GitHub Apps et l'application du principe de moindre privilège dans [test-helm](/repos/dnum-mi/test-helm), [test-app](/repos/dnum-mi/test-app) et [fabnum-cicd](/repos/dnum-mi/fabnum-cicd).
- Durcissement de la sécurité des données avec la validation des claims JWT et le masquage des jetons API dans les logs pour [referentiel-applications](/repos/dnum-mi/referentiel-applications).
- Sécurisation des processus de déploiement grâce à l'utilisation de "trusted publishers" dans [ds-api-client](/repos/dnum-mi/ds-api-client).

## Autres changements notables
- **Modernisation des infrastructures de build et de déploiement** : Adoption de standards OCI pour les images Docker dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd), mise à jour des environnements de build (pnpm, Node 24) dans [vue-dsfr](/repos/dnum-mi/vue-dsfr) et optimisation des pipelines CI/CD dans [test-app](/repos/dnum-mi/test-app) et [a11y-toolkit](/repos/dnum-mi/a11y-toolkit).
- **Évolutions des données et des API** : Mise à jour majeure des schémas GraphQL pour [ds-api-client](/repos/dnum-mi/ds-api-client) et actualisation massive des URLs de services publics pour [dashlord-extended](/repos/dnum-mi/dashlord-extended).

## Dépôts les plus actifs
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes (mode hors-ligne, SSR) et stabilisation de l'infrastructure de build.
- [test-app](/repos/dnum-mi/test-app) : Passage en version 1.0.0 et optimisation de l'automatisation CI/CD.
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Évolutions majeures sur l'accessibilité, l'export de données et la gestion des droits.
- [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) : Synchronisation avec l'amont et amélioration des standards de construction Docker.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Implémentation du parcours d'acceptation des CGU et mise à jour de l'infrastructure Docker.
- [ds-api-client](/repos/dnum-mi/ds-api-client) : Mise à jour des schémas GraphQL et fiabilisation des tests.
- [a11y-toolkit](/repos/dnum-mi/a11y-toolkit) : Structuration du projet et ajout de nouveaux outils d'accessibilité.
- [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode) : Enrichissement de la documentation pour l'intégration d'agents d'IA.
- [dashlord-extended](/repos/dnum-mi/dashlord-extended) : Maintenance et actualisation des sources de données.
- [test-helm](/repos/dnum-mi/test-helm) : Sécurisation des workflows de déploiement.
