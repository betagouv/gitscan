## Changelog : nosgestesclimat-app (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives concernant les actions proposées aux utilisateurs, avec l'ajout d'un nouveau backend pour gérer ces actions et l'intégration de données plus précises. Des optimisations ont également été apportées pour améliorer l'expérience utilisateur, notamment en corrigeant des bugs et en améliorant la performance. L'application a également bénéficié de l'ajout d'un mode "scolaire" et de la possibilité de configurer le mode simulation via l'URL.

### Évolutions fonctionnelles
- Ajout d'un nouveau backend pour les actions, permettant d'afficher des impacts et des détails plus précis. [#1791](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1791), [#1822](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1822)
- Implémentation d'un mode "scolaire" pour adapter l'application à un public étudiant. [#1758](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1758)
- Possibilité de configurer le mode simulation directement via l'URL. [#1859](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1859)
- Amélioration de la page de détails des actions, avec des corrections de visibilité et de SEO. [#1855](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1855)
- Amélioration du texte et de la formulation concernant les actions proposées. [#1849](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1849), [#1837](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1837), [#1835](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1835)
- Affichage du formulaire de contact en anglais. [#1853](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1853)
- Mise à jour du texte concernant l'empreinte moyenne sur la page d'accueil. [#1809](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1809)
- Nouvelle question sur la tranche d'âge de l'utilisateur. [#1788](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1788)
- Amélioration de la présentation du graphique des catégories sur la page des résultats groupés. [#1807](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1807)

### Évolutions techniques
- Migration de `zod` vers `valibot` pour la validation des données. [#1801](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1801)
- Refonte du système de déploiement avec `pnpm deploy` au lieu de `standalone`. [#1831](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1831)
- Ajout de tests E2E pour les feature flags. [#1816](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1816)
- Implémentation de la gestion des feature flags avec des paramètres d'URL. [#1799](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1799)
- Ajout d'un worker pour le calcul des actions. [#1811](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1811)
- Utilisation d'un package npm pour les informations sur les pays, remplaçant `restcountries`. [#1847](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1847)
- Ajout d'une table `ActionAssessment` dans la base de données. [#1808](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1808)
- Amélioration de la performance en préchargeant l'illustration de la page d'accueil. [#1802](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1802)
- Correction d'un crash potentiel lors de la récupération des cookies côté serveur. [#1819](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1819)

### Autres changements
- Intégration de PostHog pour l'autotracking des événements utilisateurs. [#1800](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1800)
- Correction de liens morts. [#1843](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1843)
- Correction de bugs liés au chargement du modèle de nuit. [#1860](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1860)
- Correction de bugs liés à la mise à jour de la langue via les paramètres régionaux. [#1841](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1841)
- Correction d'un problème d'iframe sur certaines versions de Safari. [#1814](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1814)
- Ajout d'un déclencheur manuel pour le déploiement de l'application. [#1834](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1834)
- Correction d'un bug sur le bouton de saut de la question d'âge. [#1838](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1838)
- Ajout de migrations pour les utilisateurs anonymes et les sondages anonymes. [#1856](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1856)
- Amélioration du suivi des actions. [#1852](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1852)
- Correction de bugs sur le formulaire de code de vérification. [#1813](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1813)
- Mise à jour de la version du modèle. [#1810](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1810)
- Correction de l'URL de partage avec les paramètres UTM. [#1821](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1821)
