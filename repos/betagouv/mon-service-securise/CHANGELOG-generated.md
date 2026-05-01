## Changelog : mon-service-securise (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la refonte de l'interface utilisateur vers une version SPA (Single Page Application) pour améliorer l'expérience utilisateur, notamment dans les parcours d'homologation et la gestion des services. De nombreuses corrections et améliorations ont été apportées à l'accessibilité et à la stabilité de l'application. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la performance du projet.

### Évolutions fonctionnelles
- Implémentation du parcours d'homologation en SPA avec navigation entre les étapes : téléchargement de dossier, documents, avis, décision et récapitulatif [#1234](https://github.com/betagouv/mon-service-securise/issues/1234).
- Ajout de la possibilité de reprendre une homologation en cours.
- Ajout de landings "Sécurisez votre service numérique" et "Industrialisez vos homologations".
- Affichage des données de dossiers d'homologation dans la SPA.
- Ajout d'un bouton de téléchargement du tampon d'homologation.
- Ajout de la navigation entre les onglets d'indice cyber.
- Affichage des indices cyber ANSSI et personnalisé dans les onglets.
- Ajout de la page "Indice Cyber" dans la SPA.
- Ajout de la gestion des risques V1 à l'objet JSON de service complet.
- Ajout de la possibilité de télécharger les documents.
- Ajout d'un bouton "Enregistrer la décision" sur la dernière étape du parcours d'homologation.
- Ajout d'une modale "Démarche d'homologation indicative".
- Affichage du parcours d'homologation en lecture seule si nécessaire.
- Ajout de la possibilité de masquer le titre de "PageService" sur les étapes autres que la première.

### Évolutions techniques
- Migration progressive de l'interface utilisateur vers Svelte et une architecture SPA.
- Refonte du header avec l'utilisation des composants DSFR.
- Utilisation des variables CSS du DSFR pour les styles.
- Extraction de composants réutilisables (boutons, cartes, modales).
- Amélioration de la structure du code et factorisation de composants.
- Mise à jour des dépendances (Express, PostgreSQL, bcrypt, jsonwebtoken, axios, pg, knex, Svelte, Vite, etc.).
- Ajout de tests d'accessibilité avec Playwright et Axe.
- Configuration de l'exécution des tests d'accessibilité en CI/CD.
- Amélioration de la gestion des erreurs et des retries (recherche d'entreprise).
- Refactoring des workflows de déploiement Clever Cloud.
- Suppression des anciennes vues `pug`.
- Utilisation de l'API pour enregistrer les contacts utiles via un POST.

### Autres changements
- Suppression des fichiers concernant les anciennes pages de service.
- Amélioration des styles du bloc "Fonctionnalités".
- Correction de fautes d'orthographe et amélioration du wording.
- Nettoyage du code et suppression de code obsolète.
- Mise à jour de la documentation.
- Ajout de commentaires et amélioration de la lisibilité du code.
- Correction de problèmes de style et d'affichage.
- Correction de bugs divers.
- Suppression du bandeau de promotion de MSC.
- Ajout de liens vers des articles de FAQ.
- Amélioration de la gestion des états "hover" et "actif" des cartes d'indices cyber.
- Ajout du nom du service dans l'entête des pages de service.
- Ajout du bouton de gestion des contributeurs.
- Correction de l'affichage de l'entête des pages service avec un étapier.
- Correction de l'affichage de la visite guidée pour les étapes Sécuriser et Homologuer.
- Correction de problèmes de scroll sur les pages de service.
- Correction de tests et amélioration de la couverture de tests.
- Correction de problèmes d'accessibilité.
- Amélioration de la performance de l'application.
