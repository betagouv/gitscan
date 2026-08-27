## Changelog : domifa (30 derniers jours, au 26 août 2026)

### Résumé
Ce mois-ci, Domifa a franchi une étape importante avec la montée de version vers Angular 20, renforçant la stabilité et la modernité de la plateforme. Les utilisateurs bénéficient de nouvelles fonctionnalités comme l'accès à un kit de communication, la possibilité de modifier leurs adresses e-mail en autonomie, et une meilleure gestion des codes de validation (OTP). L'expérience de navigation a également été enrichie par l'ajout de contenus pédagogiques (vidéo) et de nouveaux outils de téléchargement.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** : Ajout d'un onglet "Kit de communication", intégration du RGAA dans le portail usagers, et possibilité de télécharger les affiches "Mon Domifa".
- **Autonomie utilisateur** : Les structures peuvent désormais modifier leur adresse e-mail directement.
- **Amélioration de l'expérience (UX)** : 
    - Ajout d'un compte à rebours pour les codes de validation (OTP) afin de mieux gérer le délai de validité.
    - Ajout d'une vidéo de présentation pour découvrir la plateforme.
    - Amélioration de l'affichage des résultats de recherche et des menus déroulants.
- **Contenu et conformité** : Mise à jour des CGU pour l'année 2026 et ajout d'un bouton pour afficher tous les témoins.
- **Corrections** : Résolution de divers problèmes d'affichage (dates, popups, liens) et de l'affichage des secondes.

### Évolutions techniques
- **Migration majeure** : Mise à jour complète de l'écosystème frontend vers Angular 20 (incluant NgRx, CDK et les outils de build).
- **Optimisation des performances** : 
    - Refonte du processus d'importation pour utiliser des threads de travail (*worker threads*), évitant ainsi le blocage du système lors de l'analyse de fichiers volumineux.
    - Meilleure gestion de la concurrence et du nettoyage des fichiers lors des uploads.
- **Infrastructure et CI/CD** : 
    - Optimisation du déploiement en routant les flux d'importation vers des pods dédiés [#4249](https://github.com/SocialGouv/domifa/pull/4249).
    - Amélioration de la résilience des déploiements pour garantir une disponibilité continue.
- **Base de données** : Migration des comptes utilisateurs n'ayant pas mis à jour leur mot de passe récemment [#4241](https://github.com/SocialGouv/domifa/pull/4241).
- **Refactorisation** : Optimisation de la gestion des codes OTP et du formatage des grands nombres.

### Autres changements
- Suppression de Swagger sur le backend.
- Mise à jour de la documentation et des contenus de la FAQ.
