## Changelog : hyyypertool (30 derniers jours, au 20 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de l'expérience utilisateur, notamment en affichant l'historique de connexion OIDC des utilisateurs et en ajoutant des badges d'informations sur les organisations. Des corrections et des mises à jour techniques ont également été apportées pour améliorer la stabilité et la sécurité de l'outil.

### Évolutions fonctionnelles
- Ajout de la pagination de l'historique de connexion OIDC sur la page utilisateur pour une meilleure lisibilité. [#1678](https://github.com/proconnect-gouv/hyyypertool/issues/1678)
- Affichage de l'historique de connexion aux services ProConnect directement sur la fiche utilisateur. [#1673](https://github.com/proconnect-gouv/hyyypertool/issues/1673)
- Ajout de badges d'informations synthétiques (type de service public, statut, activité, siège social, éligibilité à la vérification) dans les fiches organisation et utilisateur. [#1672](https://github.com/proconnect-gouv/hyyypertool/issues/1672)
- Possibilité de spécifier une raison de refus lors de la gestion des modérations. [#1652](https://github.com/proconnect-gouv/hyyypertool/issues/1652)
- L'email des membres est désormais un lien vers leur profil utilisateur. [#1653](https://github.com/proconnect-gouv/hyyypertool/issues/1653)
- Correction d'une faute de frappe dans l'email automatisé. [#1654](https://github.com/proconnect-gouv/hyyypertool/issues/1654)

### Évolutions techniques
- Remplacement des modals SSR par des "Preact islands" auto-contenues pour améliorer la performance et la maintenabilité. [#1627](https://github.com/proconnect-gouv/hyyypertool/issues/1627)
- Mise à jour de la bibliothèque `@proconnect-gouv/proconnect.identite`. [#1651](https://github.com/proconnect-gouv/hyyypertool/issues/1651) et [#1663](https://github.com/proconnect-gouv/hyyypertool/issues/1663)
- Mise à jour des valeurs ACR (Attestation de Conformité des Risques) pour l'authentification. [#1687](https://github.com/proconnect-gouv/hyyypertool/issues/1687)

### Autres changements
- Mise à jour de diverses dépendances (typescript, hono, sentry, etc.).
- Publication des versions 2026.6.0, 2026.6.1, 2026.6.2, 2026.6.3, 2026.6.4 et 2026.6.5.
