## Changelog : aplypro (30 derniers jours, au 19 juin 2026)

### Résumé
Cette version apporte des corrections de bugs et des améliorations concernant la gestion des dates de scolarité, l'envoi des informations à l'ASP, et l'affichage des données dans l'interface utilisateur. Des améliorations ont également été apportées à la gestion des données RNVP et des paiements.

### Évolutions fonctionnelles
- Correction de l'affichage des dates de début et de fin de scolarité dans l'espace académique [#1970](https://github.com/betagouv/aplypro/issues/1970).
- L'adresse redressée est maintenant envoyée à l'ASP dès qu'un élève a au moins une PFMP 'rectifiée' [#1942](https://github.com/betagouv/aplypro/issues/1942).
- Suppression du blocage de l'envoi des paiements négatifs [#1985](https://github.com/betagouv/aplypro/issues/1985) et [#8c29b20](https://github.com/betagouv/aplypro/commit/8c29b20).
- Blocage de la création de scolarités débutant après la date du jour [#1966](https://github.com/betagouv/aplypro/issues/1966) et [#f62d1bb](https://github.com/betagouv/aplypro/commit/f62d1bb).
- Modification des messages affichés pour les demandes de paiement [#1967](https://github.com/betagouv/aplypro/issues/1967).
- Correction d'un bug d'affichage lié à une date de fin de scolarité manquante [#1972](https://github.com/betagouv/aplypro/issues/1972).

### Évolutions techniques
- Amélioration de la gestion et de la mise en cache des données RNVP [#1980](https://github.com/betagouv/aplypro/issues/1980), [#949c3d5](https://github.com/betagouv/aplypro/commit/949c3d5) et [#0c2fd48](https://github.com/betagouv/aplypro/commit/0c2fd48).
- Refactorisation du code pour introduire la méthode `future_start_date?`.
- Gestion améliorée des cas où `rnvp_data` est vide [#1974](https://github.com/betagouv/aplypro/issues/1974).
- Renommage de la variable `start_date` en `sc_start_date`.

### Autres changements
- Correction des en-têtes des résultats de recherche [#1988](https://github.com/betagouv/aplypro/issues/1988).
- Suppression d'un test Cucumber obsolète.
- Mise à jour de la version à 2.10.3 et 2.10.4.
- Application des règles Rubocop pour améliorer la qualité du code.
- Ajout de tests unitaires.
