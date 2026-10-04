## Changelog : tchap-x-ios (30 derniers jours, au 21 septembre 2026)

### Résumé
Cette période a été principalement consacrée à l'épuration de l'interface utilisateur et à une mise à jour technique majeure. Plusieurs bannières d'information ont été retirées pour simplifier l'expérience, tandis que l'application a bénéficié d'une intégration importante de nouvelles bases de code (rebase) pour garantir sa stabilité et sa compatibilité avec les derniers outils de développement.

### Évolutions fonctionnelles
- **Interface utilisateur et design** :
    - Nettoyage de l'interface par la suppression de plusieurs bannières d'information (réinitialisation d'identité, nouveau son, et avertissement sur l'authenticité).
    - Amélioration visuelle des badges (couleurs et styles) et de leur intégration dans l'en-tête des discussions.
    - Amélioration de la localisation française et correction de la typographie sur certains éléments de partage d'historique.
- **Sécurité et authentification** :
    - Amélioration de la fiabilité du scanner de contenu pour éviter les échecs de scan prématurés.
    - Rétablissement du code pour la gestion des comptes expirés.

### Évolutions techniques
- **Maintenance et architecture** :
    - Mise à jour majeure de la base de code via l'intégration de la version ElementX-iOS v26.08.2.
    - Mise en conformité de la gestion des cartes statiques pour la compatibilité avec Swift 6.2.
    - Implémentation d'un hook spécifique pour le scanner de contenu utilisant l'URL du serveur d'hébergement (homeserver).
- **Build et CI/CD** :
    - Optimisation du processus de déploiement par la désactivation des builds de vérification nocturnes (nightly checks) pour faciliter les releases.
    - Résolution de conflits de fusion et de problèmes de compilation Xcode suite aux opérations de rebase.

### Autres changements
- Mise à jour de la version de l'application et du changelog.
- Corrections diverses de fautes de frappe.
