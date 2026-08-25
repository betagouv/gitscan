## Changelog : accounts (30 derniers jours, au 24 août 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience de déconnexion des utilisateurs, la modernisation de la structure des données via l'adoption de l'UUID v7, et le renforcement de la fiabilité des déploiements et des tests automatisés.

### Évolutions fonctionnelles
- **Authentification** : Amélioration du processus de déconnexion (OIDC) en transmettant la confirmation de déconnexion initiée par le client (RP) vers l'interface utilisateur.

### Évolutions techniques
- **Base de données** : Migration des clés primaires vers le format UUID Version 7 pour une meilleure gestion des identifiants.
- **Infrastructure et Déploiement** :
    - Optimisation des déploiements Helm (mise à jour des valeurs de développement et restriction du déploiement à la branche principale).
    - Correction de la configuration Docker pour le composant `link-collector` afin d'éviter l'écrasement du répertoire `/app`.
- **Tests** :
    - Renforcement de la robustesse des tests (gestion de l'invalidation du cache, tests de repli lors d'erreurs d'introspection).
    - Automatisation du marquage de la base de données Django pour les tests `pytest`.

### Autres changements
- **Nettoyage** : Suppression de configurations et de fichiers d'environnement inutilisés et réorganisation des clés de configuration.
- **Documentation** : Mise à jour et correction du fichier changelog.
