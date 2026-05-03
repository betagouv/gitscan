## Changelog : mon-indemnisation-justice (30 derniers jours, au 01 mai 2026)

### Résumé
Le projet a connu une période d'activité intense axée sur la refonte de l'expérience de dépôt de dossier, avec une attention particulière portée à la gestion des données, la sécurité et l'amélioration de l'interface utilisateur. De nombreuses étapes du processus ont été revues et implémentées, incluant la gestion des brouillons, l'ajout de pièces jointes, la validation des données et l'intégration de France Connect. L'équipe a également renforcé la surveillance et la gestion des erreurs grâce à l'intégration de Sentry.

### Évolutions fonctionnelles
- Intégration de Crisp pour le support utilisateur.
- Amélioration de l'affichage des dossiers dans l'espace rédacteur.
- Implémentation d'une page d'erreur 404 personnalisée.
- Ajout d'une fonctionnalité d'autocomplétion pour le champ adresse.
- Création des pages d'étape de saisie du dossier.
- Validation des données de la première étape du formulaire.
- Possibilité de naviguer avec un dossier existant.
- Affichage et gestion des pièces jointes.
- Création d'une modale d'ajout de fichiers avec prévisualisation.
- Amélioration de l'inscription et de la connexion via France Connect, avec remontée des erreurs.
- Gestion des permissions pour les points d'entrée API requérant.
- Possibilité d'éditer et de téléverser des pièces jointes pendant l'instruction du dossier.
- Affichage de la validation et de l'obligation des champs.
- Correction de l'erreur lors de la décision.
- Amélioration de la gestion des erreurs et affichage de messages plus clairs à l'utilisateur.
- Mise à jour du courriel d'invitation à déposer sur décla FDO.
- Publication de l'avis d'intervention mis à jour.

### Évolutions techniques
- Suppression de l'utilisation d'API Platform.
- Refonte de la gestion des entités et des données, avec création d'entités dédiées (Brouillon, Personne).
- Utilisation de DTOs pour l'échange de données avec l'espace FIP6.
- Migration vers le router Tanstack pour l'espace requérant.
- Simplification de la gestion des erreurs.
- Correction des tests backend et end-to-end.
- Normalisation des entités et correction des tests associés.
- Documentation du schéma de base de données.
- Intégration de Sentry pour la surveillance et la gestion des erreurs.
- Réorganisation de routes API pour la liste des communes par code postal.
- Création d'un endpoint `/me` pour le requérant.
- Suppression des classes de mapper.
- Délégation de l'acceptation au DossierManager.
- Suppression de la normalisation directe des entités.

### Autres changements
- Mise à jour des documents PN.
- Création d'un compte FC de bac à sable pour le déploiement en environnement de développement.
- Renommage des tables `bris_porte` en `dossiers` et `requerants` en `usagers`.
- Correction d'un bug où l'état actuel du patch était perdu.
- Ajout des pays et de la commune de naissance.
- Correction de l'affichage de la liste des agents à gérer.
- Enrichissement du champ Input.
- Suppression des données de bris de porte vers une table dédiée.
- Correction de la liaison déclaration <-> dossier et de la déconnexion utilisateur.
- Validation de la présence de tous les types de pièces jointes.
- Correction de l'astérisque indiquant les champs obligatoires.
- Création d'attributs pour enrichir les arguments de route.
- Correction de l'inscription France Connect.
- Correction de la perte d'informations lors du changement d'étape.
- Correction des données fixtures et des tests liés aux actions requérants.
- Ajustements de l'étape 1 du formulaire.
- Rallongement du délai d'attente de disparition de la modale dans les tests end-to-end.
- Correction d'un bug empêchant la création d'un dossier sans requérant.
- Ajout d'un message d'alerte lors de la fermeture avec des modifications non sauvegardées.
- Correction de la gestion des erreurs liées à la date.
- Publication du code en production (branche `prod` mergée dans `main`).
