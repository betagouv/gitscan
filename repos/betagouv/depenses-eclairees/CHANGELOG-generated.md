## Changelog : depenses-eclairees (30 derniers jours)

### Résumé
Les dernières mises à jour de depenses-eclairees se concentrent sur l'amélioration de l'extraction et de l'affichage des données, notamment pour les actes d'engagement, les fiches navettes et les documents CCAP. Des efforts importants ont été réalisés pour optimiser la reconnaissance optique de caractères (OCR) avec l'intégration de Mistral, et pour affiner la classification des documents. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Amélioration de l'affichage des actes d'engagement avec ajout de la gestion de l'avance et du montant en annexe. (#76, #68, #53)
- Prise en charge de l'affichage des fiches navette dans l'interface utilisateur. (#71, #63)
- Amélioration de la classification des documents et correction de problèmes liés à la reconnaissance des types de fichiers. (#65, #57, #55)
- Intégration d'un nouvel outil OCR (Mistral) pour une meilleure extraction de texte des documents numérisés. (#51)
- Amélioration de l'affichage des montants avec ajout du séparateur de milliers. (#53)
- Ajout de la gestion des documents RIB et amélioration de l'affichage des attributs. (#53)
- Correction de l'affichage des checkbox décalées. (#57)
- Correction du login OIDC. (#56)

### Évolutions techniques
- Refactorisation des fonctions de comparaison pour utiliser des prompts pour l'évaluation par LLM. (#73)
- Suppression de la dépendance `odfpy` et refactorisation de l'extraction Excel. (#62)
- Amélioration de la gestion des timeouts du LLMClient et ajout d'une limitation de débit par modèle. (#53)
- Refactorisation du code pour une meilleure lisibilité et maintenance, notamment dans les tests et les templates. (#73, #67, #61, #58)
- Utilisation de variables d'environnement pour la configuration de l'API Grist. (#67)
- Mise à jour des dépendances du projet. (#61, #56)
- Amélioration de la gestion des erreurs et des exceptions dans le code. (#51)
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code. (#73, #51)
- Refactorisation de la base de données pour une meilleure gestion des relations entre les documents et les engagements. (#56)

### Autres changements
- Mise à jour de la documentation et des commentaires dans le code.
- Amélioration du formatage du code avec `ruff`.
- Suppression de code obsolète et nettoyage du codebase.
- Correction de bugs mineurs et amélioration de la stabilité du projet.
- Ajout de nouvelles variables d'environnement pour la configuration des tests.
- Suppression de certains documents du front car non prêt à être affichés. (#53)
