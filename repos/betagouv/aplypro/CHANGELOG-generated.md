## Changelog : aplypro (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives au reporting, notamment avec l'ajout d'une ventilation par BOP. Des corrections ont été apportées à la gestion des dates de scolarité et des paiements, ainsi que des ajustements pour améliorer la robustesse et la clarté de l'application.

### Évolutions fonctionnelles
- Ajout de la ventilation par BOP dans les rapports de données [#1992](https://github.com/betagouv/aplypro/issues/1992).
- Modification du message affiché lors de l'envoi des demandes de paiement, pour une meilleure clarté [#1994](https://github.com/betagouv/aplypro/issues/1994) et [#3c1c42c](https://github.com/betagouv/aplypro/commit/3c1c42c).
- Suppression du blocage de l'envoi des paiements négatifs [#1985](https://github.com/betagouv/aplypro/issues/1985).
- Blocage de la création de scolarités dont la date de début est postérieure à la date du jour [#1966](https://github.com/betagouv/aplypro/issues/1966).
- Correction de l'affichage des en-têtes des résultats de recherche [#1988](https://github.com/betagouv/aplypro/issues/1988).
- Ajout des attributs manquants dans le mapper des scolarités FREGATA [#1997](https://github.com/betagouv/aplypro/issues/1997) et [#4685fa6](https://github.com/betagouv/aplypro/commit/4685fa6).

### Évolutions techniques
- Mise à jour de la syntaxe du fichier `docker-compose.yml`.
- Amélioration de la gestion du cache des données RNVP [#1980](https://github.com/betagouv/aplypro/issues/1980).
- Refactorisation de la structure des pages HTML.
- Ajout de tests unitaires.
- Gestion améliorée des dates de début de scolarité absentes dans la logique `within_schooling_dates?` [#1986](https://github.com/betagouv/aplypro/issues/1986).
- Suppression d'un test Cucumber obsolète.
- Suppression d'une méthode inutile `check_negative_rectification!` [#1995](https://github.com/betagouv/aplypro/issues/1995).

### Autres changements
- Mise à jour de la version de l'application à 2.10.4 [#1987](https://github.com/betagouv/aplypro/issues/1987).
- Mise à jour des dépendances via `bundle update`.
- Ajout de nouvelles données au seeder.
- Correction d'une injection UAI.
