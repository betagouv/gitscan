## Changelog : aplypro (30 derniers jours, au 10 juillet 2026)

### Résumé
Les dernières mises à jour d'APLyPro se concentrent sur l'amélioration de la gestion des données FREGATA, notamment la résolution de conflits et l'ajout d'attributs manquants. Des améliorations ont également été apportées à la gestion des paiements, avec la suppression de blocages concernant les paiements négatifs et la création de scolarités. Enfin, des corrections et des refactorings ont été effectués sur l'interface utilisateur et le code.

### Évolutions fonctionnelles
- Amélioration de la ventilation des données dans les rapports, avec l'ajout de données par BOP. [#1992](https://github.com/betagouv/aplypro/issues/1992)
- Modification du message affiché lors de l'envoi des demandes de paiement, pour une meilleure clarté. [#1994](https://github.com/betagouv/aplypro/issues/1994) et [#1985](https://github.com/betagouv/aplypro/issues/1985)
- Suppression du blocage de l'envoi des paiements négatifs, offrant plus de flexibilité dans la gestion des paiements. [#1985](https://github.com/betagouv/aplypro/issues/1985)
- Blocage de la création de scolarités débutant dans le futur, pour éviter les erreurs de saisie. [#1966](https://github.com/betagouv/aplypro/issues/1966)
- Correction des en-têtes des résultats de recherche pour une meilleure lisibilité. [#1988](https://github.com/betagouv/aplypro/issues/1988)

### Évolutions techniques
- Résolution de conflits dans le mapper FREGATA entre les codes 'division' et 'statutApprenant'. [#1998](https://github.com/betagouv/aplypro/issues/1998) et [#1986](https://github.com/betagouv/aplypro/issues/1986)
- Ajout des attributs manquants dans le mapper des scolarités FREGATA pour une meilleure synchronisation des données. [#1997](https://github.com/betagouv/aplypro/issues/1997) et [#4685fa6](https://github.com/betagouv/aplypro/commit/4685fa6)
- Refactoring de la structure des pages HTML pour une meilleure organisation du code.
- Mise à jour de la syntaxe du fichier `docker-compose.yml`.
- Ajout de tests unitaires pour améliorer la couverture et la robustesse du code.
- Suppression de la méthode `check_negative_rectification!`. [#1995](https://github.com/betagouv/aplypro/issues/1995)
- Renommage de l'attribut `start_date` en `sc_start_date` pour plus de clarté.

### Autres changements
- Mise à jour de la version de l'application à 2.10.4. [#1987](https://github.com/betagouv/aplypro/issues/1987)
- Ajout de nouvelles données au seeder pour les tests et le développement.
- Suppression d'un test Cucumber obsolète.
- Correction d'une injection UAI potentielle. [#1f4efb0](https://github.com/betagouv/aplypro/commit/1f4efb0)
