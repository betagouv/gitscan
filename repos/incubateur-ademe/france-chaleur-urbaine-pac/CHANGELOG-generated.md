## Changelog : france-chaleur-urbaine-pac (30 derniers jours, au 1er août 2026)

### Résumé
Ce mois-ci, le projet a connu une refonte significative de l'interface utilisateur et de l'expérience utilisateur (UX) du questionnaire et de la page de résultats. L'objectif principal est d'améliorer la clarté et la facilité d'utilisation du comparateur de PAC, notamment sur mobile.  Une séparation du code en composants plus spécifiques a également été entreprise pour une meilleure maintenabilité.

### Évolutions fonctionnelles
- Amélioration de l'UX du formulaire de questionnaire, avec des ajustements graphiques et un réagencement de l'ordre des questions.
- Ajout d'une barre de défilement (scroll) sur les recommandations affichées.
- Correction de l'affichage du logo France Renov.
- Amélioration de l'affichage sur les appareils mobiles.
- L'option "Je ne sais pas" dans le questionnaire est maintenant affichée sur une nouvelle ligne pour une meilleure lisibilité.
- Redesign complet de la page de résultats pour une présentation plus claire et intuitive.
- Remplacement de la librairie `react-dsfr` par un système de "stepper" pour guider l'utilisateur à travers le questionnaire.

### Évolutions techniques
- Séparation du composant `HomeScreen` dans un fichier dédié pour une meilleure organisation du code.
- Découpage du composant principal `App` en `Questionnaire` et `ResultsPage` pour une meilleure modularité.
- Découpe de composants en éléments plus spécifiques pour faciliter la maintenance et la réutilisation.
- Ajout d'une configuration de build.
- Renommage de "IFPEN" en "PAC" dans le code pour plus de cohérence.

### Autres changements
- Initialisation du comparateur IFPEN (premières étapes de développement).
- Renommage de "journey" en "questionnaire" dans le code.
- Ajustements graphiques du graphique de résultats.
