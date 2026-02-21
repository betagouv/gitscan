## Changelog : transport-site (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées au site transport au cours du dernier mois. Les efforts se sont concentrés sur l'amélioration du support du format de données NeTEx, l'amélioration de la recherche de jeux de données, et l'amélioration de la consolidation des données IRVE. Des corrections et des optimisations diverses ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Amélioration de la recherche de jeux de données avec la possibilité de filtrer par sous-type (#5303).
- Ajout d'un menu de navigation sur la page de détails des ressources (#5311).
- Affichage des dates de validité des données NeTEx dans les cartouches (#5331).
- Ajout d'un indicateur "Périmé" sur les cartouches GTFS Flex (#5332).
- Notification des ressources NeTEx expirées (#5336).
- Remontée d'informations supplémentaires dans le cadre de la consolidation IRVE (#5321).
- Ajout d'un rapport opérationnel global et détaillé (#5285).
- Ajout de la possibilité d'ajouter des sous-types de catégories de données dans le backoffice (#5283).

### Évolutions techniques
- Amélioration de la robustesse du parseur NeTEx pour gérer les dossiers (#5355).
- Extraction des métadonnées NeTEx lors de la validation pour faciliter leur utilisation (#5323).
- Divers refactorings et corrections dans le code NeTEx (#5338).
- Amélioration des extracteurs NeTEx suite à des tests (#5320).
- Optimisation de la recherche en mémoire pour les jeux de données (#5345, #5340, #5333).
- Mise en cache sur disque et vérification ETag pour le proxy Unlock S3 (#5264).
- Correction de la sérialisation des sous-types de données (#5307).
- Suppression de code mort dans le DatasetController (#5329).
- Correction de la valeur de configuration `jsonschema_validator_impl` (#5284).

### Autres changements
- Nettoyage de warnings de compilation (#5344).
- Actualisation de la configuration ZFE (#5348).
- Suppression d'une fonctionnalité de recherche par sous-type de données qui causait des problèmes (#5324).
- Nettoyage routinier du code (#5322).
- Page de nouveautés mise à jour pour janvier 2026 (#5304).
- Correction d'un problème avec le tag de début dans le feed Atom (#5308).
- Amélioration de la gestion des points de contact lors de l'import de jeux de données (#5288, #5287).
- Ajout de statistiques sur le nombre de ressources (#5277).
- Correction de la gestion des tabulations dans les fichiers IRVE (#5281).
- Log du début du job de consolidation IRVE (#5286).
- Export de la base de données IRVE (#5255).
- Correction d'un bug dans le fil d'ariane de l'espace producteur (#5299).
- Suppression d'un tag saisonnier inutile (#5297).
- Modification de l'heure d'exécution de la consolidation IRVE (#5300).
