## Changelog : aplypro (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations à la gestion des données FREGATA, notamment la correction de conflits et l'ajout d'attributs manquants. Des améliorations ont également été apportées à la recherche, aux rapports de paiement et à la gestion des dates de scolarité. Enfin, des tests unitaires ont été ajoutés pour renforcer la qualité du code.

### Évolutions fonctionnelles
- Correction d'un conflit dans le mapper FREGATA entre le code 'division' et 'statutApprenant' [#1998](https://github.com/betagouv/aplypro/issues/1998) et [#e363042](https://github.com/betagouv/aplypro/commit/e363042).
- Ajout d'attributs manquants dans le mapper des scolarités FREGATA [#1997](https://github.com/betagouv/aplypro/issues/1997) et [#4685fa6](https://github.com/betagouv/aplypro/commit/4685fa6).
- Ajout d'une ventilation par BOP (Base d'Orientation Pédagogique) aux rapports de données [#1992](https://github.com/betagouv/aplypro/issues/1992).
- Modification du message affiché pour les demandes de paiement envoyées [#1994](https://github.com/betagouv/aplypro/issues/1994) et [#3c1c42c](https://github.com/betagouv/aplypro/commit/3c1c42c).
- Correction des en-têtes des résultats de recherche [#1988](https://github.com/betagouv/aplypro/issues/1988).
- Suppression du blocage de l'envoi des paiements négatifs [#1985](https://github.com/betagouv/aplypro/issues/1985).
- Blocage de la création de scolarités débutant après la date du jour [#1966](https://github.com/betagouv/aplypro/issues/1966).
- Gestion d'une date de début de scolarité absente dans la méthode `within_schooling_dates?` [#1986](https://github.com/betagouv/aplypro/issues/1986).

### Évolutions techniques
- Mise à jour de la syntaxe du fichier `docker-compose` [#d4cf3a6](https://github.com/betagouv/aplypro/commit/d4cf3a6).
- Ajout de tests unitaires [#d00ea25](https://github.com/betagouv/aplypro/commit/d00ea25), [#2ae887e](https://github.com/betagouv/aplypro/commit/2ae887e), [#01358a8](https://github.com/betagouv/aplypro/commit/01358a8).
- Refactoring de la structure des pages HTML [#4c6997d](https://github.com/betagouv/aplypro/commit/4c6997d).
- Suppression de la méthode `check_negative_rectification!` [#1995](https://github.com/betagouv/aplypro/issues/1995).
- Correction d'une injection UAI [#1f4efb0](https://github.com/betagouv/aplypro/commit/1f4efb0).

### Autres changements
- Ajout de nouvelles données au seeder [#e5e65e5](https://github.com/betagouv/aplypro/commit/e5e65e5).
- Mise à jour du seeder des rapports [#29ebd00](https://github.com/betagouv/aplypro/commit/29ebd00).
- Bump de version à 2.10.4 [#1987](https://github.com/betagouv/aplypro/issues/1987) et [#3d15375](https://github.com/betagouv/aplypro/commit/3d15375).
- Bump de version [#fd58364](https://github.com/betagouv/aplypro/commit/fd58364) et [#08bed71](https://github.com/betagouv/aplypro/commit/08bed71).
- Ajout d'une méthode d'inspection des données XML envoyées [#fc232cd](https://github.com/betagouv/aplypro/commit/fc232cd).
