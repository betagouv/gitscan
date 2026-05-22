## Changelog : hyyypertool (30 derniers jours, au 2026-05-21)

### Résumé
Les dernières mises à jour de Hyyypertool se concentrent sur l'amélioration de la sécurité, de l'expérience utilisateur et de la maintenabilité du code. Des fonctionnalités de limitation de débit par adresse IP ont été ajoutées pour se protéger contre les abus, tandis que le mode sombre a été amélioré et le tri des colonnes a été implémenté dans la liste des modérations. De nombreuses dépendances ont également été mises à jour pour bénéficier des dernières corrections et améliorations.

### Évolutions fonctionnelles
- Ajout de la possibilité de trier les modérations par colonne (date de création, etc.) en cliquant sur les en-têtes. [#1604](https://github.com/proconnect-gouv/hyyypertool/issues/1604) et [#1606](https://github.com/proconnect-gouv/hyyypertool/issues/1606)
- Possibilité de filtrer les modérations par statut de décision (acceptées, rejetées, réouvertes). [#1594](https://github.com/proconnect-gouv/hyyypertool/issues/1594)
- Ajout de la possibilité de supprimer des modèles de réponse. [#1600](https://github.com/proconnect-gouv/hyyypertool/issues/1600)
- Amélioration du mode sombre pour les boutons et la liste déroulante. [#1622](https://github.com/proconnect-gouv/hyyypertool/issues/1622)
- Suppression de l'affichage du prénom et du nom dans les emails de rejet. [#1576](https://github.com/proconnect-gouv/hyyypertool/issues/1576)

### Évolutions techniques
- Implémentation d'une limitation de débit par adresse IP via `RateLimiterPostgres` pour améliorer la sécurité. [#1621](https://github.com/proconnect-gouv/hyyypertool/issues/1621)
- Configuration du seuil de limitation de débit via la variable d'environnement `RATE_LIMIT_POINTS` (valeur par défaut : 120). [#1626](https://github.com/proconnect-gouv/hyyypertool/issues/1626)
- Remplacement des mocks de certains services externes (api.crisp.chat, agentconnect, support.etalab.gouv.fr) par des routes de développement Hono pour faciliter les tests et le développement local. [#1607](https://github.com/proconnect-gouv/hyyypertool/issues/1607), [#1608](https://github.com/proconnect-gouv/hyyypertool/issues/1608), [#1609](https://github.com/proconnect-gouv/hyyypertool/issues/1609), [#1610](https://github.com/proconnect-gouv/hyyypertool/issues/1610)
- Mise à jour de nombreuses dépendances (Cypress, tailwindcss, sentry, etc.).

### Autres changements
- Amélioration du contraste et de la lisibilité en mode sombre. [#1577](https://github.com/proconnect-gouv/hyyypertool/issues/1577) et [#1578](https://github.com/proconnect-gouv/hyyypertool/issues/1578)
- Corrections de bugs mineurs liés au cache et à la gestion des templates de réponse. [#1601](https://github.com/proconnect-gouv/hyyypertool/issues/1601), [#1602](https://github.com/proconnect-gouv/hyyypertool/issues/1602), [#1603](https://github.com/proconnect-gouv/hyyypertool/issues/1603)
- Améliorations de l'interface utilisateur (UX) et corrections de problèmes d'affichage. [#1595](https://github.com/proconnect-gouv/hyyypertool/issues/1595), [#1596](https://github.com/proconnect-gouv/hyyypertool/issues/1596), [#1597](https://github.com/proconnect-gouv/hyyypertool/issues/1597), [#1598](https://github.com/proconnect-gouv/hyyypertool/issues/1598), [#1599](https://github.com/proconnect-gouv/hyyypertool/issues/1599)
