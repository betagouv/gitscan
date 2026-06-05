## Changelog : monitorenv (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'interface utilisateur et la gestion des données, notamment au niveau des zones de vigilance et des aires réglementaires. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application. L'ajout de tags et la refonte de certains composants contribuent à une meilleure organisation et accessibilité des informations.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre le focus sur une ligne lors d'un clic dans les tableaux de données.
- Amélioration du filtrage des ressources `controlUnit` par rapport aux ressources de contrôle de mission [#1234](https://github.com/MTES-MCT/monitorenv/issues/1234).
- Correction de l'affichage du nom de la source `controlUnit` dans le survol des zones de vigilance.
- Implémentation de la création et de l'affichage de tags dans l'interface backoffice.
- Ajout d'une table éditable avec un formulaire et un rechargement des données lors de la sauvegarde.
- Affichage du planning dans une vue liste pour les zones de vigilance.
- Ajout d'un infobulle pour la période sur le planning des zones de vigilance.
- Correction de l'affichage des notes sur la timeline des missions.
- Correction des filtres de tags dans la recherche de couches.
- Amélioration de l'affichage des périodes dans la liste des zones de vigilance, notamment en termes d'accessibilité.
- Ajout d'un cercle indiquant la période dans le nom des lignes des zones de vigilance et correction de l'interface utilisateur dans la ligne étendue.

### Évolutions techniques
- Mise à jour de Node.js vers la version 24 et de npm vers la version 11, avec ajout de logs pour les tests RGAA.
- Refactorisation du composant `MonthBox`.
- Correction de problèmes de typage suite à la mise à jour des dépendances.
- Suppression de code obsolète pour les aires réglementaires.
- Amélioration du flux de mise à jour des aires réglementaires environnementales.
- Suppression des flux de mise à jour des thèmes et des tags depuis le CACEM.
- Suppression des anciennes tables et correction des données de test pour les aires réglementaires.
- Correction de requêtes SQL pour les hashes CACEM.
- Suppression du trigger de mise à jour du hash des lignes des aires réglementaires.

### Autres changements
- Correction de fautes de frappe dans le fichier README.
- Correction de tests unitaires et E2E.
- Suppression de code inutile.
- Mise à jour des icônes de l'interface utilisateur.
- Mise à jour du survol des zones de vigilance.
- Correction de la variable name.
