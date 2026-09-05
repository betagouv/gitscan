# Synthèse d'activité : dnum-mi (du 01/08 au 31/08/2026)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en maturité significative, tant sur le plan de la sécurité que de l'expérience utilisateur. Les efforts se sont concentrés sur la sécurisation des processus de déploiement et le renforcement de la protection des données. 

Les utilisateurs bénéficieront de services de surveillance plus précis ([dashlord](/repos/dnum-mi/dashlord)), de fonctionnalités de conformité améliorées pour la gestion des conditions d'utilisation ([bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique)) et de composants UI plus performants, notamment pour les usages hors-ligne ([vue-dsfr](/repos/dnum-mi/vue-dsfr)).

## Sécurité
- Généralisation de l'authentification via GitHub App pour sécuriser les workflows de publication et de scan ([test-helm](/repos/dnum-mi/test-helm), [test-app](/repos/dnum-mi/test-app), [fabnum-cicd](/repos/dnum-mi/fabnum-cicd)).
- Renforcement de la protection contre les injections (SQL, SSRF, shell) et application du principe de moindre privilège ([referentiel-applications](/repos/dnum-mi/referentiel-applications), [fabnum-cicd](/repos/dnum-mi/fabnum-cicd)).
- Correction de vulnérabilités dans les modules et mise en place de scans de secrets ([ds-api-client](/repos/dnum-mi/ds-api-client), [fabnum-cicd](/repos/dnum-mi/fabnum-cicd)).
- Amélioration de la traçabilité des images via l'attestation des composants et la génération de SBOMs ([fabnum-cicd](/repos/dnum-mi/fabnum-cicd)).

## Autres changements notables
- **Optimisation de la CI/CD** : Support des monorepos, automatisation des releases et gestion améliorée des charts Helm ([fabnum-cicd](/repos/dnum-mi/fabnum-cicd), [test-app](/repos/dnum-mi/test-app)).
- **Évolutions d'infrastructure et de build** : Stabilisation des environnements de build (Node 24, pnpm) et mise à jour des images Docker ([vue-dsfr](/repos/dnum-mi/vue-dsfr), [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique)).
- **Mise à jour des données de surveillance** : Actualisation exhaustive des catalogues d'URLs pour les services publics, les préfectures et les services de l'ANTS ([dashlord](/repos/dnum-mi/dashlord), [dashlord-extended](/repos/dnum-mi/dashlord-extended)).

## Dépôts les plus actifs
- [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) : Refonte majeure de la sécurité et de l'automatisation des pipelines.
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Évolutions fonctionnelles majeures et renforcement de la sécurité.
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes et de l'infrastructure de build.
- [test-app](/repos/dnum-mi/test-app) : Passage à la version 1.0.0 et optimisation de l'automatisation.
