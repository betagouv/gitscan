## Changelog : mon-indemnisation-justice (30 derniers jours, au 09 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la refonte de l'application, notamment en préparant le passage à Symfony 8 et Doctrine 8.  De nombreuses améliorations ont été apportées à l'interface utilisateur, en particulier pour la saisie et la gestion des dossiers, avec une attention particulière portée à la gestion des erreurs et à l'expérience utilisateur. L'intégration de Sentry pour le suivi des erreurs a également été renforcée.

### Évolutions fonctionnelles
- Amélioration de l'affichage de l'explication de la clôture d'une demande sur la page "Mes demandes".
- La référence à rappeler est maintenant incluse dans l'email de confirmation de dépôt.
- Ajout du type d'attestation "Avis d'intervention".
- Correction de l'affichage du prénom et du nom de la personne morale.
- Correction d'un lien mort sur la page de récapitulatif.
- Amélioration de la gestion des erreurs France Connect : affichage de messages d'erreur clairs et envoi des erreurs à Sentry.
- Ajout d'un message d'erreur après une erreur d'inscription ou de connexion France Connect.
- Possibilité d'éditer et de téléverser des pièces jointes pendant l'instruction du dossier.
- Amélioration de la navigation et de la gestion des étapes de saisie du dossier.
- Ajout d'une modale pour l'ajout de fichiers avec prévisualisation.
- Création des pages d'étape de saisie du dossier et de la page de récapitulatif.
- Ajout d'un endpoint `/me` pour récupérer les informations du requérant.
- Amélioration de la gestion des permissions.
- Ajout d'un champ d'autocomplete pour l'adresse.
- Mise à jour du courriel d'invitation à déposer sur décla FDO.
- Publication de l'avis d'intervention mis à jour.

### Évolutions techniques
- Mise à jour de Symfony et Doctrine pour préparer le passage à la version 8.0.
- Mise à jour de l'image Docker pour retirer `APP_RUNTIME`.
- Correction des tests unitaires backend.
- Refonte de la gestion des erreurs pour plus de simplicité.
- Suppression de l'utilisation d'API Platform.
- Utilisation de Tanstack Router pour l'espace requérant.
- Normalisation des entités simplifiée.
- Création des entités `Brouillon` et `Personne`.
- Refactorisation de la route API listant les communes par code postal.
- Utilisation de DTOs pour l'échange de données avec l'espace FIP6.
- Suppression des classes de mapper.
- Migration des données de bris de porte vers une table dédiée.
- Suppression de la normalisation directe des entités.
- Amélioration de la gestion des brouillons de dossier.
- Intégration de Sentry pour le suivi des erreurs et la journalisation.
- Correction de bugs liés à Doctrine.
- Correction d'un bug lié à la configuration obsolète de Doctrine en production.

### Autres changements
- Mise à jour de la documentation PN.
- Installation de Crisp pour le support client.
- Documentation du schéma de base de données.
- Correction de tests end-to-end et ajout de délais d'attente.
- Mise à jour des fixtures de données et des tests associés.
- Nettoyage et réorganisation du code.
- Suppression de code inutile.
- Correction de la liaison déclaration <-> dossier, de la déconnexion usager et de l'attribution à un rédacteur.
- Validation de la présence de tous les types de pièces jointes.
- Création d'une page d'erreur 404.
- Création d'un compte FC de bac à sable pour le déploiement en environnement de développement.
- Enrichissement du champ Input.
- Correction de l'inscription France Connect.
- Suppression de la normalisation des entités.
- Correction de l'erreur lors de la décision.
- Correction de l'affichage des agents à gérer.
- Intégration des nouvelles informations et pièces jointes des personnes morales sur la vue dossier.
- Extension et adaptation de la liste des types de rapport au logement.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
- Correction de l'erreur lors de la décision.
