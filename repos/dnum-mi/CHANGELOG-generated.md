# Synthèse d'activité : dnum-mi (du 05/08 au 12/08)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une montée en maturité de plusieurs produits clés, notamment avec le passage en version 1.0.0 de [test-app](/repos/dnum-mi/test-app). Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, comme l'intégration d'un flux de gestion des conditions d'utilisation dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) ou l'optimisation de la recherche et de la gouvernance dans [referentiel-applications](/repos/dnum-mi/referentiel-applications). 

Parallèlement, la fiabilité du suivi des services publics a été renforcée via une mise à jour majeure des périmètres de surveillance dans [dashlord](/repos/dnum-mi/dashlord) et [dashlord-extended](/repos/dnum-mi/dashlord-extended). Enfin, l'organisation continue d'investir dans l'accompagnement des nouveaux usages, notamment l'intégration d'agents d'IA avec [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode).

## Sécurité
- **Renforcement de l'authentification** : Migration vers l'utilisation de GitHub Apps pour sécuriser les accès et appliquer le principe de moindre privilège dans les workflows de [test-helm](/repos/dnum-mi/test-helm) et [test-app](/repos/dnum-mi/test-app).
- **Correction de vulnérabilités** : Résolution de failles de sécurité dans les modules de [ds-api-client](/repos/dnum-mi/ds-api-client).
- **Gouvernance** : Amélioration de la traçabilité des actions et renforcement des outils d'administration dans [referentiel-applications](/repos/dnum-mi/referentiel-applications).

## Autres changements notables
- **Migrations technologiques majeures** : Passage au framework NestJS 11 pour [referentiel-applications](/repos/dnum-mi/referentiel-applications) et mise à jour de l'environnement de build (Node 24, pnpm v11) pour [vue-dsfr](/repos/dnum-mi/vue-dsfr).
- **Optimisation de l'infrastructure et CI/CD** : Unification des processus d'attestation d'images Docker dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) et amélioration de la gestion des icônes pour les environnements hors-ligne et le rendu côté serveur (SSR) dans [vue-dsfr](/repos/dnum-mi/vue-dsfr).
- **Expérience de développement** : Activation globale des serveurs LSP pour améliorer l'autocomplétion et le développement avec [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode).

## Dépôts les plus actifs
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes et stabilisation de la chaîne de build.
- [test-app](/repos/dnum-mi/test-app) : Passage en version majeure 1.0.0 et optimisation de l'automatisation de déploiement.
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Refonte de la gouvernance et migration vers NestJS 11.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Implémentation complète du système d'acceptation des CGU.
- [dashlord](/repos/dnum-mi/dashlord) : Mise à jour massive du périmètre de monitoring des services de l'État.
