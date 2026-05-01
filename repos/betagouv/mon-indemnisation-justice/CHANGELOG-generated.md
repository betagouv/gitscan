## Changelog : mon-indemnisation-justice (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, l'application a connu une refonte significative de l'interface utilisateur et de la gestion des données, notamment en vue de la prise en charge des dossiers et requérants. De nombreuses améliorations ont été apportées au formulaire de dépôt de dossier, à la gestion des pièces jointes et à l'intégration avec FranceConnect. Des corrections de bugs et des optimisations ont également été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Intégration de Crisp pour le support utilisateur.
- Amélioration de l'affichage des dossiers dans l'espace rédacteur.
- Implémentation d'une page de récapitulatif du dossier.
- Ajout d'une autocomplétion pour le champ adresse.
- Création des pages d'étape de saisie du dossier.
- Validation des données de la première étape du formulaire.
- Possibilité de publier un brouillon de dossier.
- Affichage des informations et des pièces jointes des personnes morales.
- Correction de l'erreur lors de la décision.
- Ajout d'un message d'erreur clair après une erreur d'inscription ou de connexion FranceConnect.
- Amélioration de la gestion des erreurs et des validations dans le formulaire.
- Possibilité d'éditer le dossier avant l'instruction et de téléverser des pièces jointes pendant cette phase.
- Création d'une modale d'ajout de fichiers avec prévisualisation.
- Navigation améliorée avec un dossier existant.
- Correction de l'inscription FranceConnect.
- Affichage d'un message informant l'utilisateur des modifications non sauvegardées lors de la fermeture de la page.
- Ajout d'un endpoint `/me` pour récupérer les informations du requérant.
- Correction des datas fixtures et des tests liés aux actions requérants.

### Évolutions techniques
- Suppression de l'utilisation d'API Platform.
- Refonte de la gestion des données avec la création des entités `Brouillon` et `Personne`.
- Utilisation de DTOs (Data Transfer Objects) pour l'échange de données avec l'espace FIP6.
- Migration vers le router Tanstack pour l'espace requérant.
- Simplification du mapping des données.
- Correction des tests backend et end-to-end.
- Normalisation des entités.
- Intégration de Sentry pour la gestion des erreurs et le logging.
- Documentation du schéma de base de données.
- Restructuration des routes API pour la liste des communes par code postal.
- Suppression de classes de mapper inutiles.
- Amélioration de la gestion des permissions.
- Correction de la perte d'informations lors du changement d'étape du formulaire.
- Refonte de la gestion des erreurs.
- Suppression de la normalisation directe des entités.

### Autres changements
- Mise à jour des documents PN (Plan National).
- Création d'un compte FranceConnect de bac à sable pour l'environnement de développement.
- Renommage des tables `bris_porte` en `dossiers` et `requerants` en `usagers`.
- Correction de la liste des agents à gérer qui ne s'affichait plus.
- Extension et adaptation de la liste des types de rapport au logement.
- Publication d'un avis d'intervention mis à jour.
- Correction de la liaison entre la déclaration et le dossier, la déconnexion utilisateur et l'attribution à un rédacteur.
- Validation de la présence de tous les types de pièces jointes.
- Suppression de la page 404 par défaut et création d'une page personnalisée.
- Correction de la gestion des données de l'étape 1.
- Suppression de l'API Platform.
- Sauvegarde des données via le `DossierManager`.
- Rafraîchissement de la liste des communes en fonction du code postal.
- Définition du schéma de données idéal (en cours).
- Conversion des dossiers à finaliser en brouillons pour utiliser les données réelles du formulaire.
- Correction de l'association personne physique.
- Correction de l'affichage des valeurs de rapport au logement pour les tests d'éligibilité.
- Premier jet de l'interface de l'étape 3.
- Soumission et notification du dépôt de dossier.
- Correction de l'EntityResolveur qui pouvait retourner null.
- Création des routes API pour la gestion des brouillons.
- Liaison directe des personnes physiques ou morales au dossier.
- Correction de la normalisation côté FDO.
- Nommage précis des types de pièces jointes.
- Récupération et affichage des pièces jointes.
- Enrichissement du champ Input.
- Gestion des permissions sur les points d'entrée API requérant.
- Activation des formulaires dans la modale.
- Correction de l'erreur lors de la décision.
- Correction de l'astérisque indiquant les champs obligatoires.
- Création d'attributs pour enrichir les arguments de route.
- Réorganisation des étapes 1 et 2 du formulaire.
- Correction de l'inscription FranceConnect.
- Suppression de la normalisation directe des entités.
- Correction des tests.
- Mise en place d'un système de logging avec Sentry.
- Correction de la perte d'information lors du changement d'étape.
- Correction de l'affichage des erreurs.
- Suppression de la normalisation directe des entités.
- Correction de la perte d'information lors du changement d'étape.
- Correction de l'affichage des erreurs.
- Correction de l'inscription FranceConnect.
- Correction de la perte d'information lors du changement d'étape.
- Correction de l'affichage des erreurs.
- Correction de l'inscription FranceConnect.
- Correction de la perte d'information lors du changement d'étape.
- Correction de l'affichage des erreurs.
- Correction de l'inscription FranceConnect.
- Correction de la perte d'information lors du changement d'étape.
- Correction de l'affichage des erreurs.
- Correction de l'inscription FranceConnect.
- Correction de la perte d'information lors du changement d'étape.
- Correction de l'affichage des erreurs.
- Correction de l'inscription FranceConnect.
- Correction de la perte d'information lors du changement d'étape.
- Correction de l'affichage des erreurs.
- Correction de l'inscription FranceConnect.
