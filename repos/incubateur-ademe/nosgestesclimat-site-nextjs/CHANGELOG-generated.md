## Changelog : nosgestesclimat-site-nextjs (30 derniers jours)

### Résumé
Ce mois-ci, le site nosgestesclimat a bénéficié d'améliorations significatives en termes d'expérience utilisateur, notamment dans la gestion des comptes utilisateurs (création pour les organisations, gestion des abonnements à la newsletter) et dans la présentation des résultats du calcul d'empreinte carbone. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance du site.

### Évolutions fonctionnelles
- Possibilité de créer un compte pour les membres d'une organisation ou d'un groupe [#1639](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1639).
- Nouvelle page de gestion des abonnements à la newsletter [#1598](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1598).
- Amélioration de la présentation des résultats, avec un détail par catégories [#1641](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1641) et une nouvelle section d'objectifs.
- Ajout d'un bloc pour sauvegarder les simulations [#1653](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1653).
- Mise à jour du texte sur la page de connexion des organisations (NGC-3021) [#1667](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1667).
- Mise à jour du titre de la page des organisations pour inclure les animateurs (NGC-3022) [#1668](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1668).
- Suppression de la fonctionnalité de reprise de test [#1606](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1606).
- Ajout de suivi (tracking) pour les clics de renvoi du code de vérification [#1629](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1629).

### Évolutions techniques
- Mise à jour du modèle d'empreinte carbone vers la version 4.9.1 et 4.9.0 [#1664](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1664) et [#1652](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1652).
- Mise à jour de la librairie PostHog et configuration améliorée [#1660](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1660) et [#1662](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1662).
- Correction d'un problème de crash de l'application Scalingo dû à une dépendance TypeScript [#1651](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1651).
- Amélioration de la configuration des tests E2E avec la variable d'environnement `COOKIE_NAME` [#1666](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1666).
- Suppression du bloc d'email Microsoft pour l'authentification.
- Correction d'un bug empêchant l'affichage correct des résultats pour les simulations sans données d'empreinte hydrique [#1643](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1643).
- Suppression du code mort avec knip.js [#1615](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1615).

### Autres changements
- Mise à jour de la bannière de cookie [#1630](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1630).
- Correction de l'affichage du HTML brut sur les pages thématiques [#1648](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1648).
- Correction du problème de désélection [#1646](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1646).
- Correction de l'état d'acceptation des cookies GTM pour les utilisateurs de retour [#1682](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1682).
- Suppression du hreflang pour les pages Strapi en français uniquement [#1680](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1680).
- Mise à jour du chemin du service worker mock [#1678](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1678).
- Correction d'une faute de frappe dans un script [#1677](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1677).
- Amélioration de l'angle et de la longueur de la flèche sur la page de fin [#1671](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1671).
- Correction de la majuscule sur "Mon Espace" et "My Space" [#1636](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1636).
- Possibilité de désactiver la capture d'erreur Sentry [#1634](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1634).
- Publication des versions 2.51.0, 2.52.0 et 2.53.0 [#1637](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1637), [#1645](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1645) et [#1659](https://github.com/incubateur-ademe/nosgestesclimat-site-nextjs/issues/1659).
