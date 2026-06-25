## Changelog : aplypro (30 derniers jours, au 19 juin 2026)

### Résumé
Cette version apporte des améliorations à la gestion des dates de scolarité, notamment en empêchant la création de scolarités futures et en affichant correctement les dates dans l'espace académique. Des corrections ont également été apportées à la gestion des données RNVP, à l'envoi des adresses à l'ASP et à l'affichage des messages liés aux demandes de paiement. Enfin, des corrections de bugs et des améliorations de la recherche ont été implémentées.

### Évolutions fonctionnelles
- Correction de l'affichage des dates de début et de fin de scolarité dans l'espace académique. [#1970](https://github.com/betagouv/aplypro/issues/1970)
- Blocage de la création de scolarités débutant après la date du jour. [#1966](https://github.com/betagouv/aplypro/issues/1966)
- Suppression du blocage de l'envoi des paiements négatifs. [#1985](https://github.com/betagouv/aplypro/issues/1985)
- Envoi de l'adresse redressée à l'ASP dès que l'élève a au moins une PFMP 'rectified'. [#1942](https://github.com/betagouv/aplypro/issues/1942)
- Modification des messages affichés pour les demandes de paiement. [#1967](https://github.com/betagouv/aplypro/issues/1967)
- Correction de l'affichage d'une date de fin de scolarité manquante. [#1972](https://github.com/betagouv/aplypro/issues/1972)
- Correction des en-têtes des résultats de recherche. [#1988](https://github.com/betagouv/aplypro/issues/1988)

### Évolutions techniques
- Amélioration de la gestion et de la mise en cache des données RNVP. [#1980](https://github.com/betagouv/aplypro/issues/1980)
- Refactorisation pour introduire la méthode `future_start_date?`.
- Gestion des cas où `rnvp_data` est vide. [#1974](https://github.com/betagouv/aplypro/issues/1974)
- Renommage de la variable `start_date` en `sc_start_date`.
- Suppression d'un test Cucumber obsolète.

### Autres changements
- Mise à jour de la version à 2.10.3 puis 2.10.4.
- Application des règles Rubocop pour améliorer la qualité du code.
- Ajout de tests unitaires.
- Mise à jour des dépendances (bundle).
