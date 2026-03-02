## Changelog : carbure (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à Carbure au cours des 30 derniers jours. Les principales évolutions concernent l'ajout de fonctionnalités pour la gestion du biogaz et du biométhane, notamment l'import de données, la gestion des intrants, et l'amélioration de l'interface utilisateur. Des corrections et optimisations ont également été apportées au module QualiCharge et à l'administration pour les agents de l'administration.

### Évolutions fonctionnelles
- Ajout de la possibilité d'importer des producteurs de biométhane via un fichier Excel. [#1859](https://github.com/MTES-MCT/carbure/issues/1859)
- Amélioration de la gestion des intrants pour le biométhane, avec la correction de doublons dans les fichiers Excel exportés.
- Ajout de la gestion des classifications et des matières premières pour le biométhane.
- Intégration de la gestion des entités DREAL (Directions Régionales de l'Environnement, de l'Aménagement et du Logement) avec la possibilité pour les DREAL d'accepter ou de refuser des utilisateurs.
- Ajout d'un tableau de bord pour les DREAL.
- Ajout de la gestion des retours du ministère de l'Agriculture pour le biométhane.
- Amélioration de l'affichage des quantités en kWh dans le module QualiCharge.
- Ajout d'un formulaire de satisfaction pour les utilisateurs.
- Amélioration de la gestion des données QualiCharge, notamment la correction de requêtes N+1 pour améliorer les performances.
- Ajout de la gestion des transactions UDB (Unknown Data Base) avec la possibilité d'importer l'état des transactions.
- Amélioration de la gestion des certificats d'électricité, notamment l'affichage du solde des certificats disponibles.

### Évolutions techniques
- Refactorisation du modèle Site avec l'utilisation d'héritage pour une meilleure organisation et maintenabilité.
- Simplification et optimisation de certaines requêtes en base de données.
- Mise à jour des migrations pour assurer la compatibilité avec les nouvelles fonctionnalités.
- Amélioration de la gestion des erreurs et des exceptions, notamment pour les requêtes UDB.
- Utilisation de variables d'environnement pour configurer certaines options, comme la taille maximale des fichiers uploadés.
- Correction de bugs et amélioration de la qualité du code.
- Ajout de tests unitaires pour valider les nouvelles fonctionnalités et les corrections de bugs.
- Amélioration de la gestion des dépendances.
- Refactorisation du code pour améliorer la réutilisabilité et la lisibilité.

### Autres changements
- Mise à jour de la documentation.
- Correction de fautes de frappe et amélioration de la qualité des textes.
- Ajout de commentaires dans le code pour faciliter la compréhension.
- Correction de problèmes de performance mineurs.
- Mise à jour des fixtures pour refléter les changements dans les modèles de données.
