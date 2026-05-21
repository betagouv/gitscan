## Changelog : b3desk (30 derniers jours, au 20 mai 2026)

### Résumé
Cette version apporte des améliorations à la délégation de réunions, notamment l'affichage du nom complet du propriétaire. Une correction importante a été apportée au système de traductions, résolvant des problèmes potentiels d'affichage. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Amélioration de la délégation de réunions : le nom complet du propriétaire est maintenant affiché. [#339](https://github.com/numerique-gouv/b3desk/pull/339)
- Correction du système de traductions, permettant un affichage correct des textes dans différentes langues. [#308](https://github.com/numerique-gouv/b3desk/issues/308)
- Affichage du nom complet du propriétaire d'une réunion. [#344](https://github.com/numerique-gouv/b3desk/issues/344)

### Évolutions techniques
- Mise à jour de la version principale vers 1.6.2dev.
- Mises à jour de plusieurs dépendances :
    - `idna` de 3.11 à 3.15
    - `authlib` de 1.6.11 à 1.6.12
    - `urllib3` de 2.6.3 à 2.7.0
    - `mako` de 1.3.11 à 1.3.12
    - `lxml` de 6.0.2 à 6.1.0
    - `python-dotenv` de 1.2.1 à 1.2.2

### Autres changements
- Mise à jour des traductions.
- Intégration des traductions via Weblate.
