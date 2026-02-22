## Changelog : sylvasan (30 derniers jours)

### Résumé
Les dernières semaines ont été consacrées à la mise en place de l'infrastructure de base pour l'application mobile et à l'amélioration de l'authentification et de la gestion des requêtes.  Des ajustements ont également été faits pour préparer le déploiement et faciliter le développement futur.

### Évolutions fonctionnelles
- Implémentation d'un système de notification pour l'application.
- Authentification via token sur l'application mobile. #7ce384f
- Amélioration de la page d'accueil de l'application mobile. #5a5b54a
- Correction des routes de l'application mobile. #55c0444
- Ajout d'un mécanisme de retry automatique pour les requêtes échouant à cause d'un token expiré. #203f1e9

### Évolutions techniques
- Refonte de l'authentification : utilisation du store d'authentification et renommage de la fonction `custom fetch`. #f584330
- Factorisation des fonctions de thème pour une meilleure organisation du code. #783e136
- Déplacement du backend vers la plateforme et ajout d'une nouvelle interface utilisateur sur le frontend web. #b21dfd0
- Mise en place du routage basé sur des fichiers. #6e7fea2
- Utilisation de `useTitle` et d'un endpoint pour le token CSRF. #5bb3c12
- Ajout de Tailwind CSS et DSFR pour l'application mobile. #45d4b30
- Première compilation Android de l'application mobile. #59d674c
- Placement des fichiers statiques à l'intérieur du répertoire `src`. #5ec0ff2
- Mise en place de la structure de base du projet. #904b0ef

### Autres changements
- Ajout de l'ADR 0001 (Architectural Decision Record). #bf1ca4b
- Mise à jour du fichier README.md. #56804ae, #5169c7f
