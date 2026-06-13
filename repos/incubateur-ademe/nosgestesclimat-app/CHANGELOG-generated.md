## Changelog : nosgestesclimat-app (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives concernant les actions proposées aux utilisateurs pour réduire leur empreinte carbone, avec l'intégration d'un nouveau backend pour les actions et l'affichage de leur impact. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment pour l'expérience utilisateur sur différents navigateurs et appareils, ainsi que pour le déploiement et les tests. Un mode "scolaire" a été ajouté pour faciliter l'utilisation en milieu éducatif.

### Évolutions fonctionnelles
- Ajout d'un nouveau mode "scolaire" pour une utilisation en classe [#1758](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1758)
- Implémentation de l'affichage de l'impact des actions proposées aux utilisateurs [#1822](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1822)
- Intégration d'un nouveau backend pour la gestion des actions [#1793](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1793) et détails des actions [#1791](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1791)
- Amélioration de la page de question sur l'âge avec une nouvelle interface [#1788](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1788)
- Possibilité d'évaluer les actions à la fin de la simulation [#1823](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1823)
- Synchronisation des actions depuis Notion [#1812](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1812)
- Amélioration du texte et de l'expérience utilisateur pour le mode intégrateur [#1804](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1804) et étudiant [#1803](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1803)
- Correction de l'unité d'affichage de l'empreinte hydrique [#1798](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1798) et [#1797](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1797)
- Mise à jour de la version du modèle de calcul de l'empreinte carbone [#1810](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1810)
- Correction du partage d'URL avec des paramètres UTM [#1821](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1821)
- Correction du bouton de saut de la question d'âge [#1838](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1838)

### Évolutions techniques
- Migration de Zod vers Valibot pour la validation des données [#1801](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1801)
- Utilisation de pnpm deploy au lieu de standalone pour la production [#1831](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1831)
- Ajout d'une table `ActionAssessment` en base de données [#1808](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1808)
- Implémentation de feature flags avec des paramètres d'URL pour les tests A/B [#1799](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1799)
- Ajout d'un worker pour le calcul des actions [#1811](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1811)
- Préchargement de l'illustration de la page d'accueil pour améliorer le LCP (Largest Contentful Paint) [#1802](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1802)
- Activation de Posthog pour l'autotrack d'événements [#1800](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1800)
- Correction d'un crash potentiel lié à l'utilisation de cookies côté serveur [#1819](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1819)
- Correction d'un problème d'iframe sur certaines versions de Safari [#1814](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1814)

### Autres changements
- Correction de liens morts [#1843](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1843)
- Mise à jour du titre de la page d'accueil [#1815](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1815)
- Amélioration du style de la bannière beta sur la page "mon espace" / "action" [#1836](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1836)
- Ajout d'un déclencheur manuel pour le déploiement de l'application [#1834](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1834)
- Correction de tests E2E [#1836](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1836) et [#1823](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1823)
- Suppression d'une définition de mois erronée sur le calendrier de réservation de démonstration [#1795](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1795)
- Déplacement des boutons de langue pour corriger des problèmes sur les pages de campagne [#1789](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1789)
- Correction d'un bug empêchant la création de `VerifiedUser` sans `User` [#1792](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1792)
- Correction d'un script Brevo qui ne se synchronisait pas [#1794](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1794)
- Suppression d'un script de suppression obsolète [#1844](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1844)
