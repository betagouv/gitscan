# Synthèse d'activité : dnum-mi (du 05/08 au 12/08/2026)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en maturité significative de ses produits et une extension de ses capacités de surveillance. Le passage à la version 1.0.0 de [test-app](/repos/dnum-mi/test-app) et l'évolution majeure du [referentiel-applications](/repos/dnum-mi/referentiel-applications), incluant un nouveau moteur de corrélation et un centre de notifications, renforcent la valeur métier des outils. Parallèlement, les capacités de monitoring de [dashlord](/repos/dnum-mi/dashlord) et [dashlord-extended](/repos/dnum-mi/dashlord-extended) s'élargissent pour couvrir un périmètre plus vaste de services publics et de préfectures.

L'organisation met également l'accent sur l'expérience utilisateur et le développement, avec une gestion optimisée des icônes dans [vue-dsfr](/repos/dnum-mi/vue-dsfr), l'intégration facilitée des agents d'IA dans [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode) et la mise en place d'un nouveau flux de gestion des conditions générales d'utilisation dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique).

## Sécurité
- **Renforcement de l'authentification et des accès** : Migration massive vers l'utilisation des GitHub Apps pour sécuriser les processus de publication et application du principe de moindre privilège dans [test-helm](/repos/dnum-mi/test-helm), [test-app](/repos/dnum-mi/test-app) et [fabnum-cicd](/repos/dnum-mi/fabnum-cicd).
- **Protection contre les vulnérabilités** : Corrections d'injections SQL, de protections SSRF et de cloisonnement des permissions dans [referentiel-applications](/repos/dnum-mi/referentiel-applications), ainsi que la correction de vulnérabilités de modules dans [ds-api-client](/repos/dnum-mi/ds-api-client).
- **Sécurisation de la chaîne logicielle** : Mise en place de scans de secrets (Gitleaks), de la signature des composants et de l'attestation des images Docker/charts Helm (via Cosign et SBOM) dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd).
- **Protection des workflows** : Sécurisation contre les injections de commandes shell dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd).

## Autres changements notables
- **Modernisation des infrastructures de build** : Mise à jour des environnements vers `pnpm`, Node 24 et Vite 7 pour [vue-dsfr](/repos/dnum-mi/vue-dsfr).
- **Optimisation du CI/CD et du déploiement** : Amélioration de la gestion des conteneurs, support des monorepos pour les charts Helm et automatisation du nettoyage des ressources dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) et [test-app](/repos/dnum-mi/test-app).
- **Amélioration de l'expérience de développement** : Activation globale des serveurs LSP dans [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode).

## Dépôts les plus actifs
- [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) : Refonte majeure de la sécurité, de l'attestation des composants et de l'automatisation des publications (Docker, Helm, NPM).
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Évolutions fonctionnelles importantes (moteur de corrélation, interface d'administration) et renforcement de la sécurité.
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes (mode hors-ligne/SSR) et stabilisation de l'infrastructure de build.
- [test-app](/repos/dnum-mi/test-app) : Passage en version 1.0.0 et optimisation des pipelines de déploiement.
- [dashlord](/repos/dnum-mi/dashlord) : Extension massive du périmètre de monitoring des services de l'État et des préfectures.
