## Changelog : b3desk (30 derniers jours, au 5 juin 2026)

### Résumé
Les dernières mises à jour de b3desk se concentrent sur l'amélioration de la gestion des délégations de réunions et l'intégration des informations utilisateur via OIDC. Des corrections et améliorations diverses ont également été apportées pour une meilleure expérience utilisateur et une plus grande stabilité.

### Évolutions fonctionnelles
- **Délégation de réunions :** Possibilité d'ajouter des délégués à une réunion via l'API. [#357](https://github.com/numerique-gouv/b3desk/issues/357)
- **Délégation de réunions :** Amélioration de la gestion des délégations de réunions, incluant la limitation du nombre de délégués à 15 et l'impossibilité pour le propriétaire de la réunion de se déléguer lui-même. [#364](https://github.com/numerique-gouv/b3desk/issues/364)
- **Informations utilisateur :** Intégration des informations utilisateur provenant des revendications OIDC (OpenID Connect). [#360](https://github.com/numerique-gouv/b3desk/issues/360)
- **Affichage du nom complet :** Correction de l'affichage du nom complet du propriétaire de la réunion.
- **Redirection en mode développement :** Redirection automatique vers `b3desk.localhost` en mode développement pour une meilleure expérience.

### Évolutions techniques
- **Publication des releases :** Automatisation de la publication des releases GitHub lors de la création de tags.
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances, notamment `webob`, `uv`, `idna`, `authlib` et `urllib3`.
- **Linting :** Ajout de vérifications lint supplémentaires pour améliorer la qualité du code.
- **Documentation :** Ajout d'un exemple de personnalisation du scope OIDC.

### Autres changements
- Mise à jour des traductions.
- Préparation des versions de développement 1.6.2dev, 1.6.3dev et 1.6.4dev.
