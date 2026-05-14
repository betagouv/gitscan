## Changelog : monstagedeseconde (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de la stabilité et de la performance de la plateforme, ainsi que sur l'ajout de nouvelles fonctionnalités pour faciliter la gestion des stages, notamment pour les établissements scolaires et les entreprises. Des mises à jour de sécurité et de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Amélioration de la géolocalisation et de la validation des adresses pour les entreprises [#817](https://github.com/betagouv/monstagedeseconde/pull/817).
- Possibilité pour un élève d'avoir deux stages validés simultanément.
- Correction d'un bug empêchant la validation des candidatures lorsque l'élève postule sur plusieurs semaines.
- Amélioration de l'affichage des offres d'emploi dans le tableau de bord pour les employeurs.
- Correction d'un problème d'affichage de la description des offres QPV.
- Ajout de la possibilité pour les référents d'inviter des collègues.
- Suppression de l'envoi d'emails de confirmation de candidature.
- Amélioration de l'affichage des statistiques pour les maisons d'accueil.
- Correction de bugs liés à l'affichage des coordonnées des maisons d'accueil.
- Correction d'un bug empêchant l'édition des conventions par les établissements.
- Correction d'un bug lié à l'affichage du nom et de l'email du responsable de l'établissement sur les conventions.
- Ajout de la possibilité pour les étudiants légaux de relancer les représentants pour redémarrer le processus de signature.

### Évolutions techniques
- Mise à jour de la version de Rails en 8.1 [#765](https://github.com/betagouv/monstagedeseconde/pull/765).
- Amélioration de la gestion des erreurs Sentry avec mise en cache et correction de plusieurs incidents signalés.
- Optimisation des requêtes SQL pour accélérer le processus de reconstruction de l'index.
- Ajout de tests CodeQL pour améliorer la sécurité du code.
- Refactorisation du code pour simplifier la logique de validation des candidatures.
- Mise à jour de plusieurs dépendances (bundler, npm, pip) pour bénéficier des dernières corrections et améliorations de sécurité.
- Amélioration de la configuration SSH pour les déploiements.
- Suppression de code obsolète.

### Autres changements
- Mise à jour de la documentation.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de commentaires pour faciliter la maintenance du code.
- Mise à jour des fichiers de configuration.
- Amélioration des tests unitaires et d'intégration.
- Correction de problèmes liés à l'affichage des liens FAQ.
- Correction de bugs liés à l'importation des maisons d'accueil.
- Correction de bugs liés à l'affichage des statistiques.
- Correction de bugs liés à la gestion des comptes utilisateurs.
- Correction de bugs liés à la gestion des offres de stage.
- Amélioration de la gestion des erreurs et des exceptions.
