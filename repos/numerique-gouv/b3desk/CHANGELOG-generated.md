## Changelog : b3desk (30 derniers jours, au 13 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion de la délégation de réunions, notamment en affichant clairement le propriétaire initial et en permettant la suppression correcte des réunions déléguées. Des corrections ont également été apportées au système de traductions et à l'affichage du nom complet du propriétaire. Des mises à jour de dépendances ont été intégrées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- **Gestion de la délégation de réunions :** Amélioration de l'affichage du bouton de gestion de la délégation en fonction de la présence de délégués [#339](https://github.com/numerique-gouv/b3desk/pull/339).
- **Affichage du propriétaire :** Affichage du nom complet du propriétaire d'une réunion [#339](https://github.com/numerique-gouv/b3desk/pull/339).
- **Suppression des réunions déléguées :** Correction d'un bug empêchant la suppression des réunions ayant des délégués [#339](https://github.com/numerique-gouv/b3desk/pull/339).
- **Traduction :** Correction du système de traductions [#308](https://github.com/numerique-gouv/b3desk/issues/308).

### Évolutions techniques
- **Tests :** Ajout de tests relatifs aux améliorations de la délégation de réunions.
- **Mises à jour de dépendances :**
    - Authlib mis à jour de 1.6.9 à 1.6.12.
    - Mako mis à jour de 1.3.10 à 1.3.12.
    - Urllib3 mis à jour de 2.6.3 à 2.7.0.
    - Lxml mis à jour de 6.0.2 à 6.1.0.
    - Python-dotenv mis à jour de 1.2.1 à 1.2.2.

### Autres changements
- Mise à jour de la traduction anglaise via Weblate [#344](https://github.com/numerique-gouv/b3desk/pull/344).
- Mise à jour de la version principale à 1.6.2dev.
- Mise à jour des traductions.
