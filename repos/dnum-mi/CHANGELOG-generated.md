# Synthèse d'activité : dnum-mi (du 05/08 au 20/08/2026)

## Résumé de l'activité
L'activité de cette période est marquée par une montée en maturité significative de plusieurs produits, avec notamment le passage en version 1.0.0 de [test-app](/repos/dnum-mi/test-app) et le lancement de fonctionnalités bêta dans [referentiel-applications](/repos/dnum-mi/referentiel-applications). Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment via la gestion des conditions générales d'utilisation dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) et l'optimisation de l'accessibilité dans [a11y-toolkit](/repos/dnum-mi/a11y-toolkit).

Parallèlement, l'organisation a renforcé la fiabilité de ses services grâce à une modernisation profonde des infrastructures de déploiement et une sécurisation accrue des processus d'automatisation (CI/CD) sur l'ensemble des dépôts.

## Sécurité
- **Gestion des accès et authentification** : Migration vers l'utilisation des GitHub Apps pour renforcer la sécurité des workflows dans [test-helm](/repos/dnum-mi/test-helm) et [test-app](/repos/dnum-mi/test-app).
- **Protection des données et des secrets** : Centralisation des secrets via une API Vault dans [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode) et renforcement de la validation des jetons (JWT) et du masquage des jetons API dans [referentiel-applications](/repos/dnum-mi/referentiel-applications).
- **Audit et conformité** : Intégration de nouveaux outils d'audit de sécurité pour les workflows GitHub Actions dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) et correction de vulnérabilités sur les images Docker dans [referentiel-applications](/repos/dnum-mi/referentiel-applications).

## Autres changements notables
- **Optimisation de la CI/CD** : Restructuration majeure des workflows pour gagner en performance (exécution en parallèle, segmentation des tâches) dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) et [test-app](/repos/dnum-mi/test-app).
- **Évolutions d'infrastructure** : Modernisation des environnements de build (passage à pnpm et Node 24) pour [vue-dsfr](/repos/dnum-mi/vue-dsfr) et mise à jour des images Docker pour [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique).
- **Amélioration produit** : Optimisation de la gestion des icônes pour le mode hors-ligne et le rendu côté serveur dans [vue-dsfr](/repos/dnum-mi/vue-dsfr).

## Dépôts les plus actifs
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Évolutions majeures sur la synchronisation de données, l'accessibilité (RGAA) et les outils de notification.
- [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) : Refonte profonde de l'architecture des workflows et optimisation des performances de la chaîne de CI.
- [test-app](/repos/dnum-mi/test-app) : Passage à la version 1.0.0 et renforcement de l'automatisation du déploiement.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Implémentation complète du flux d'acceptation des conditions générales d'utilisation.
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes et stabilisation de l'infrastructure de build.
- [starter-kit-opencode](/repos/dnum-mi/starter-kit-opencode) : Amélioration de la fiabilité de l'orchestration et intégration d'outils d'assistance IA.
