## Changelog : mon-indemnisation-justice (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la refonte de l'application, notamment la migration vers Symfony 8 et Doctrine 8, ainsi que sur l'amélioration de l'expérience utilisateur avec la création d'un nouveau formulaire de dépôt de dossier, plus intuitif et complet. De nombreuses corrections de bugs et améliorations de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- **Dépôt de dossier :** Création des étapes de saisie du dossier, incluant la gestion des pièces jointes et la validation des données. Possibilité de naviguer avec un dossier existant.
- **Interface utilisateur :** Amélioration de l'affichage des dossiers dans l'espace rédacteur et correction de liens morts.
- **France Connect :** Amélioration de la gestion des erreurs et ajout de la remontée des erreurs dans Sentry. Affichage de messages d'erreur plus clairs pour l'utilisateur.
- **Notifications :** Remontée de la référence à rappeler dans l'email de confirmation de dépôt.
- **Types d'attestations :** Ajout du type "Avis d'intervention" à la liste des types d'attestation.
- **Autocomplete :** Ajout d'une autocomplete sur le champ adresse.
- **Gestion des utilisateurs :** Correction de l'affichage de la liste des agents à gérer.
- **Pièces jointes :** Possibilité d'ajouter et de prévisualiser des pièces jointes.
- **Décisions :** Correction d'une erreur lors de la prise de décision.

### Évolutions techniques
- **Mise à jour des dépendances :** Migration vers Symfony 8 et Doctrine 8.
- **Architecture :** Suppression de l'utilisation d'API Platform et refonte de la gestion des routes API.
- **Base de données :** Création de nouvelles entités (Brouillon, Personne) et simplification de la gestion des erreurs.
- **Monitoring :** Intégration de Sentry pour la remontée des erreurs et la surveillance de l'application. Transmission du contexte utilisateur à Sentry.
- **Docker :** Mise à jour de l'image Docker pour retirer `APP_RUNTIME`.
- **Tests :** Correction des tests unitaires backend et adaptation des tests end-to-end.
- **Code :** Nettoyage du code et suppression de classes de mapper inutiles.
- **Sécurité :** Conversion en minuscules des adresses en entrée et en base de données.

### Autres changements
- **Documentation :** Mise à jour de la documentation concernant les nouveaux points d'entrée API.
- **Configuration :** Correction d'une configuration obsolète pour Doctrine en production.
- **Intégration :** Installation de Crisp pour le support client.
- **Schéma de données :** Documentation du schéma de base de données.
- **Divers :** Ajout de données de test, correction de bugs mineurs et amélioration de la navigation.
