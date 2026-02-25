## Changelog : diagbruit.beta.gouv.fr (30 derniers jours)

### Résumé
Les dernières mises à jour de diagbruit.beta.gouv.fr se concentrent sur l'amélioration de la gestion des zones bruyantes, le calcul du score sonore et l'expérience utilisateur. Des corrections de bugs et des refactorisations ont également été apportées pour stabiliser et optimiser la plateforme.

### Évolutions fonctionnelles
- Ajout d'une alerte spécifique si une zone de bruit est atteinte (#40).
- Intégration de la ville de Strasbourg à la liste blanche des zones autorisées (#42).
- Amélioration de l'affichage du résumé des informations, notamment la taille du texte et la présentation générale (#42).
- Ajout d'un iframe pour afficher un tableau de bord externe (#41).
- Ajout d'un bouton pour copier l'URL de la page, avec un style visuel amélioré (#35).
- Ajout d'une gestion des erreurs 500 avec un message d'erreur clair pour l'utilisateur (#35).
- Amélioration de l'affichage des composants de réglementation (#35).
- Ajout d'un score global (#35).
- Calcul du pourcentage de zones impactées (#35).

### Évolutions techniques
- Refactorisation du code frontend pour améliorer la lisibilité et la maintenabilité (#42, #35).
- Ajout de zones de bruit dans la base de données et l'API (#40).
- Adaptation des scripts d'ingestion de données pour tenir compte des changements en production (#37).
- Correction de bugs dans les tests d'intégration FastAPI (#38, #35).
- Mise à jour de la version de l'API (#38, #35).
- Correction d'une erreur dans les scripts DBT causant des échecs de création d'indices (#35).
- Ajout de tests pour la gestion de l'isolation acoustique (#35).
- Suppression de références inutiles au PLU local dans le frontend (#35).

### Autres changements
- Correction de bugs mineurs dans l'interface utilisateur, notamment concernant les titres d'accordéon et l'affichage des totaux de zonage (#41).
- Amélioration du style visuel de certains éléments de l'interface, comme les boutons et le héros (#42).
- Correction de conflits dans le code (#35).
- Ajout de la possibilité de gérer des exceptions liées à la représentation des zones (#37).
- Suppression d'un package `serve` inutilisé dans le frontend (#35).
