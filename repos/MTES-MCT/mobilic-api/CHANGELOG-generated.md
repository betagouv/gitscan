## Changelog : mobilic-api (30 derniers jours)

### Résumé
Les dernières mises à jour de l'API Mobilic se concentrent sur l'amélioration de la gestion des entreprises, des contrôles et des utilisateurs. Des corrections ont été apportées pour une meilleure gestion des dates, des informations sur les entreprises et des alertes. De nouvelles fonctionnalités ont été ajoutées pour la gestion des employés inactifs et l'intégration avec Brevo pour l'envoi de notifications.

### Évolutions fonctionnelles

- Ajout de la possibilité d'enregistrer le poids du véhicule lors des contrôles, visible sur le bulletin de contrôle. [#668](https://github.com/MTES-MCT/mobilic-api/pull/668)
- Amélioration de la gestion des entreprises issues de la nouvelle BDC (Base de Données Communale). [#667](https://github.com/MTES-MCT/mobilic-api/pull/667), [#660](https://github.com/MTES-MCT/mobilic-api/pull/660)
- Ajout d'une sanction en cas d'absence d'activité le jour du contrôle.
- Possibilité de voir les employés inactifs dans l'interface d'administration. [#653](https://github.com/MTES-MCT/mobilic-api/pull/653)
- Ajout d'une fonctionnalité pour rattacher un employé, avec envoi d'une notification par email. [#656](https://github.com/MTES-MCT/mobilic-api/pull/656)
- Amélioration du workflow d'activation via Brevo. [#654](https://github.com/MTES-MCT/mobilic-api/pull/654)
- Restriction de l'accès à l'authentification ProConnect pour les contrôleurs. [#657](https://github.com/MTES-MCT/mobilic-api/pull/657), [#662](https://github.com/MTES-MCT/mobilic-api/pull/662)

### Évolutions techniques

- Ajout d'un index à la table `employment` pour optimiser les performances.
- Refactoring du code pour la gestion des métadonnées NATINF dans le cadre de l'intégration de la nouvelle BDC.
- Ajout d'une colonne `last_active_at` à la table `employment` avec un trigger PostgreSQL pour la mise à jour automatique.
- Amélioration de la gestion des transactions concurrentes.
- Correction d'une erreur de date dans la gestion des contrôles.
- Suppression de la dépendance `pypdf3`.
- Optimisation de la logique de calcul des employés inactifs.
- Correction d'un bug empêchant l'envoi d'emails de rattachement dans une transaction atomique.

### Autres changements

- Correction d'un revert de la fusion de la branche `feat/register-vehicle-weight`.
- Mise à jour de la documentation et ajout de tests unitaires.
- Amélioration de la gestion des erreurs et des messages d'erreur.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de la localisation et de l'heure de début/fin dans la nouvelle BDC.
- Ajout de l'annexe avec les infractions dans la nouvelle BDC.
- Ajout de la gestion du cas où la date de naissance ou l'utilisateur contrôleur est manquant dans la nouvelle BDC.
- Ajout de la possibilité d'exclure les administrateurs du calcul des employés inactifs.
- Ajout de la possibilité de terminer plusieurs emplois en batch.
- Ajout de l'API pour la localisation des contrôles. [#651](https://github.com/MTES-MCT/mobilic-api/pull/651)
