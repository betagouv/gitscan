# Synthèse d'activité : dnum-mi (du 05/08 au 12/08)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance de la sécurité et une automatisation accrue des processus de déploiement. Des évolutions majeures ont été apportées aux produits pour améliorer l'expérience utilisateur et la conformité, notamment avec la mise en place de la gestion des conditions générales d'utilisation dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) et l'enrichissement des capacités de surveillance et de notification dans [referentiel-applications](/repos/dnum-mi/referentiel-applications).

Parallèlement, l'organisation a consolidé ses outils de développement et de monitoring, garantissant une meilleure fiabilité des services publics suivis par [dashlord](/repos/dnum-mi/dashlord) et une infrastructure de build plus robuste pour [vue-dsfr](/repos/dnum-mi/vue-dsfr). Le passage à la version 1.0.0 de [test-app](/repos/dnum-mi/test-app) marque également une étape clé dans la maturité de nos applications.

## Sécurité
- **Authentification et accès** : Généralisation de l'utilisation des GitHub Apps pour sécuriser les workflows d'automatisation ([test-helm](/repos/dnum-mi/test-helm), [test-app](/repos/dnum-mi/test-app), [fabnum-cicd](/repos/dnum-mi/fabnum-cicd)) et renforcement de l'authentification forte pour l'administration ([referentiel-applications](/repos/dnum-mi/referentiel-applications)).
- **Protection contre les attaques** : Mise en place de protections contre les injections SQL, SSRF, IDOR et les injections de commandes shell ([referentiel-applications](/repos/dnum-mi/referentiel-applications), [fabnum-cicd](/repos/dnum-mi/fabnum-cicd)).
- **Gestion des vulnérabilités** : Correction de vulnérabilités dans les modules ([ds-api-client](/repos/dnum-mi/ds-api-client)) et intégration de scans de secrets via Gitleaks ([fabnum-cicd](/repos/dnum-mi/fabnum-cicd)).

## Autres changements notables
- **Optimisation CI/CD et DevOps** : Amélioration significative de la gestion des charts Helm, des images Docker (génération de SBOMs avec Cosign) et de la publication de paquets NPM ([fabnum-cicd](/repos/dnum-mi/fabnum-cicd), [test-app](/repos/dnum-mi/test-app)).
- **Infrastructure et Build** : Stabilisation des environnements de build et mise à jour des outils de gestion de paquets ([vue-dsfr](/repos/dnum-mi/vue-dsfr), [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique)).
- **Maintenance des données de surveillance** : Actualisation massive des listes d'URLs pour le monitoring des services de l'État ([dashlord](/repos/dnum-mi/dashlord), [dashlord-extended](/repos/dnum-mi/dashlord-extended)).

## Dépôts les plus actifs
- [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) : Refonte majeure de la sécurité et de l'automatisation des processus de publication.
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Ajout de fonctionnalités de notification, de corrélation et renforcement de la sécurité applicative.
- [test-app](/repos/dnum-mi/test-app) : Passage en version 1.0.0 et optimisation de l'infrastructure de déploiement.
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes (mode hors-ligne/SSR) et stabilisation du build.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Implémentation complète du cycle de gestion et d'acceptation des CGU.
