## Changelog : nosgestesclimat-app (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives concernant les actions proposées aux utilisateurs, avec l'intégration d'une nouvelle version et l'affichage de leur impact. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment pour l'expérience utilisateur sur Safari et pour la gestion des tests et des déploiements. L'ajout d'un mode scolaire et l'amélioration du suivi des événements complètent ces évolutions.

### Évolutions fonctionnelles
- **Actions :** Intégration complète de la nouvelle version des actions, incluant des pages de détails et l'affichage de leur impact sur l'empreinte carbone [#1822](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1822), [#1830](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1830), [#1835](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1835), [#1791](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1791), [#1793](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1793), [#1784](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1784).
- **Mode Scolaire :** Ajout d'un nouveau mode dédié aux établissements scolaires [#1758](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1758).
- **Calculateur :** Implémentation d'une nouvelle question sur la tranche d'âge [#1788](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1788).
- **Partage :** Correction de l'URL de partage pour inclure les paramètres UTM [#1821](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1821).
- **Suivi :** Ajout du suivi des actions réalisées par les utilisateurs [#1830](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1830).
- **Amélioration UX :** Rendre cliquable l'ensemble du bloc des actions à la fin de la simulation [#1805](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1805).

### Évolutions techniques
- **Déploiement :** Utilisation de `pnpm deploy` au lieu de `standalone` pour la production [#1831](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1831).
- **Tests :** Correction des tests E2E et ajout de fixtures pour les tests de feature flags [#1823](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1823), [#1802](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1802).
- **Infrastructure :** Ajout d'un worker pour le calcul des actions afin d'améliorer la performance [#1811](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1811).
- **ORM :** Migration de l'ORM vers le core [#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771).
- **Feature Flags :** Implémentation de la gestion de feature flags via des paramètres d'URL [#1799](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1799).
- **Validation :** Migration de Zod vers Valibot pour la validation des données [#1801](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1801).

### Autres changements
- **Corrections de bugs :**
    - Correction d'un problème d'affichage sur Safari avec les iframes [#1814](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1814).
    - Correction d'un bug empêchant de sauter la question de l'âge [#1838](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1838).
    - Correction du forçage de la région via le paramètre `region` [#1824](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1824).
    - Correction d'un crash lié à la récupération des cookies côté serveur [#1819](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1819).
    - Correction d'erreurs sur le formulaire de code de vérification [#1813](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1813).
    - Correction d'une erreur d'unité pour l'empreinte hydrique totale [#1798](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1798), [#1797](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1797).
    - Correction de l'affichage des boutons de langue sur les pages de campagne [#1789](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1789).
    - Correction d'un problème d'absence de création de `VerifiedUser` sans `User` [#1792](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1792).
- **Documentation :** Mise à jour du titre de la page d'accueil [#1815](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1815).
- **Mise à jour du modèle :** Mise à jour de la version du modèle de calcul [#1810](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1810).
- **Améliorations de l'UX :** Amélioration du texte du mode étudiant [#1803](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1803).
- **Configuration :** Masquage des éléments pour les intégrateurs utilisant des régions de modèle différentes [#1804](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1804).
- **Intégration Brevo :** Sauvegarde de nouveaux attributs dans les contacts Brevo [#1774](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1774).
- **Correction script Brevo :** Correction du script Brevo [#1794](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1794).
