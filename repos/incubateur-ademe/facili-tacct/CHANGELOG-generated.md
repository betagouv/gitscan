## Changelog : facili-tacct (30 derniers jours)

### Résumé
Les dernières mises à jour de facili-tacct se concentrent sur l'amélioration de la fonctionnalité "patch4", notamment en affinant l'affichage des aléas, des données statistiques et en corrigeant des erreurs liées à l'iframe et aux niveaux d'aggravation. Des améliorations ont également été apportées à l'interface utilisateur, notamment au niveau du menu latéral et de l'affichage des articles. Des corrections et des ajustements ont été effectués pour préparer la prochaine étape de déploiement (MEP 16/02/2026).

### Évolutions fonctionnelles
- Correction de l'affichage des aléas dans le patch4 (#issue inconnue).
- Amélioration de l'affichage des données statistiques et des surfaces agricoles dans le patch4 (#issue inconnue).
- Correction de l'iframe des aléas dans le patch4 (#issue inconnue).
- Suppression du niveau d'aggravation dans la partie statique du patch4 (#issue inconnue).
- Ajout de la possibilité d'exporter des données (déclencheur de sondage) (#issue inconnue).
- Mise à jour du texte et de l'affichage des aléas modérés dans le patch4 (#issue inconnue).
- Amélioration de l'affichage des articles (titre) (#issue inconnue).
- Activation/désactivation des cookies (#887c0cc8).

### Évolutions techniques
- Refactorisation du code pour utiliser `toSorted` (#94416008).
- Correction de la génération de Prisma et des modèles (#519de55e, #19bc53bf, #86d43be6).
- Préparation pour le déploiement MEP 16/02/2026 (#29142400).
- Suppression des `console.log` avant déploiement (#179602f7).
- Intégration des tuiles de carte pour le débroussaillement (#5c8fd19d).
- Intégration du menu latéral pour le débroussaillement (#5a44a278).
- Intégration des données de débroussaillement (#6c4566fb).

### Autres changements
- Mise à jour du budget (#852cfd73).
- Ajout d'une notification sur la page d'accueil (#76dc397e).
- Correction de l'affichage des recettes dans le patch4 (#f24f4b8b, #26e1fa04).
- Mise à jour de la recette modale des collections (#050cec98).
- Correction des secrets pour les types de cultures (#d39965ca).
- Mise à jour du texte du patch4 pour l'aléa modéré (#485727bb).
- Suppression de la notice de la page d'accueil (#b2e74d38).
