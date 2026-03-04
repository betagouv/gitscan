## Changelog : sylvasan (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes de SylvaSan, l'outil de suivi des problèmes sanitaires des arbres en forêt. Les dernières semaines ont été marquées par l'ajout de pages légales (mentions légales, données personnelles, cookies), l'amélioration de l'accessibilité, et la mise en place d'une infrastructure CI/CD plus robuste. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application. Le développement de l'application mobile progresse avec l'intégration de l'authentification et l'ajout de fonctionnalités de base.

### Évolutions fonctionnelles
- Ajout de la page « mentions légales » pour répondre aux obligations légales.
- Ajout de la page « données personnelles » informant les utilisateurs sur la gestion de leurs données.
- Ajout de la page « cookies » pour informer les utilisateurs sur l'utilisation des cookies par l'application.
- Ajout d'une déclaration d'accessibilité pour améliorer l'utilisation de l'application par tous les utilisateurs.
- Mise à jour du texte de la page d'accueil pour une meilleure clarté.
- Implémentation d'un système de notification.
- Mise en place de l'authentification et du routage de base pour l'application mobile.
- Ajout de la première version staging de l'application.
- Correction des routes de l'application mobile.
- Ajout d'un retry automatique pour les requêtes échouant à cause d'un token expiré.

### Évolutions techniques
- Mise en place d'une infrastructure CI/CD avec GitHub Actions pour automatiser les tests et le déploiement.
- Refonte de la structure du projet pour une meilleure organisation.
- Intégration de Tailwind CSS et du Design System de la GouvMinint pour l'application mobile.
- Première compilation Android de l'application mobile.
- Utilisation du store d'authentification et refactorisation de la fonction `fetch` personnalisée.
- Utilisation de l'authentification par token sur l'application mobile.
- Factorisation des fonctions de thème.
- Mise en place du routage basé sur des fichiers.
- Utilisation de `useTitle` et d'un endpoint pour le token CSRF.
- Ajout d'un ADR (Architectural Decision Record) pour documenter les choix d'architecture.
- Mise à jour de plusieurs dépendances : Vue, Vue Router, Tailwind CSS, Capacitor, Django, et autres.
- Ajout de tests unitaires pour l'application mobile et le backend.
- Ajout de fichiers `.yml` pour les workflows GitHub Actions.

### Autres changements
- Mise à jour du fichier `README.md` avec des informations plus précises.
- Suppression temporaire des settings liés à l'email.
- Ajout de fichiers statiques à l'intérieur du dossier `src`.
- Ajout d'un fichier `.htaccess` pour le déploiement web.
- Correction de coquilles dans le code.
- Whitelist des chemins d'analyse.
- Ignorer les fichiers Kotlin et Swift lors de l'analyse.
- Ajout de variables d'environnement nécessaires.
- Ajustements aux fichiers à ignorer et ajout des variables d'environnement.
