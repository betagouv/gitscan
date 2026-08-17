## Changelog : domifa (30 derniers jours, au 15 août 2026)

### Résumé
Ce mois a été marqué par une modernisation majeure de l'infrastructure technique, notamment avec le passage à Angular 20 et Node 22. Côté utilisateur, le portail a été enrichi de nouvelles fonctionnalités comme l'intégration du RGAA, la possibilité de télécharger des affiches et l'ajout de contenus pédagogiques (vidéo). Parallèlement, des optimisations importantes ont été réalisées sur le backend pour garantir une meilleure fluidité lors des imports de données.

### Évolutions fonctionnelles
- **Enrichissement du portail usagers :**
  - Intégration du RGAA sur le portail ([#4227](https://github.com/SocialGouv/domifa/pull/4227)).
  - Ajout de la possibilité de télécharger les affiches "Mon Domifa" ([#4217](https://github.com/SocialGouv/domifa/pull/4217)).
  - Ajout d'une vidéo de présentation "Découvrir Domifa" et d'un bouton pour afficher tous les témoins ([#4212](https://github.com/SocialGouv/domifa/pull/4212)).
- **Améliorations de l'expérience utilisateur :**
  - Mise à jour des Conditions Générales d'Utilisation (CGU 2025-2026).
  - Amélioration des notifications lors de la suppression de compte.
  - Meilleure clarté des informations de statut lors de la génération de comptes en masse ([#4219](https://github.com/SocialGouv/domifa/pull/4219)).
- **Corrections diverses :**
  - Résolution de problèmes d'affichage des résultats de recherche et des popups.
  - Correction de liens et de l'affichage des tableaux d'administration ([#4223](https://github.com/SocialGouv/domifa/pull/4223)).

### Évolutions techniques
- **Modernisation de la stack :** Migration majeure vers Angular 20 et Node 22, incluant la mise à jour de l'écosystème lié (NgRx, CDK, ESLint, Matomo).
- **Optimisation du backend :** 
  - Amélioration des performances d'importation en déportant le parsing et la validation dans des *worker threads* pour éviter de bloquer le serveur.
  - Renforcement de la gestion de la concurrence et de la stabilité lors des processus d'import.
- **Infrastructure et CI/CD :**
  - Migration des builds d'images vers `buildkit-operator`.
  - Amélioration de la résilience des déploiements pour garantir le "zero-downtime" et une meilleure détection des pods figés.
  - Routage des flux d'importation vers des pods dédiés ([#4249](https://github.com/SocialGouv/domifa/issues/4249)).
- **Sécurité et Refactoring :**
  - Déplacement de la gestion des en-têtes de sécurité directement au niveau de Nginx.
  - Ajout d'attributs de sécurité (`noopener noreferrer`) sur les liens externes.
  - Refactorisation de la gestion des codes OTP et des composants de formatage de données.

### Autres changements
- **Documentation :** Mises à jour régulières de la FAQ et des composants d'aide à l'utilisation ([#4240](https://github.com/SocialGouv/domifa/issues/4240), [#4236](https://github.com/SocialGouv/domifa/issues/4236)).
- **Maintenance :** Nettoyage des scripts de dump de base de données et optimisation des tests unitaires.
