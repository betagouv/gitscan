## Changelog : aplypro (30 derniers jours, au 19 juin 2026)

### Résumé
Cette version apporte des améliorations à la gestion des dates de scolarité, notamment pour bloquer la création de scolarités futures et gérer les cas où la date de début est manquante. Des corrections de bugs ont été implémentées concernant l'affichage des dates et le cache des données RNVP.  Une nouvelle fonctionnalité permet l'envoi de l'adresse redressée à l'ASP dès qu'un élève a une PFMP "rectifiée".

### Évolutions fonctionnelles
- Correction d'un bug d'affichage concernant la date de fin de scolarité manquante [#1972](https://github.com/betagouv/aplypro/issues/1972).
- Affichage des dates de début et de fin de scolarité dans l'espace académique [#1970](https://github.com/betagouv/aplypro/issues/1970) et [#035987b](https://github.com/betagouv/aplypro/commit/035987b).
- Envoi de l'adresse redressée à l'ASP dès qu'un élève a au moins une PFMP "rectifiée" [#1942](https://github.com/betagouv/aplypro/issues/1942).
- Blocage de la création de scolarités débutant après la date du jour [#1966](https://github.com/betagouv/aplypro/issues/1966).
- Suppression du blocage de l'envoi des paiements négatifs [#1985](https://github.com/betagouv/aplypro/issues/1985) et [#8c29b20](https://github.com/betagouv/aplypro/commit/8c29b20).

### Évolutions techniques
- Correction du cache des données RNVP [#1980](https://github.com/betagouv/aplypro/issues/1980).
- Refactorisation pour introduire la méthode `future_start_date?` [#72958e3](https://github.com/betagouv/aplypro/commit/72958e3).
- Gestion des cas où `rnvp_data` est vide [#1974](https://github.com/betagouv/aplypro/issues/1974) (réverté puis corrigé).
- Renommage de `start_date` en `sc_start_date`.

### Autres changements
- Correction des en-têtes des résultats de recherche [#1988](https://github.com/betagouv/aplypro/issues/1988).
- Mise à jour de la version à 2.10.3 et 2.10.4 [#1987](https://github.com/betagouv/aplypro/issues/1987).
- Suppression d'un test Cucumber obsolète.
