# Synthèse d'activité : dnum-mi (du 24/06 au 24/09/2026)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une phase de consolidation et de montée en maturité de plusieurs produits clés. Plusieurs projets ont franchi des étapes importantes, comme le passage en version 1.0.0 de [test-app](/repos/dnum-mi/test-app) ou la stabilisation fonctionnelle de [a11y-toolkit](/repos/dnum-mi/a11y-toolkit). Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur (gestion des CGU dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique), refonte d'interface dans [referentiel-applications](/repos/dnum-mi/referentiel-applications)), la modernisation des infrastructures de déploiement (normes OCI dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd)) et un renforcement global de la sécurité.

## Sécurité
- **Renforcement critique** : Prévention des injections SQL, des attaques SSRF et de l'escalade de privilèges dans [referentiel-applications](/repos/dnum-mi/referentiel-applications), accompagnée d'une meilleure isolation des données et de l'imposition d'une authentification forte.
- **Gestion des accès** : Migration vers l'authentification par GitHub App et application du principe de moindre privilège pour sécuriser les workflows de [test-helm](/repos/dnum-mi/test-helm) et [test-app](/repos/dnum-mi/test-app).
- **Correction de vulnérabilités** : Résolution de failles identifiées dans les modules de [ds-api-client](/repos/dnum-mi/ds-api-client).

## Autres changements notables
- **Standardisation et Infrastructure** : Adoption des normes OCI pour la construction d'images Docker dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) et modernisation de l'environnement de build (pnpm, Node 24) pour [vue-dsfr](/repos/dnum-mi/vue-dsfr).
- **Évolutions Produits** : Implémentation d'un système complet de gestion, d'affichage et d'acceptation des conditions générales d'utilisation (CGU) dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique).
- **Expérience Développeur** : Amélioration de l'autocomplétion et de l'environnement de développement via l'activation des serveurs LSP dans [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode).

## Dépôts les plus actifs
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes (SSR/offline) et de l'infrastructure de build.
- [test-app](/repos/dnum-mi/test-app) : Passage à la version 1.0.0 et optimisation massive de l'automatisation CI/CD.
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Refonte de l'interface d'administration et renforcement majeur de la sécurité.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Mise en place du flux complet d'acceptation des CGU.
- [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) : Standardisation des images Docker et fiabilisation des processus de scan et de nettoyage.
