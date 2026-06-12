## Changelog : hyyypertool (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, hyyypertool a bénéficié d'améliorations significatives en termes de gestion des utilisateurs, notamment l'ajout de l'historique de connexion OIDC, ainsi que des optimisations techniques et de sécurité. L'interface utilisateur a également été enrichie avec des badges d'informations sur les organisations et des améliorations de l'affichage des modérations.

### Évolutions fonctionnelles
- Ajout de la pagination de l'historique de connexion OIDC sur la page utilisateur pour une meilleure lisibilité. [#1678](https://github.com/proconnect-gouv/hyyypertool/issues/1678)
- Affichage de l'historique de connexion aux services ProConnect directement sur la fiche utilisateur. [#1673](https://github.com/proconnect-gouv/hyyypertool/issues/1673)
- Ajout de badges d'informations synthétiques (type de service, statut, activité, etc.) dans les fiches organisation. [#1672](https://github.com/proconnect-gouv/hyyypertool/issues/1672)
- Possibilité de spécifier une raison de refus lors de la suppression d'un utilisateur. [#1652](https://github.com/proconnect-gouv/hyyypertool/issues/1652)
- Lien direct vers le profil utilisateur depuis l'adresse e-mail affichée. [#1653](https://github.com/proconnect-gouv/hyyypertool/issues/1653)
- Amélioration de l'affichage des modérations avec la possibilité de trier les colonnes. [#1604](https://github.com/proconnect-gouv/hyyypertool/issues/1604) et [#1620](https://github.com/proconnect-gouv/hyyypertool/issues/1620)

### Évolutions techniques
- Remplacement des modals SSR par des "Preact islands" auto-contenues pour les modérations, améliorant potentiellement les performances et la maintenabilité. [#1627](https://github.com/proconnect-gouv/hyyypertool/issues/1627)
- Implémentation d'une limitation de débit (rate limiting) basée sur l'adresse IP pour renforcer la sécurité. [#1621](https://github.com/proconnect-gouv/hyyypertool/issues/1621)
- Remplacement des mocks de certains services externes par des routes de développement locales pour faciliter les tests et le développement. [#1607](https://github.com/proconnect-gouv/hyyypertool/issues/1607), [#1608](https://github.com/proconnect-gouv/hyyypertool/issues/1608), [#1609](https://github.com/proconnect-gouv/hyyypertool/issues/1609)
- Mise à jour de plusieurs dépendances pour bénéficier des dernières corrections et améliorations.

### Autres changements
- Correction d'une faute de frappe dans un e-mail automatisé. [#1654](https://github.com/proconnect-gouv/hyyypertool/issues/1654)
- Amélioration de la gestion des nonces pour la sécurité des îles Preact. [#1605](https://github.com/proconnect-gouv/hyyypertool/issues/1605)
- Mise à jour de la dépendance `@proconnect-gouv/proconnect.identite`. [#1651](https://github.com/proconnect-gouv/hyyypertool/issues/1651)
