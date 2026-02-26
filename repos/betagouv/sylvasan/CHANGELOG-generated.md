## Changelog : sylvasan (30 derniers jours)

### Résumé
Les dernières semaines ont été consacrées à la mise en place de l'infrastructure de base pour une application mobile, ainsi qu'à des améliorations de l'authentification et de la gestion des requêtes. L'interface utilisateur web a également été partiellement migrée vers une nouvelle plateforme.

### Évolutions fonctionnelles
- Implémentation d'un système de notification pour l'application.
- Authentification via token sur l'application mobile. (#7ce384f)
- Amélioration de la page d'accueil de l'application mobile. (#5a5b54a)
- Correction des routes de l'application mobile. (#55c0444)
- Tentative automatique de relance des requêtes en cas d'expiration du token d'authentification. (#203f1e9)

### Évolutions techniques
- Migration du backend vers une nouvelle plateforme. (#b21dfd0)
- Ajout de Tailwind CSS et du Design System Fr pour l'application mobile. (#45d4b30)
- Première compilation de l'application pour Android. (#59d674c)
- Refactorisation des fonctions de thème. (#783e136)
- Utilisation du store d'authentification et renommage de la fonction `fetch` personnalisée. (#f584330)
- Mise en place d'un système de routage basé sur des fichiers. (#6e7fea2)
- Utilisation de `useTitle` et d'un endpoint pour le token CSRF. (#5bb3c12)
- Placement des fichiers statiques à l'intérieur du répertoire `src`. (#5ec0ff2)
- Mise en place de la structure de base du projet. (#904b0ef)

### Autres changements
- Ajout de l'ADR 0001. (#bf1ca4b)
- Mise à jour du fichier README.md. (#56804ae, #5169c7f)
