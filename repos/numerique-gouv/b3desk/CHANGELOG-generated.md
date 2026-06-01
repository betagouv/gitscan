## Changelog : b3desk (30 derniers jours, au 30 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la délégation de réunions et à la gestion des informations utilisateur via l'intégration des claims OIDC. Des corrections et des améliorations de la documentation ont également été apportées. L'automatisation de la publication des releases sur GitHub a été implémentée.

### Évolutions fonctionnelles
- **Délégation de réunions :** Amélioration de la fonctionnalité de délégation de réunions via l'API. [#357](https://github.com/numerique-gouv/b3desk/issues/357)
- **Informations utilisateur :**  Possibilité de mapper les claims OIDC pour récupérer et afficher des informations utilisateur plus complètes. [#360](https://github.com/numerique-gouv/b3desk/issues/360)
- **Affichage du nom complet du propriétaire :** Correction de l'affichage du nom complet du propriétaire d'une réunion.
- **Traduction :** Mise à jour des traductions via Weblate. [#344](https://github.com/numerique-gouv/b3desk/issues/344)

### Évolutions techniques
- **Publication des releases :** Automatisation de la publication des releases GitHub lors de la création de tags.
- **Linting :** Ajout de vérifications lint supplémentaires pour améliorer la qualité du code.
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (uv, idna, authlib, urllib3, mako) pour bénéficier des dernières corrections et améliorations de sécurité. (Ces mises à jour sont gérées automatiquement par Dependabot et ne sont pas détaillées individuellement).
- **Configuration de développement :** Redirection automatique vers `b3desk.localhost` en mode développement.

### Autres changements
- **Documentation :** Ajout d'un exemple de personnalisation du scope OIDC. [#339](https://github.com/numerique-gouv/b3desk/issues/339)
- **Amélioration de la délégation de réunions :** Amélioration de la délégation de réunions. [#322](https://github.com/numerique-gouv/b3desk/issues/322)
