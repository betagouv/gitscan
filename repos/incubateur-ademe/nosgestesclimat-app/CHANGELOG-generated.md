## Changelog : nosgestesclimat-app (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de performance, notamment au niveau du temps de chargement initial. De nouvelles fonctionnalités ont été ajoutées, en particulier autour du "mode scolaire" et de la gestion des actions, ainsi que des corrections de bugs pour améliorer l'expérience utilisateur et la fiabilité de l'application. Le suivi analytique a également été renforcé.

### Évolutions fonctionnelles
- Ajout d'un "mode scolaire" pour adapter l'application à un usage pédagogique [#1758](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1758).
- Implémentation de la fonctionnalité "Actions" avec la liste des actions, le détail des actions et la gestion des attributs liés aux organisations via Brevo [#1793](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1793), [#1791](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1791), [#1784](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1784), [#1774](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1774).
- Amélioration de l'affichage des points sur les graphiques [#1780](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1780).
- Correction de l'unité d'affichage de l'empreinte hydrique [#1798](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1798), [#1797](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1797).
- Correction du bouton "Terminer" bloqué dans le questionnaire [#1776](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1776).
- Correction de l'affichage des noms des participants et des administrateurs [#1773](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1773).
- Suppression de la bannière JVA [#1779](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1779).
- Correction du positionnement des boutons de langue sur les pages d'atterrissage des campagnes [#1789](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1789).

### Évolutions techniques
- Amélioration du LCP (Largest Contentful Paint) en préchargeant l'illustration de la page d'accueil [#1802](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1802).
- Activation du suivi automatique avec PostHog sur l'ensemble de l'application [#1800](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1800).
- Mise en place de paramètres d'override des feature flags via les paramètres d'URL [#1799](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1799).
- Migration de l'ORM vers le core [#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771).
- Correction de la synchronisation du script Brevo [#1794](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1794).
- Correction d'un problème empêchant la création d'un `VerifiedUser` sans `User` associé [#1792](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1792).
- Correction du chargement des iframes en évitant les collisions avec les variables globales [#1786](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1786).
- Correction du suivi analytique du site et des iframes [#1783](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1783), [#1782](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1782).
- Suppression du déploiement en pré-production en raison d'un pentest [#1787](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1787).
- Récupération sécurisée des données Matomo via un token [#1770](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1770).

### Autres changements
- Correction d'un bug lié à la définition du mois dans le calendrier de réservation de démonstration [#1795](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1795).
- Ajout d'un feature flag pour la fonctionnalité "Actions" [#1775](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1775).
