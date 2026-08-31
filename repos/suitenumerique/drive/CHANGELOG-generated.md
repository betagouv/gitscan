## Changelog : drive (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité, notamment pour la détection de fichiers malveillants et la sécurisation de l'édition de documents en ligne. Des outils de gestion du stockage et des corrections d'interface ont également été déployés pour faciliter le travail des administrateurs et des utilisateurs.

### Évolutions fonctionnelles
- **Administration** : possibilité d'interrompre manuellement une analyse de malware en cours.
- **Gestion du stockage** : introduction d'un indicateur d'exclusion de quota sur les fichiers et d'une commande pour accorder un stockage illimité.
- **Sécurité** : scan automatique des fichiers écrits via le protocole d'édition en ligne (WOPI) pour détecter d'éventuels malwares.
- **Expérience utilisateur** : correction d'un bug de comportement lors du glisser-déposer dans la fenêtre de partage.
- **API** : application des attributs par audience aux éléments de l'API externe.

### Évolutions techniques
- **Sécurité WOPI** : renforcement de la validation des signatures de requêtes, gestion des clés de preuve client et sécurisation des processus de renommage de fichiers.
- **Sécurité Backend** : mise en place d'une liste blanche statique pour la résolution des fichiers de modèles.
- **Infrastructure & CI/CD** : mise à jour des environnements de build vers Node 22 et passage de l'image Docker frontend sur Alpine 3.24.
- **Automatisation** : planification des commandes de réconciliation pour la détection de malwares via Helm.

### Autres changements
- **Documentation** : mise à jour des notes de version concernant les fonctionnalités d'exclusion de quota.
- **Maintenance** : normalisation des fins de ligne dans le fichier `yarn.lock`.
