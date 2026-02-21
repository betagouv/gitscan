## Changelog : nosgestesclimat-site-nextjs (30 derniers jours)

### Résumé
Ce mois-ci, le site nosgestesclimat a bénéficié d'une série d'améliorations axées sur la stabilité, la performance et l'expérience utilisateur. Des corrections de bugs ont été apportées, notamment concernant l'authentification, les tests et l'affichage des données. De nouvelles fonctionnalités ont été ajoutées, comme la gestion des abonnements à la newsletter et l'intégration de Calendly pour les demandes de démo. L'équipe a également travaillé sur l'optimisation du site et la suppression de code obsolète.

### Évolutions fonctionnelles
- Amélioration de la page de connexion des organisations avec une formulation plus claire (#1667).
- Mise à jour du titre de la page des organisations pour inclure les animateurs (#1668).
- Remplacement du formulaire Tally par Calendly sur la page "/demander-demo" (#1657).
- Ajout d'une page de gestion des abonnements à la newsletter [NGC-2262] (#1598).
- Correction d'un bug empêchant la désélection d'options dans le questionnaire (#1646).
- Correction d'un bug empêchant l'authentification avec des adresses email Microsoft (#1640, revert puis correction ultérieure).
- Suppression de la fonctionnalité de test "resume" (#1606).
- Ajout de l'autocomplétion au champ de code de vérification (#1631).
- Mise à jour de la bannière de cookies (#1630).
- Correction de l'affichage de code HTML brut sur les pages thématiques (#1648).

### Évolutions techniques
- Mise à jour du modèle nosgestesclimat vers la version 4.9.1 et 4.9.0 (#1664, #1652).
- Mise à jour du package PostHog et configuration associée (#1660).
- Amélioration de la gestion du suivi "Do Not Track" et des cookies avec PostHog (#1662).
- Mise à jour des packages `next` et `react` (#1626).
- Suppression de code mort avec Knip.js (#1615).
- Correction d'un crash de l'application Scalingo dû à une dépendance TypeScript (#1651).
- Ajout d'événements PostHog pour le suivi des actions utilisateurs (#1654).
- Configuration du nom du cookie d'authentification via une variable d'environnement (#1666).
- Ajout de tests E2E avec Cypress (#1556).
- Correction de problèmes liés aux tests E2E et au déploiement en préproduction.
- Suppression de sources d'images provoquant des erreurs 429 (#1605).
- Ajout de redirections (#1603).

### Autres changements
- Publication des versions 2.54.0, 2.53.0, 2.52.0, 2.51.0 et 2.50.5 (#1659, #1645, #1637, #1627, #1622).
- Correction de la capitalisation de "Mon Espace" et "My Space" (#1636).
- Ajout de la possibilité de désactiver la capture d'erreurs Sentry (#1634).
- Ajout de tracking pour les clics sur "Renvoyer le code" (#1629).
- Suppression du blocage des adresses email Microsoft pour l'inscription (#1640, revert puis correction ultérieure).
- Amélioration du sitemap (#1604).
- Correction de bugs liés à l'affichage des résultats pour les simulations sans données sur la consommation d'eau (#1643).
- Ajout de tracking pour les clics sur "Renvoyer le code" (#1629).
- Correction d'un bug lié à l'affichage des propriétés pour les événements suivis côté serveur (#1647).
