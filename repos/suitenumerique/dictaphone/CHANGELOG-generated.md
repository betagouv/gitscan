## Changelog : dictaphone (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, en particulier sur l'application mobile, avec des fonctionnalités comme la reprise d'enregistrement en cas de perte de connexion, la gestion des téléchargements en WiFi uniquement, et une meilleure gestion des erreurs. Des améliorations significatives ont également été apportées à la gestion des transcriptions, avec la possibilité de les régénérer et d'exporter au format SRT. Plusieurs corrections de bugs et optimisations de sécurité ont été implémentées.

### Évolutions fonctionnelles
- Ajout de la possibilité de régénérer une transcription échouée via l'interface d'administration et un nouvel endpoint dédié. [#issue à suivre]
- Ajout de l'export des transcriptions au format SRT. [#issue à suivre]
- Ajout de la possibilité de copier le texte de la transcription et d'ouvrir les documents associés (indocs) directement depuis le menu d'action du fichier. [#issue à suivre]
- Amélioration de l'interface utilisateur pour afficher la source et la durée des fichiers audio dans l'administration Django. [#issue à suivre]
- Ajout d'un indicateur visuel (tooltip) sur le bouton d'upload. [#issue à suivre]
- Amélioration de l'expérience utilisateur lors de la réinitialisation du mot de passe sur l'application mobile.
- Ajout de la possibilité de contourner l'écran de connexion sur l'application mobile.
- Ajout d'un support pour le regroupement de textes consécutifs du même intervenant dans les transcriptions (frontend et mobile).
- Amélioration de l'affichage des durées courtes dans l'interface utilisateur.
- Ajout d'un indicateur de progression lors du téléchargement des fichiers sur l'application mobile.
- Ajout d'une option pour n'autoriser les téléchargements qu'en WiFi sur l'application mobile.
- Amélioration de la gestion des erreurs et des alertes sur l'application mobile.
- Ajout d'un lien vers la salle Matrix pour la communauté. [#75733f8](https://github.com/suitenumerique/dictaphone/commit/75733f8)

### Évolutions techniques
- Mise à jour de Python à la version 3.14.5 et de Django à la version 5.12.4. [#c41aac4](https://github.com/suitenumerique/dictaphone/commit/c41aac4)
- Amélioration de la sécurité avec l'utilisation de `secrets.compare_digest` pour la comparaison de chaînes sensibles. [#4e8ce56](https://github.com/suitenumerique/dictaphone/commit/4e8ce56)
- Ajout de logs plus détaillés dans le processus de connexion pour faciliter le débogage des problèmes d'authentification mobile. [#600e899](https://github.com/suitenumerique/dictaphone/commit/600e899)
- Refactorisation du code mobile pour une meilleure organisation et lisibilité.
- Mise en place d'un script pour automatiser les releases de l'application mobile.
- Amélioration de la robustesse de la logique de gestion des enregistrements sur l'application mobile.
- Ajout d'une commande pour nettoyer les fichiers en attente et supprimés. [#f270029](https://github.com/suitenumerique/dictaphone/commit/f270029)
- Configuration de l'exécution de la commande de nettoyage des fichiers en tant que tâche cron. [#69a917b](https://github.com/suitenumerique/dictaphone/commit/69a917b)
- Activation du support vidéo par défaut. [#1ff013e](https://github.com/suitenumerique/dictaphone/commit/1ff013e)
- Amélioration de la gestion des erreurs et de la robustesse du code.

### Autres changements
- Mise à jour de la documentation pour l'utilisation de linter sur le code mobile.
- Mise à jour des documents légaux.
- Ajout d'un user agent spécifique pour les requêtes de l'application.
- Correction de typos et améliorations de la lisibilité de la documentation et du code.
- Amélioration de l'accessibilité de l'application frontend.
- Nettoyage et refactoring du code.
