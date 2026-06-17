## Changelog : ami-notifications-api (30 derniers jours, au 19 juin 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur et de l'expérience utilisateur, notamment concernant la gestion des préférences de zone géographique, l'archivage des suivis et l'intégration de FranceConnect. Des travaux ont également été réalisés sur la gestion des notifications et l'administration des utilisateurs, ainsi que sur l'infrastructure et la sécurité.

### Évolutions fonctionnelles
- **Gestion des préférences de zone géographique :** Refonte complète de la gestion des zones géographiques et des préférences utilisateur, incluant la possibilité de sélectionner des zones via une recherche, de gérer les zones de vacances et d'améliorer l'affichage des informations de zone dans l'application.  (#789, #802)
- **Archivage des suivis :** Ajout de la fonctionnalité d'archivage des suivis (follow-up items), permettant de masquer les éléments archivés et de les retrouver facilement.  (#776)
- **Amélioration de la page d'édition d'adresse :** Correction de bugs et amélioration de l'expérience utilisateur sur la page d'édition d'adresse. (#946)
- **Intégration FranceConnect :** Amélioration de l'intégration avec FranceConnect, notamment pour l'authentification et la gestion des sessions. (#708, #917)
- **Gestion des utilisateurs (administration) :** Développement de nouvelles fonctionnalités pour l'administration des utilisateurs, incluant la recherche, la consultation des détails et la suppression d'utilisateurs. (#774)
- **Notifications :** Amélioration de la gestion des notifications, notamment en excluant les notifications avec une date de validité dépassée. (#674)
- **Notifications - Lien vers la page de suivi :** Mise à jour du lien des notifications pour rediriger vers la page de suivi correspondante. (#794)
- **Bouton "Gérer" des notifications :** Amélioration de la mise en page du bouton "Gérer" dans l'écran des notifications. (#874)

### Évolutions techniques
- **Refactoring de l'authentification :** Factorisation et amélioration du code lié à l'authentification, notamment pour l'intégration de FranceConnect. (#917)
- **Réplication de la base de données :** Amélioration de la réplication de la base de données pour une meilleure performance et fiabilité. (#904)
- **Suppression de code obsolète :** Suppression de fonctionnalités et de code obsolètes, notamment le flag "requests enabled". (#823)
- **Amélioration de l'architecture de l'interface utilisateur :** Introduction d'un nouveau composant `PageWrapper` pour améliorer la structure et la cohérence de l'interface utilisateur. (#801)
- **Mise à jour des dépendances :** Mise à jour de plusieurs dépendances, notamment `vitest`, `uv`, `svelte`, `idna` et `ujson`. (Ces mises à jour de routine ne sont pas toutes listées individuellement)
- **Gestion des variables d'environnement :** Amélioration de la gestion des variables d'environnement, notamment pour l'environnement de développement local. (#905)
- **Audit :** Ajout d'entrées d'audit pour les actions de consultation et de suppression d'utilisateurs. (#774)

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements apportés.
- **Tests :** Ajout et mise à jour de tests unitaires et d'intégration.
- **Matomo :** Ajout du suivi des zones de vacances sur Matomo pour une meilleure analyse de l'utilisation. (#750)
- **Nettoyage de code :** Diverses corrections et améliorations du code pour une meilleure lisibilité et maintenabilité.
- **Correction de bugs :** Correction de plusieurs bugs mineurs dans l'interface utilisateur et le code serveur.
