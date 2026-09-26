# Synthèse d'activité : dnum-mi (du 08/06 au 24/09)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en maturité significative des produits, avec un accent particulier mis sur la sécurité, la conformité et l'observabilité. Les efforts ont permis de renforcer la protection des données et des accès, tout en améliorant l'expérience utilisateur à travers des refontes d'interfaces et l'intégration de nouvelles fonctionnalités de conformité légale, comme la gestion des conditions générales d'utilisation dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique).

Parallèlement, l'organisation a étendu ses capacités de surveillance des services publics via [dashlord](/repos/dnum-mi/dashlord) et a stabilisé ses infrastructures de développement et de déploiement pour garantir des cycles de livraison plus fiables et sécurisés.

## Sécurité
- **Renforcement de la sécurité applicative** : Prévention de l'escalade de privilèges, authentification forte et protection contre les injections SQL/SSRF dans [referentiel-applications](/repos/dnum-mi/referentiel-applications).
- **Sécurisation des accès et de l'infrastructure** : Migration vers l'authentification par GitHub App et application du principe de moindre privilège pour les processus CI/CD dans [test-helm](/repos/dnum-mi/test-helm) et [test-app](/repos/dnum-mi/test-app).
- **Correction de vulnérabilités** : Résolution de failles identifiées dans les modules de [ds-api-client](/repos/dnum-mi/ds-api-client).

## Autres changements notables
- **Évolutions de l'expérience utilisateur et produit** : Amélioration de la gestion des icônes (support hors-ligne et rendu serveur) dans [vue-dsfr](/repos/dnum-mi/vue-dsfr) et mise en place d'un système complet d'acceptation des CGU dans [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique).
- **Expansion du monitoring** : Mise à jour massive du périmètre de surveillance des services de l'État (ANTS, préfectures, administration centrale) dans [dashlord](/repos/dnum-mi/dashlord) et [dashlord-extended](/repos/dnum-mi/dashlord-extended).
- **Standardisation technique** : Adoption des normes OCI pour la construction des images Docker dans [fabnum-cicd](/repos/dnum-mi/fabnum-cicd) et passage à une version fonctionnelle avec tests d'accessibilité automatisés pour [a11y-toolkit](/repos/dnum-mi/a11y-toolkit).

## Dépôts les plus actifs
- [vue-dsfr](/repos/dnum-mi/vue-dsfr) : Amélioration de la gestion des icônes et stabilisation de l'infrastructure de build.
- [test-app](/repos/dnum-mi/test-app) : Passage à la version 1.0.0 et optimisation majeure de l'automatisation CI/CD.
- [referentiel-applications](/repos/dnum-mi/referentiel-applications) : Durcissement de la sécurité et refonte de l'interface d'administration.
- [bibliotheque-numerique](/repos/dnum-mi/bibliotheque-numerique) : Implémentation du flux de conformité pour les conditions générales d'utilisation.
- [dashlord](/repos/dnum-mi/dashlord) : Extension importante du catalogue de services publics surveillés.
