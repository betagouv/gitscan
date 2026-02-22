## Changelog : jeveuxaider-back (30 derniers jours)

### Résumé
Ce changelog fait le point sur les améliorations apportées au backend de la plateforme "Je veux aider" au cours du dernier mois. Les évolutions concernent principalement l'amélioration des statistiques, la gestion des notifications, la correction de bugs et l'ajout de nouvelles fonctionnalités liées aux missions et aux témoignages.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité permettant de revoir les témoignages (#130).
- Ajout d'un champ `is_open_to_minors` dans les templates de missions, avec la logique correspondante (#123).
- Amélioration de l'affichage des statistiques publiques, notamment pour les organisations et les missions actives.
- Ajout d'un endpoint spécifique pour les statistiques des missions "février pour protéger" (#120).
- Amélioration de la gestion des référents et responsables (#119).
- Redirection de l'email de notification du réseau vers Augusta (#13cb691).

### Évolutions techniques
- Refactorisation des notifications Slack avec l'introduction d'un trait `HasSlackNotification` (#125) pour une meilleure organisation et réutilisation du code.
- Optimisation des requêtes pour le tableau de bord des statistiques (#120).
- Amélioration de la gestion des dates et des requêtes liées aux missions dans le contrôleur des statistiques publiques (#120).
- Simplification des requêtes dans le contrôleur des missions en supprimant des relations inutiles (#122).
- Optimisation de la méthode `overviewPlaces` dans le contrôleur des statistiques (#1d1f9b0).
- Correction de filtres dans le contrôleur `ActivityLogController` pour une recherche plus précise (#124).
- Correction de la logique de filtrage des participations dans le contrôleur `UserController` (#d6a241a).
- Correction d'une erreur de temps de verbe dans la notification `MissionSuggestEnhanceText` (#476c086).
- Mise à jour de PHPUnit et de ses dépendances (#120).

### Autres changements
- Correction d'un bug dans l'écouteur des messages email avec la prise en compte de `canBeNotified` (#127).
- Amélioration des notifications Slack avec l'utilisation de composants Block Kit (#126).
- Suppression de l'assignation du canal Slack dans plusieurs classes de notifications (#4b96c15, #f477479).
- Suppression de méthodes inutilisées et mise à jour de la logique de notification dans certains contrôleurs (#e38d76b).
- Correction d'un bug dans le filtre de missions recommandées (#a050316).
- Mise à jour de la librairie `psy/psysh` (#121).
- Nettoyage de code et commentaires inutiles dans divers contrôleurs.
- Correction de la durée du filtre des missions envoyées (#a050316).
