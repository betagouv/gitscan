## Changelog : mon-indemnisation-justice (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la refonte de l'expérience de dépôt de dossier, avec une attention particulière portée à la gestion des erreurs, l'intégration de France Connect, et l'amélioration de la robustesse de l'application. De nombreuses corrections et améliorations ont été apportées, notamment au niveau de la gestion des données et de l'interface utilisateur.

### Évolutions fonctionnelles
- Intégration de Crisp pour le support utilisateur.
- Amélioration de l'affichage de l'explication de la clôture sur la page "mes demandes".
- Ajout du type d'attestation "Avis d'intervention".
- Amélioration de l'affichage des informations sur les personnes morales dans la vue dossier.
- Ajout d'une page d'erreur 404 personnalisée.
- Implémentation d'une fonctionnalité d'autocomplétion pour le champ adresse.
- Création d'une page de récapitulatif.
- Amélioration de la navigation et correction de liens morts.
- Possibilité de télécharger des pièces jointes pendant l'édition d'un dossier.
- Ajout d'un message d'erreur plus clair après une erreur d'inscription ou de connexion France Connect.
- Amélioration de l'affichage des informations sur le pays et la commune de naissance.
- Mise à jour du courriel d'invitation à déposer sur décla FDO.
- Ajout d'un indicateur visuel pour les modifications non sauvegardées avant la fermeture de la page.

### Évolutions techniques
- Mise à jour de Symfony et Doctrine vers la version 8.0.
- Refonte de l'architecture de l'application avec l'utilisation de Tanstack Router pour l'espace requérant.
- Suppression de l'utilisation d'API Platform.
- Simplification de la gestion des erreurs et amélioration du logging avec l'intégration de Sentry.
- Création de DTOs pour l'échange de données avec l'espace FIP6.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Correction de tests unitaires et end-to-end.
- Mise à jour de l'image Docker pour retirer `APP_RUNTIME`.
- Normalisation des entités et simplification du mapping.
- Création des entités `Brouillon` et `Personne`.
- Déplacement des données de bris de porte vers une table dédiée.
- Suppression des classes de mapper.

### Autres changements
- Documentation du schéma de base de données.
- Mise à jour des documents PN.
- Correction de bugs mineurs et améliorations de la performance.
- Correction de la configuration Doctrine en production.
- Correction de problèmes liés à la validation des données.
- Correction de problèmes liés à la gestion des permissions.
- Correction de problèmes liés à la liaison entre les déclarations et les dossiers.
- Correction de problèmes liés à la déconnexion des utilisateurs.
- Correction de problèmes liés à l'attribution des dossiers aux rédacteurs.
- Correction de problèmes liés à la gestion des états de brouillon.
- Correction de problèmes liés à la récupération des pièces jointes.
- Correction de problèmes liés à la gestion des erreurs France Connect.
- Correction de problèmes liés à la gestion des données de rapport au logement.
- Création d'un compte FC de bac à sable pour le déploiement en environnement de développement.
- Amélioration de la gestion des erreurs et des messages d'erreur.
- Ajout de commentaires et de documentation au code.
