## Changelog : mobilic-api (30 derniers jours)

### Résumé
Les dernières mises à jour de l'API Mobilic se concentrent sur l'amélioration de la gestion des utilisateurs, des contrôles et des entreprises, notamment avec l'intégration d'une nouvelle source de données (BDC) et l'optimisation des alertes. Des corrections de bugs et des améliorations de l'interface ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité d'enregistrer le poids du véhicule lors d'un contrôle. [#676](https://github.com/MTES-MCT/mobilic-api/pull/676)
- Amélioration de la gestion des entreprises issues de la nouvelle source de données BDC. [#667](https://github.com/MTES-MCT/mobilic-api/pull/667)
- Prise en compte de l'absence d'activité lors d'un contrôle, entraînant une sanction. [#657](https://github.com/MTES-MCT/mobilic-api/pull/657)
- Modification du bouton de détachement pour les administrateurs. [#656](https://github.com/MTES-MCT/mobilic-api/pull/656)
- Amélioration du modèle d'email pour la création de compte tiers, incluant la validation du consentement. [#676](https://github.com/MTES-MCT/mobilic-api/pull/676)
- Restriction de l'accès des contrôleurs aux fournisseurs d'identité ProConnect autorisés. [#654](https://github.com/MTES-MCT/mobilic-api/pull/654)

### Évolutions techniques
- Refactorisation du code pour la gestion des métadonnées NATINF dans le cadre de l'intégration de la nouvelle source BDC. [#660](https://github.com/MTES-MCT/mobilic-api/pull/660)
- Optimisation des alertes Scalingo pour éviter les exécutions concurrentes dans les transactions. [#663](https://github.com/MTES-MCT/mobilic-api/pull/663)
- Ajout d'index à la table des emplois pour améliorer les performances. [#658](https://github.com/MTES-MCT/mobilic-api/pull/658)
- Amélioration de la gestion des statuts des employés (actif, inactif, licencié). [#658](https://github.com/MTES-MCT/mobilic-api/pull/658)
- Correction d'une erreur dans la date/heure des contrôles.
- Ajout de fallbacks pour les contrôles NATINF automatiques.
- Correction d'un problème de concurrence dans les transactions.
- Suppression de la dépendance `pypdf3`. [#660](https://github.com/MTES-MCT/mobilic-api/pull/660)

### Autres changements
- Correction de bugs mineurs et améliorations de la documentation.
- Mise à jour des tests unitaires et d'intégration.
- Correction de la logique pour la gestion des entreprises en cas d'absence d'activité.
- Correction de la gestion des utilisateurs tiers après la validation du consentement.
- Correction de l'affichage du nom ou de l'identifiant greco dans la nouvelle BDC.
- Correction de l'affichage de la date de naissance dans la nouvelle BDC.
- Correction de la gestion des cas où la date de naissance ou l'utilisateur contrôleur est manquant dans la nouvelle BDC.
- Correction d'un bug lié à la réintégration des emails.
- Correction d'un bug lié au calcul des employés inactifs.
