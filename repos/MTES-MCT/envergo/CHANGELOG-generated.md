## Changelog : envergo (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des haies et des pétitions, ainsi que sur des corrections de bugs et des optimisations de performance. Des améliorations de la sécurité et de la conformité RGPD ont également été apportées. Enfin, la documentation et les tests ont été renforcés.

### Évolutions fonctionnelles
- Amélioration de l'affichage des haies sur la carte, avec optimisation des requêtes et correction de bugs liés à la densité et au dessin. [#1124](https://github.com/MTES-MCT/envergo/issues/1124)
- Ajout d'informations sur la responsabilité (liability) et suivi des liens associés dans les pétitions. [#1098](https://github.com/MTES-MCT/envergo/issues/1098)
- Amélioration de la gestion des messages d'erreur et d'information, notamment pour les jetons expirés et les actions à effectuer. [#1096](https://github.com/MTES-MCT/envergo/issues/1096)
- Clarification de l'affichage des coefficients RU. [#1086](https://github.com/MTES-MCT/envergo/issues/1086)
- Ajout d'une FAQ pour les instructeurs, accessible via Gitbook. [#1101](https://github.com/MTES-MCT/envergo/issues/1101)
- Amélioration de la notification de changement d'état dans les procédures. [#1118](https://github.com/MTES-MCT/envergo/issues/1118)
- Correction de l'affichage de la date dans les formulaires. [#1105](https://github.com/MTES-MCT/envergo/issues/1105)
- Correction de l'affichage de la fin du dessin des haies. [#1108](https://github.com/MTES-MCT/envergo/issues/1108)
- Amélioration de l'affichage des haies. [#1109](https://github.com/MTES-MCT/envergo/issues/1109)

### Évolutions techniques
- Suppression du modèle `RecipientStatus` et des événements associés dans le cadre d'une simplification de la gestion des emails et de la conformité RGPD. [#1126](https://github.com/MTES-MCT/envergo/issues/1126)
- Optimisation du calcul de la longueur des haies. [#1124](https://github.com/MTES-MCT/envergo/issues/1124)
- Refactorisation du code lié à l'analyse des données (analytics) pour une meilleure lisibilité et maintenance.
- Correction de la gestion des erreurs liées aux valeurs flottantes dans les tests. [#1138](https://github.com/MTES-MCT/envergo/issues/1138)
- Correction de la gestion des octets nuls dans les champs de département. [#1116](https://github.com/MTES-MCT/envergo/issues/1116)
- Optimisation de la requête pour l'affichage des haies en simplifiant la topologie du cercle.
- Amélioration de la gestion des erreurs de validation dans le module MTM. [#1139](https://github.com/MTES-MCT/envergo/issues/1139)
- Mise à jour des dépendances. [#1092](https://github.com/MTES-MCT/envergo/issues/1092)

### Autres changements
- Mise à jour de la documentation.
- Amélioration de la lisibilité du code.
- Ajout de tests unitaires et d'intégration.
- Correction de problèmes de compatibilité avec les anciennes évaluations.
- Clarification des commentaires dans le code.
- Correction de bugs mineurs dans l'interface utilisateur.
- Mise à jour des messages d'erreur pour une meilleure clarté.
- Modification du libellé "Administration" en "Espace instruction". [#1145](https://github.com/MTES-MCT/envergo/issues/1145)
- Correction du CI. [#1145](https://github.com/MTES-MCT/envergo/issues/1145)
