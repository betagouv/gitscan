## Changelog : transport-site (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion et de la validation des données NeTEx et GTFS, ainsi que sur l'enrichissement des fonctionnalités de recherche et de consolidation des données IRVE. Des améliorations de performance et de maintenance ont également été apportées, notamment au niveau du proxy Unlock S3 et de l'interface utilisateur.

### Évolutions fonctionnelles
- **Recherche :** Possibilité de rechercher des jeux de données par sous-type (#5303). Cette fonctionnalité a été temporairement revertée puis réintégrée avec des corrections (#5324).
- **NeTEx :** Amélioration de la robustesse du parseur NeTEx pour gérer les dossiers (#5355).
- **NeTEx :** Ajout de l'affichage des métadonnées associées aux données NeTEx (#5339).
- **NeTEx :** Ajout d'un indicateur pour signaler les dates de validité manquantes (#5337) et la notification des ressources expirées (#5336).
- **NeTEx :** Extraction des métadonnées NeTEx lors de la validation des données (#5323).
- **GTFS Flex :** Ajout d'un indicateur "Périmé" sur la cartouche des données GTFS Flex (#5332).
- **IRVE :** Amélioration de la consolidation des données IRVE, avec remontée d'informations supplémentaires (#5321) et identification des datasets présents sur data.gouv.fr mais absents du système (#5276).
- **Interface utilisateur :** Ajout d'un menu de navigation sur la page de détails des ressources (#5311).
- **Espace producteur :** Mise à jour du fil d'ariane (#5299).
- **Backoffice :** Ajout d'un champ pour le sous-type de catégorie de données (#5283).
- **Rapport opérationnel :** Ajout d'un rapport opérationnel avec un suivi global et détaillé (#5285).

### Évolutions techniques
- **Proxy Unlock S3 :** Mise en place d'un cache sur disque et vérification de l'ETag pour améliorer les performances (#5264).
- **Consolidation IRVE :** Modification de l'heure d'exécution du job de consolidation IRVE (#5300).
- **Refactoring :** Divers refactorings et corrections dans le code NeTEx (#5338).
- **Configuration :** Actualisation de la configuration ZFE (#5348).
- **Tests :** Améliorations des extracteurs NeTEx suite à des tests (#5320).
- **Base de données :** Correction d'un problème de sérialisation des sous-types de données (#5307) et suppression de code mort dans le DatasetController (#5329).
- **Authentification :** Désactivation du log de requêtes dans le plug TokenAuth pour Unlock (#5314).

### Autres changements
- Suppression des pdc avec id_pdc_itinerance "non concerné" de la consolidation IRVE dédoublonnée (#5360).
- Correction d'une URL de ressource mal encodée (#5363).
- Renommage du rapport de consolidation IRVE (#5359).
- Nettoyage de warnings de compilation (#5344).
- Nettoyage routinier du code (#5322).
- Correction de bugs mineurs et améliorations de la maintenance générale.
- Correction d'un tag de début dans le feed Atom (#5308).
- Correction d'un problème avec la population des order_datasets (#5328).
- Suppression d'un tag saisonnier inutile (#5297).
- Amélioration de la gestion des emails nil dans l'import des points de contact (#5288).
- Ajout du comptage du nombre de ressources dans StatsHandler (#5277).
- Modification de la gestion des contact_points pour qu'ils soient une liste (#5287).
- Ajout de logs au début du job de consolidation IRVE (#5286).
