## Changelog : nosgestesclimat-site-nextjs (30 derniers jours)

### Résumé
Ce mois-ci, le site nosgestesclimat a bénéficié d'améliorations significatives en termes d'expérience utilisateur, notamment dans la présentation des résultats et la gestion des comptes utilisateurs. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité du site, ainsi que des optimisations techniques pour la performance et la sécurité.

### Évolutions fonctionnelles
- Ajout d'une nouvelle section "Objectifs" sur la page des résultats (#1661).
- Création d'un nouveau bloc pour sauvegarder les simulations (#1653).
- Amélioration des composants de détails des résultats par catégories (#1641).
- Possibilité de créer un compte pour les membres de groupes ou d'organisations (#1639).
- Nouvelle page de gestion des abonnements à la newsletter [NGC-2262] (#1598).
- Ajout de l'autocomplétion pour le code de vérification lors de la connexion (#1631).
- Amélioration de la page de connexion des organisations avec la mention des animateurs (#1668).
- Mise à jour du texte sur la page de connexion des organisations (NGC-3021) (#1667).
- Ajout de suivi (tracking) pour les clics sur "Renvoyer le code de vérification" (#1629).
- Ajout de suivi (tracking) pour les événements PostHog (#1654).

### Évolutions techniques
- Mise à jour du modèle nosgestesclimat vers la version 4.9.1 (#1664) et 4.9.0 (#1652).
- Mise à jour du package PostHog et vérification de la configuration (NGC-3034) (#1660).
- Configuration du nom du cookie d'authentification via une variable d'environnement (#1666).
- Suppression du bloc d'authentification Microsoft (#1640).
- Suppression du code mort avec knip.js (#1615).
- Mise à jour des packages `next` et `react` (#1626).
- Correction d'un problème de crash de l'application Scalingo dû à une dépendance TypeScript (#1651).
- Correction d'un problème d'affichage de code HTML brut sur les pages thématiques (#1648).
- Correction d'un bug empêchant la désélection dans l'interface utilisateur (#1646).
- Amélioration de la gestion du "Do Not Track" et des cookies avec PostHog (#1662).
- Suppression de la fonctionnalité de test de reprise (#1606).
- Suppression du score de vie de l'eau (#1650).
- Correction d'un problème de 429 en mettant à jour les sources d'images (#1605).

### Autres changements
- Suppression du hreflang pour les pages Strapi en français uniquement (#1680).
- Mise à jour du chemin du service worker mock (#1678).
- Correction d'une faute de frappe dans un script (#1677).
- Amélioration de l'angle et de la longueur de la flèche sur la page de fin (#1671).
- Mise à jour de la bannière de cookie (#1630).
- Correction du masquage dynamique des boutons de langue (#1649).
- Ajout de checks pour éviter les tests E2E sur les pull requests en brouillon (#1638).
- Correction de problèmes liés aux tests E2E (#1636, #1637).
- Correction d'un bug lié à l'affichage des résultats pour les simulations sans données sur l'empreinte hydrique (#1643).
- Correction de la capitalisation de "Mon Espace" et "My Space" (#1636).
- Ajout d'une option pour désactiver la capture d'erreurs Sentry (#1634).
- Suppression de la fonctionnalité de test de reprise (#1606).
- Mise à jour de la version du site (2.50.5, 2.51.0, 2.52.0, 2.53.0, 2.54.0).
