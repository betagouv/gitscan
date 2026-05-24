## Changelog : envergo (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de l'expérience utilisateur, notamment dans la gestion des haies et des pétitions, ainsi que sur l'optimisation des performances et la maintenance technique du code. Des améliorations de la gestion des erreurs et de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'affichage des messages aux utilisateurs [#1096](https://github.com/MTES-MCT/envergo/issues/1096).
- Correction d'un problème d'affichage des valeurs flottantes dans les tests liés aux pétitions [#1138](https://github.com/MTES-MCT/envergo/issues/1138).
- Ajout d'informations de suivi pour les informations de responsabilité dans les simulations [#1092](https://github.com/MTES-MCT/envergo/issues/1092) et [#1098](https://github.com/MTES-MCT/envergo/issues/1098).
- Amélioration de la notification de changement d'état dans les pétitions.
- Ajout d'un lien vers la documentation Gitbook pour les instructeurs [#1101](https://github.com/MTES-MCT/envergo/issues/1101).
- Correction de l'affichage des haies et de la fin du dessin.
- Correction d'un bug lié à la suppression du coefficient de replantation existant [#1090](https://github.com/MTES-MCT/envergo/issues/1090).
- Correction d'un problème de paramètre `is_alternative` dupliqué dans l'URL de plantation.
- Amélioration de l'affichage des actions à prendre.
- Ajout d'un lien vers Tally dans les pages d'erreur 403.

### Évolutions techniques
- Optimisation de la requête pour accélérer l'affichage des haies [#1124](https://github.com/MTES-MCT/envergo/issues/1124).
- Optimisation du calcul de la longueur des haies.
- Simplification du code lié aux coefficients de ruissellement.
- Refactoring du code lié aux champs DN pour une meilleure maintenance.
- Correction de la gestion des octets NUL dans le champ département pour éviter les erreurs de données [#1115](https://github.com/MTES-MCT/envergo/issues/1115).
- Gestion des erreurs `ValueError` lors de la récupération de l'ID du département.
- Prévention des erreurs `TransactionManagementError` lors de la publication des évaluations.
- Correction du comportement de l'API `HedgeConditionsView` pour renvoyer un code 405 pour les requêtes GET.
- Amélioration de la gestion des cookies et des jetons d'invitation.
- Ajout de tests pour la gestion des cookies.
- Amélioration de la lisibilité du code.
- Suppression de code obsolète.
- Correction de problèmes liés à la compatibilité avec les anciennes évaluations.

### Autres changements
- Mise à jour de la documentation.
- Ajout de commentaires dans le code.
- Amélioration des noms de classes.
- Ajout de tests unitaires.
- Correction de petites erreurs typographiques et de style.
- Ajout de migrations pour les changements de schéma de base de données.
- Correction de problèmes d'affichage des messages d'erreur.
- Ajout de logs pour faciliter le débogage.
- Amélioration de la sécurité en vérifiant la validité des jetons.
- Correction d'un problème d'affichage des messages d'expiration.
- Ajout d'une documentation pour les dossiers.
- Ajout de métriques Matomo pour le suivi des liens de responsabilité.
