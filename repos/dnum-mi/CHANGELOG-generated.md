# Synthèse d'activité : dnum-mi (du 10/08 au 17/08)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en maturité de plusieurs produits clés, illustrée par le passage en version 1.0.0 de [test-app](/repos/dnum-mi/test-app) et le renforcement des outils de gouvernance pour [referentiel-applications](/repos/dnum-mi/referentiel-applications). Les efforts ont également porté sur l'amélioration de l'expérience utilisateur, notamment avec l'intégration d'un système complet de gestion des conditions d'utilisation dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) et l'optimisation du monitoring des services publics via [dashlord](/repos/dnum-mi/dashlord) et [dashlord-extended](/repos/dnum-mi/dashlord-extended).

## Sécurité
- Sécurisation des workflows CI/CD par l'adoption de GitHub Apps et l'application du principe de moindre privilège dans [test-helm](/repos/dnum-mi/test-helm) et [test-app](/repos/dnum-mi/test-app).
- Correction de vulnérabilités de modules dans [ds-api-client](/repos/dnum-mi/ds-api-client).
- Renforcement de la gouvernance, de la gestion des droits et de la traçabilité des utilisateurs dans [referentiel-applications](/repos/dnum-mi/referentiel-applications).

## Autres changements notables
- **Migrations technologiques** : passage au framework NestJS 11 pour [referentiel-applications](/repos/dnum-mi/referentiel-applications) et stabilisation de l'environnement de build sous Node 24 pour [vue-dsfr](/repos/dnum-mi/vue-dsfr).
- **Optimisation de l'automatisation** : unification des processus d'attestation d'images Docker dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) et automatisation des cycles de publication pour [ds-api-client](/repos/dnum-mi/ds-api-client).
- **Amélioration de l'expérience de développement** : activation globale des serveurs LSP dans [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode) et support du rendu local des icônes pour les environnements SSG/SSR dans [vue-dsfr](/repos/dnum-mi/vue-dsfr).

## Dépôts les plus actifs
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes et de la robustesse des processus de build.
- [test-app](/repos/dnum-mi/test-app) : Passage en version majeure 1.0.0 et optimisation de l'infrastructure de déploiement.
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Évolutions majeures de la gouvernance et migration vers NestJS 11.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Implémentation du cycle complet de gestion et d'acceptation des CGU.
- [dashlord](/repos/dnum-mi/dashlord) : Actualisation massive du périmètre de surveillance des services de l'État.
