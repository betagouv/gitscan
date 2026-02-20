## Changelog : jeveuxaider-back (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au backend de la plateforme "Je veux aider" au cours des 30 derniers jours. Les évolutions concernent principalement l'amélioration des notifications, l'optimisation des requêtes de données et la correction de bugs pour une meilleure expérience utilisateur et une plus grande stabilité de la plateforme. De nouvelles fonctionnalités ont également été ajoutées, notamment concernant les statistiques des missions et la gestion des missions ouvertes aux mineurs.

### Évolutions fonctionnelles
- Ajout d'un champ `is_open_to_minors` dans les templates de missions pour indiquer si une mission est ouverte aux mineurs (#123).
- Amélioration des notifications Slack avec des composants Block Kit pour une présentation plus claire et structurée (#126).
- Ajout d'un endpoint `fevrierPourProteger` pour les statistiques des missions de février (#120).
- Correction d'un bug dans l'écoute des messages de notification pour garantir que les utilisateurs reçoivent les notifications attendues (#127).
- Mise en place d'un redémarrage du scheduler de l'application frontale (#128).
- Amélioration des messages de notification pour les missions suggérées et aimées (#121, #122).

### Évolutions techniques
- Refactorisation des notifications Slack avec l'introduction d'un Trait `HasSlackNotification` pour une meilleure organisation et réutilisabilité du code (#125).
- Optimisation des requêtes pour le tableau de bord des statistiques, notamment pour les organisations et missions actives (#120).
- Amélioration de la gestion des dates et des requêtes de missions dans le contrôleur des statistiques publiques (#120).
- Optimisation de la méthode `overviewPlaces` dans le contrôleur `NumbersController` et nettoyage du code inutilisé (#120).
- Correction de la logique de filtrage des participations dans le contrôleur `UserController` pour utiliser une correspondance exacte (#121).
- Refactorisation du contrôleur `EngagementController` et `MarketplaceMissionController` pour supprimer des méthodes inutilisées et mettre à jour la logique de notification (#123).
- Correction de l'adresse de l'API Adresse et mise à jour de la documentation (#124).
- Mise à jour de PHPUnit et de ses dépendances (#125).

### Autres changements
- Modification du canal Slack pour les événements d'exportation et d'importation de données vers `#produit-logs` (#126).
- Mise à jour de l'adresse e-mail du destinataire des notifications du réseau de Nivine à Augusta (#127).
- Correction de filtres de chaînes de caractères par des filtres exacts dans le contrôleur `ActivityLogController` (#128).
- Correction d'une erreur de temps de verbe dans un message de notification (#129).
- Suppression de certaines configurations Slack dans les notifications (#130, #131, #132).
- Mise à jour de la dépendance `psy/psysh` de 0.12.18 à 0.12.19 (#133).
