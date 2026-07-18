## Changelog : recommandations-collaboratives (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, notamment l'implémentation de l'authentification à deux facteurs (2FA) pour les comptes sensibles, et des corrections de bugs. Des refactorings importants ont été réalisés pour améliorer la maintenabilité du code et l'expérience utilisateur, en particulier sur les pages de gestion de projet et d'organisation. L'ajout d'un système de plugins a également été avancé.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (2FA) pour les comptes sensibles, avec possibilité de désactivation pour les comptes non sensibles. [#2262](https://github.com/betagouv/recommandations-collaboratives/issues/2262)
- Amélioration de la page des projets à faible portée : affichage d'un badge cohérent pour les recommandations non lues. [#2220](https://github.com/betagouv/recommandations-collaboratives/issues/2220)
- Possibilité de masquer le bouton de création de nouveau projet via un flag. [#2205](https://github.com/betagouv/recommandations-collaboratives/issues/2205)
- Ajout d'informations sur la personne ayant mis en pause un projet. [#2237](https://github.com/betagouv/recommandations-collaboratives/issues/2237)
- Amélioration de l'interface de fusion d'organisations. [#2246](https://github.com/betagouv/recommandations-collaboratives/issues/2246)
- Ajout d'un indicateur visuel lors de la sélection d'une organisation suggérée.
- Amélioration de l'affichage des filtres et ajout d'un filtre "sans tâche".
- Ajout d'une nouvelle icône pour les notifications.
- Amélioration de la gestion des erreurs et des validations de formulaire.

### Évolutions techniques
- Refactorings importants du code, notamment sur les pages de gestion de projet et d'organisation, pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de plusieurs dépendances, incluant Wagtail (7.0.8), dompurify (3.4.11), soupsieve (2.8.4) et mistune (3.3.0).
- Migration vers `uv` pour la gestion des dépendances Docker.
- Amélioration de la gestion des plugins : correction de bugs, documentation et amélioration de la sécurité.
- Suppression de `requirements.txt` et utilisation de `Pipfile` et `Pipfile.lock`.
- Amélioration de la configuration de Vite pour les plugins.
- Correction de problèmes liés à l'importation de fichiers dans le formulaire "pousse-reco".
- Suppression de code inutilisé et nettoyage général du code.
- Amélioration des tests, notamment pour l'authentification et les plugins.
- Refactorisation de la navigation avec des onglets.
- Optimisation des requêtes SQL pour éviter les problèmes de performance (N+1 queries).

### Autres changements
- Mise à jour de la documentation pour les plugins.
- Ajout de commentaires et de documentation dans le code.
- Correction de typos et amélioration de la qualité du code.
- Mise à jour des messages d'erreur et d'information.
- Ajout de tests unitaires pour certaines fonctionnalités.
- Correction de problèmes liés à la configuration de l'environnement de développement.
- Suppression de dépendances inutilisées.
- Amélioration de l'accessibilité de certains composants.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour du fichier `.gitignore`.
- Ajout d'un flag pour désactiver le bouton de soumission de nouveau projet.
- Correction de problèmes liés à la gestion des cookies Sesame.
- Amélioration de la gestion des erreurs de validation d'email.
- Ajout de la possibilité de valider les emails Brevo.
- Suppression de code redondant.
- Amélioration de la gestion des erreurs dans les tests.
- Correction de problèmes liés à l'affichage des informations de projet.
- Ajout de commentaires pour expliquer le code.
- Mise à jour des messages d'erreur.
- Correction de bugs mineurs.
- Amélioration de la gestion des erreurs dans les tests.
- Correction de problèmes liés à l'affichage des informations de projet.
- Ajout de commentaires pour expliquer le code.
- Mise à jour des messages d'erreur.
- Correction de bugs mineurs.
- Ajout de tests unitaires pour certaines fonctionnalités.
- Correction de problèmes liés à la configuration de l'environnement de développement.
- Suppression de dépendances inutilisées.
- Amélioration de l'accessibilité de certains composants.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour du fichier `.gitignore`.
- Ajout d'un flag pour désactiver le bouton de soumission de nouveau projet.
- Correction de problèmes liés à la gestion des cookies Sesame.
- Amélioration de la gestion des erreurs de validation d'email.
- Ajout de la possibilité de valider les emails Brevo.
- Suppression de code redondant.
- Amélioration de la gestion des erreurs dans les tests.
- Correction de problèmes liés à l'affichage des informations de projet.
- Ajout de commentaires pour expliquer le code.
- Mise à jour des messages d'erreur.
- Correction de bugs mineurs.
- Ajout de tests unitaires pour certaines fonctionnalités.
- Correction de problèmes liés à la configuration de l'environnement de développement.
- Suppression de dépendances inutilisées.
- Amélioration de l'accessibilité de certains composants.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour du fichier `.gitignore`.
- Ajout d'un flag pour désactiver le bouton de soumission de nouveau projet.
- Correction de problèmes liés à la gestion des cookies Sesame.
- Amélioration de la gestion des erreurs de validation d'email.
- Ajout de la possibilité de valider les emails Brevo.
- Suppression de code redondant.
- Amélioration de la gestion des erreurs dans les tests.
- Correction de problèmes liés à l'affichage des informations de projet.
- Ajout de commentaires pour expliquer le code.
- Mise à jour des messages d'erreur.
- Correction de bugs mineurs.
- Ajout de tests unitaires pour certaines fonctionnalités.
- Correction de problèmes liés à la configuration de l'environnement de développement.
- Suppression de dépendances inutilisées.
- Amélioration de l'accessibilité de certains composants.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour du fichier `.gitignore`.
- Ajout d'un flag pour désactiver le bouton de soumission de nouveau projet.
- Correction de problèmes liés à la gestion des cookies Sesame.
- Amélioration de la gestion des erreurs de validation d'email.
- Ajout de la possibilité de valider les emails Brevo.
- Suppression de code redondant.
- Amélioration de la gestion des erreurs dans les tests.
- Correction de problèmes liés à l'affichage des informations de projet.
