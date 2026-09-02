## Changelog : resorption-bidonvilles (30 derniers jours, au 12/08/2026)

### Résumé
Cette période a été marquée par une simplification majeure de la plateforme avec le retrait de la fonctionnalité de questions/réponses et le renommage de l'espace "Entraide" en "Annuaire". Des améliorations ont également été apportées pour renforcer l'accessibilité de l'interface et la précision des indicateurs de données.

### Évolutions fonctionnelles
- **Simplification de l'interface** : suppression de la section Questions/Réponses et renommage de l'onglet "Entraide" en "Annuaire" [#2728](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2728).
- **Améliorations de l'expérience utilisateur** : correction du placement du fil d'ariane, amélioration de l'accessibilité générale et correction des interactions de clic dans les tableaux [#2738](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2738).
- **Gestion des données** : correction permettant de saisir un nombre de ménages égal à zéro dans les indicateurs d'action.

### Évolutions techniques
- **Refonte du système de questions/réponses** : suppression complète de la logique métier (contrôleurs, services, modèles), des tables de base de données et des migrations associées [#2728](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2728).
- **Optimisation de l'API** : réduction de la duplication de code, normalisation des indicateurs non renseignés (NULL) et suppression de contraintes SQL obsolètes [#2728](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2728).
- **Maintenance et stabilité** : correction de la compatibilité des UUID avec CommonJS, mise à jour des tests unitaires suite aux refontes et stabilisation du fichier `yarn.lock`.

### Autres changements
- **Nettoyage du projet** : suppression de packages inutilisés (matermost), de métadonnées de routes orphelines et d'illustrations non utilisées [#2728](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2728).
