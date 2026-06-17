## Changelog : nosgestesclimat-app (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives en termes d'expérience utilisateur, notamment avec l'ajout d'un nouveau questionnaire sur l'âge, l'intégration d'actions personnalisées et l'amélioration de la gestion des erreurs et des liens. Des optimisations techniques ont également été apportées pour améliorer la performance et la stabilité de l'application, ainsi que pour faciliter le déploiement et les tests.

### Évolutions fonctionnelles
- Ajout d'un formulaire de contact en anglais. [#1853](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1853)
- Mise à jour du texte des services publics affichés sur la page des résultats. [#1851](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1851)
- Ajout de la possibilité de visualiser les sondages anonymes avec des informations sur le mode et l'organisation. [#1850](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1850)
- Amélioration de l'affichage du graphique des catégories sur la page des résultats groupés. [NGC-3196](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1807)
- Implémentation d'une nouvelle page de question sur la tranche d'âge. [#1788](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1788)
- Amélioration de la clarté du texte concernant l'empreinte moyenne sur la page d'accueil. [#1809](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1809)
- Remplacement de la librairie `restcountries` par un package npm plus maintenu. [#1847](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1847)
- Ajout de la possibilité d'afficher l'impact des actions. [#1822](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1822)
- Intégration du "mode scolaire" avec des fonctionnalités spécifiques. [#1758](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1758)
- Ajout d'un bloc d'actions cliquable sur la page de fin. [#1805](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1805)
- Ajout de détails sur les actions. [#1791](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1791)
- Synchronisation des actions depuis Notion. [#1812](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1812)
- Ajout d'un suivi des actions. [#1830](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1830)
- Correction du bouton "Passer" dans la question d'âge. [#1838](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1838)

### Évolutions techniques
- Mise en place d'un helper `createPage` et d'une règle ESLint pour forcer l'utilisation de feature flags dans les tests E2E. [#1840](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1840)
- Mise à jour du script de suppression. [#1844](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1844)
- Utilisation de `pnpm deploy` au lieu de `standalone` pour la production. [#1831](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1831)
- Migration de `zod` vers `valibot` pour la validation des données. [#1801](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1801)
- Ajout d'une table `ActionAssessment` dans la base de données. [#1808](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1808)
- Implémentation de feature flags avec des paramètres d'URL pour les overrides et des fixtures E2E. [#1799](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1799)
- Amélioration du LCP (Largest Contentful Paint) en préchargeant l'illustration de la page d'accueil. [#1802](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1802)
- Ajout d'un worker pour le calcul des actions. [#1811](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1811)
- Activation du suivi automatique avec Posthog sur l'ensemble de l'application. [#1800](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1800)
- Correction d'un crash potentiel de `getClientCookie` pendant le SSR dans `useFeatureFlag`. [#1819](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1819)
- Ajout d'un trigger manuel pour le déploiement de l'application. [#1834](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1834)

### Autres changements
- Correction d'un lien mort. [#1843](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1843)
- Correction d'un problème d'affichage d'iframe sur certaines versions de Safari. [NGC-3465](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1814)
- Correction d'une erreur d'unité pour l'empreinte hydrique totale. [#1797](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1797)
- Correction d'une erreur d'unité pour l'empreinte hydrique. [#1798](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1798)
- Correction de problèmes sur le formulaire de code de vérification. [#1813](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1813)
- Correction du problème de forçage de la région avec le paramètre `region`. [#1824](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1824)
- Correction de l'activation du feature flag pour le mode scolaire.
- Correction de la synchronisation du script Brevo. [#1794](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1794)
- Suppression de la définition du mois sur le calendrier de réservation de démonstration. [#1795](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1795)
- Déplacement des boutons de langue pour réparer les pages de campagne de landing. [#1789](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1789)
- Prévention de la création d'un `VerifiedUser` sans `User`. [#1792](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1792)
- Correction de l'URL de partage avec les paramètres UTM. [#1821](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1821)
- Mise à jour de la version du modèle. [#1810](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1810)
