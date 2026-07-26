## Changelog : vao (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives au processus de premier agrément, notamment pour les DREETS, avec l'ajout de nouvelles étapes, de la gestion des demandes de compléments et de la prise en charge des refus. Des corrections d'accessibilité (RGAA) ont été implémentées sur plusieurs pages, améliorant l'expérience utilisateur pour tous. Des optimisations de performance ont également été réalisées sur la base de données.

### Évolutions fonctionnelles
- Ajout de la prise en charge du premier agrément dans le back-office [#1487](https://github.com/SocialGouv/vao/issues/1487).
- Implémentation du workflow de demande de compléments pour le premier agrément DREETS [#1492](https://github.com/SocialGouv/vao/issues/1492).
- Ajout de la gestion des refus de premier agrément pour les DREETS, incluant l'envoi de notifications par email [#1495](https://github.com/SocialGouv/vao/issues/1495).
- Confirmation de complétude pour le premier agrément DREETS [#1498](https://github.com/SocialGouv/vao/issues/1498).
- Amélioration de la page "Mon agrément" avec la correction d'un problème d'affichage des documents [#1490](https://github.com/SocialGouv/vao/issues/1490).
- Ajout d'une page de bienvenue pour le premier agrément [#1471](https://github.com/SocialGouv/vao/issues/1471).
- Ajout de la gestion des dates dans le formulaire EIG [#1452](https://github.com/SocialGouv/vao/issues/1452).
- Amélioration du workflow d'agrément avec la mise à jour du wording des emails [#1423](https://github.com/SocialGouv/vao/issues/1423).

### Évolutions techniques
- Optimisation des requêtes SQL avec l'ajout d'index pour corriger les timeouts en production [#1489](https://github.com/SocialGouv/vao/issues/1489).
- Correction d'un problème de date invalide dans l'OTP (One-Time Password) [#1450](https://github.com/SocialGouv/vao/issues/1450).

### Autres changements
- Améliorations de l'accessibilité (RGAA) sur les pages de création de compte, de mot de passe oublié, de login, et sur les étapes de renouvellement [#1488](https://github.com/SocialGouv/vao/issues/1488), [#1478](https://github.com/SocialGouv/vao/issues/1478), [#1474](https://github.com/SocialGouv/vao/issues/1474), [#1440](https://github.com/SocialGouv/vao/issues/1440), [#1277](https://github.com/SocialGouv/vao/issues/1277).
- Correction du wording sur la page de refus de validation de compte [#1500](https://github.com/SocialGouv/vao/issues/1500).
- Correction du wording concernant la mention du casier judiciaire français [#1499](https://github.com/SocialGouv/vao/issues/1499).
- Correction de l'étape 4 du renouvellement avec amélioration du bouton de suppression [#1451](https://github.com/SocialGouv/vao/issues/1451).
- Publication de la version 1.28.1 en préproduction [#1462](https://github.com/SocialGouv/vao/issues/1462).
