## Changelog : standards-front (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'API et l'expérience utilisateur. L'API a été enrichie pour fournir un résumé des données, et des corrections ont été apportées pour améliorer la stabilité et la clarté des informations affichées. Des mises à jour de dépendances et de la version de Ruby ont également été effectuées pour maintenir la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- L'API `/summary` fournit désormais un véritable résumé des données.
- Possibilité de mettre à jour les standards via l'application [#181](https://github.com/betagouv/standards-front/pull/181).
- Amélioration de l'affichage des versions des standards : les versions "N/A" ne sont plus affichées aux utilisateurs.
- Suppression de la bannière beta dans l'en-tête.
- Correction de l'affichage des messages flash.

### Évolutions techniques
- Mise à jour de la version de Ruby à 4.0.5.
- Mise à jour des gems `dsfr-view-components` et `omniauth-proconnect`.
- Documentation de la modification de l'API `/summary`.

### Autres changements
- Correction de bugs mineurs et améliorations de la stabilité.
- Mises à jour de dépendances diverses.
