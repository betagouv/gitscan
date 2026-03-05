## Changelog : depenses-eclairees (30 derniers jours)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'extraction de données, notamment grâce à l'intégration de l'OCR Mistral, et sur l'amélioration de l'interface utilisateur pour une meilleure expérience de visualisation et de gestion des données. Des corrections de bugs et des refactorisations ont également été apportées pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de la prise en charge de la classification et de l'affichage des "fiches navette" dans l'interface utilisateur.
- Amélioration de l'extraction de données des actes d'engagement avec l'ajout de champs comme l'avance et le montant annexe.
- Intégration de l'OCR Mistral pour une meilleure reconnaissance de texte.
- Amélioration de l'affichage des montants avec un séparateur de milliers.
- Correction de l'affichage des checkbox et amélioration du design général de l'interface.
- Possibilité d'accepter les fiches navettes dans le front-end.
- Correction du calcul des pourcentages dans les actes d'engagement.
- Amélioration de la gestion des IBAN avec une validation plus stricte.
- Ajout de la gestion de la classification "fiche_navette".

### Évolutions techniques
- Refactorisation du code d'extraction de texte pour supporter différents formats de fichiers (xls, xlsx, ods).
- Amélioration de la gestion des timeouts du LLMClient.
- Refactorisation des fonctions de comparaison pour utiliser des prompts pour l'évaluation par LLM.
- Suppression de dépendances inutiles (odfpy).
- Amélioration de la gestion des tests, notamment avec l'intégration de Grist API pour récupérer les données de référence.
- Refactorisation de la gestion des permissions pour l'affichage des engagements.
- Mise à jour des dépendances.
- Amélioration de la gestion des erreurs OCR et ajout de tests algorithmiques.
- Utilisation de variables d'environnement pour la configuration de l'API Grist.
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Correction de bugs liés à l'authentification OIDC.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de style avec Ruff.
- Suppression de code obsolète.
- Amélioration des messages de log.
- Correction de conflits de merge.
- Ajout de tests pour les scopes d'administration.
- Correction de bugs mineurs dans l'interface utilisateur.
- Suppression de documents non prêts à être affichés dans le front-end.
- Configuration de la couverture de code avec pytest-cov.
