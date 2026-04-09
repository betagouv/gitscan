## Changelog : monprojetsup (30 derniers jours, au 24 mars 2026)

### Résumé
Les dernières évolutions de MonProjetSup se concentrent sur l'amélioration de la fonctionnalité de suggestions, notamment en corrigeant des problèmes de calcul et en ajoutant des tests. Des ajustements ont également été apportés à la gestion des indicateurs et à l'identification des experts, avec un accent sur la journalisation pour faciliter le débogage et le suivi.

### Évolutions fonctionnelles
- Correction du calcul de lissage de Laplace dans les suggestions, améliorant ainsi la pertinence des recommandations. [#1071](https://github.com/betagouv/monprojetsup/issues/1071)
- Désactivation de la corbeille des formations dans le cadre des suggestions. [#1071](https://github.com/betagouv/monprojetsup/issues/1071)
- Amélioration de l'affichage des explications détaillées, avec une inclusion dynamique.
- Correction d'un bug lié à l'année hardcodée.
- Les indicateurs sont maintenant correctement maintenus actifs. [#1078](https://github.com/betagouv/monprojetsup/issues/1078)

### Évolutions techniques
- Ajout de tests pour la CI (Continuous Integration) pour la fonctionnalité "suggestions2". [#1075](https://github.com/betagouv/monprojetsup/issues/1075)
- Refactorisation de l'extraction des informations de l'expert depuis le JWT (JSON Web Token).
- Injection d'un booléen pour identifier si l'utilisateur est un expert.
- Ajout de logs plus détaillés pour le processus d'authentification et l'identification des experts, facilitant le débogage. [#1073](https://github.com/betagouv/monprojetsup/issues/1073)
- Rebase de la branche `demo` sur `prod2` et `demo`. [#1074](https://github.com/betagouv/monprojetsup/issues/1074)
- Amélioration de la verbosité des claims JWT.
- Corrections de tests unitaires.
- Application de règles de linting pour améliorer la qualité du code.
