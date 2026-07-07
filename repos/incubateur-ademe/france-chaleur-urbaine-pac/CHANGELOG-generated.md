## Changelog : france-chaleur-urbaine-pac (30 derniers jours, au 6 juillet 2026)

### Résumé
Ce mois-ci, le projet a connu une refonte significative de l'interface utilisateur et de l'expérience utilisateur du comparateur de PAC. Les améliorations se concentrent sur la clarté du formulaire, la présentation des résultats et l'adaptation aux écrans mobiles. Des optimisations graphiques et des ajustements de l'ordre des questions ont également été apportés.

### Évolutions fonctionnelles
- Ajout d'un bouton de partage de simulation pour faciliter le partage des résultats.
- Implémentation d'un bouton "Question précédente" pour une navigation plus fluide dans le questionnaire.
- Ajout d'une barre de progression (stepper) pour le questionnaire, remplaçant l'utilisation de React-DSFR.
- Amélioration de la gestion de l'option "Je ne sais pas" dans le formulaire, pour une meilleure lisibilité.
- Ajout d'une zone de défilement pour les recommandations.
- Redesign complet de la page de résultats pour une présentation plus claire et intuitive.
- Amélioration de la qualité de l'image des PAC affichées.
- Adaptation de l'affichage pour les écrans mobiles.

### Évolutions techniques
- Séparation du composant `HomeScreen` dans un fichier dédié pour une meilleure organisation du code.
- Renommage du composant `journey` en `questionnaire` pour une meilleure sémantique.
- Refactorisation du code pour découper les composants en éléments plus spécifiques et réutilisables.
- Modification de la configuration de build pour tester le déploiement sur electrifionslafrance.
- Tests de l'intégration des assets en ligne.
- Suppression de CSS inutilisés pour optimiser la taille du bundle.

### Autres changements
- Correction du logo France Renov.
- Ajustements graphiques divers basés sur les retours de recette.
- Renommage de "IFPEN" en "PAC" dans le code.
- Initialisation du comparateur IFPEN (premiers pas).
