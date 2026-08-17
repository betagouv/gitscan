## Changelog : complements-alimentaires (30 derniers jours, au 15 août 2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'une modernisation majeure de son architecture frontend avec le passage à Vite, visant à améliorer les performances de développement et de build. Des corrections ont également été apportées pour fiabiliser l'export de fichiers Excel et le processus de création d'entreprise.

### Évolutions fonctionnelles
- Correction de l'URL de téléchargement pour les fichiers Excel [#3064](https://github.com/betagouv/complements-alimentaires/pull/3064).
- Résolution d'un bug impactant le composant de création d'entreprise [#3063](https://github.com/betagouv/complements-alimentaires/pull/3063).

### Évolutions techniques
- **Migration Frontend** : Passage à une architecture basée sur Vite [#3050](https://github.com/betagouv/complements-alimentaires/pull/3050), incluant la transition vers `type:module` et la suppression d'ESLint.
- **Optimisation API** : Centralisation des appels API via `createFetch` pour une gestion unifiée des credentials et de l'URL racine.
- **CI/CD & Build** : 
    - Ajout d'un workflow GitHub Actions dédié au build du frontend.
    - Optimisation du Dockerfile (suppression de code inutile) et ajout d'un fichier `env.example`.
- **Configuration** : Généralisation de l'utilisation des variables d'environnement pour la gestion des URLs (API et backend).

### Autres changements
- **Nettoyage** : Suppression de bibliothèques obsolètes (`python.json`, `deprecated`, `wrapt`) et de tâches de build inutilisées.
- **Documentation** : Mise à jour du README.
- **Configuration serveur** : Ajout d'un fichier `.htaccess` et déplacement du fichier `robots.txt`.
- **Gestion de version** : Modification de la stratégie de gestion du dossier `dist` pour permettre son maintien en version.
