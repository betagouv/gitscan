## Changelog : nosgestesclimat-app (30 derniers jours, au 05 juin 2026)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives concernant les actions individuelles pour réduire son impact environnemental. L'implémentation et l'affichage des actions sont au cœur des changements, avec l'ajout d'une nouvelle page dédiée, des améliorations de l'interface utilisateur et des corrections de bugs. Des optimisations techniques ont également été apportées pour améliorer la performance et la robustesse de l'application.

### Évolutions fonctionnelles
- **Actions individuelles :** Ajout d'une nouvelle fonctionnalité permettant de visualiser et d'évaluer des actions concrètes pour réduire son empreinte carbone ([#1793](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1793), [#1822](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1822), [#1830](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1830)).
- **Mode scolaire :** Implémentation d'un mode scolaire dédié, avec des ajustements d'interface et de fonctionnalités ([#1758](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1758)).
- **Page d'âge :** Nouvelle page pour la question de l'âge avec une gestion améliorée du bouton "Passer" ([#1788](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1788), [#1838](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1838)).
- **Partage d'URL :** Correction du partage d'URL avec les paramètres UTM pour un meilleur suivi ([#1821](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1821)).
- **Actions sur la fin de simulation :** Affichage des actions proposées à la fin de la simulation ([#1823](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1823)).
- **Amélioration de l'interface :**  Le bloc d'actions est maintenant entièrement cliquable sur la page de fin ([#1805](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1805)).
- **Mise à jour du modèle :** Mise à jour de la version du modèle de calcul de l'empreinte carbone ([#1810](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1810)).

### Évolutions techniques
- **Infrastructure :** Utilisation de `pnpm deploy` au lieu de `standalone` pour la production, améliorant le processus de déploiement ([#1831](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1831)).
- **Tests :** Correction des tests E2E pour assurer la stabilité de l'application ([#1836](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1836)).
- **ORM :** Migration de l'ORM vers le core ([#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771)).
- **Feature Flags :** Ajout de la gestion de *feature flags* avec des paramètres d'URL pour des tests A/B et des déploiements progressifs ([#1799](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1799)).
- **Validation :** Migration de `zod` vers `valibot` pour la validation des données ([#1801](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1801)).
- **Performance :** Amélioration du LCP (Largest Contentful Paint) en préchargeant l'illustration de la page d'accueil ([#1802](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1802)).
- **Workers :** Implémentation de *workers* pour le calcul des actions, améliorant la performance et la réactivité de l'application ([#1811](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1811)).

### Autres changements
- **Documentation :** Mise à jour de la documentation et des textes de l'application ([#1786](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1786), [#1795](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1795), [#1803](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1803), [#1809](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1809), [#1815](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1815)).
- **Intégrations :** Amélioration de l'intégration avec Brevo pour la gestion des contacts ([#1774](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1774), [#1794](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1794)).
- **Corrections de bugs :** Diverses corrections de bugs concernant l'unité de mesure de l'empreinte hydrique, le calendrier de réservation et le chargement des iframes.
- **Déploiement :** Ajout d'un déclencheur manuel pour le déploiement de l'application ([#1834](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1834)).
