## Changelog : ami-notifications-api (30 derniers jours, au 24 juin 2026)

### Résumé
Ce changelog présente les évolutions récentes de l'API de gestion des notifications de l'application mobile interministérielle (AMI). Les améliorations concernent principalement l'affichage des icônes de notifications, la gestion des liens profonds (deep links) vers des éléments spécifiques, l'archivage des suivis, l'intégration d'un nouveau système d'authentification FranceConnect FI et des corrections pour améliorer la stabilité et la performance.

### Évolutions fonctionnelles
- **Notifications :** Amélioration de l'affichage des icônes des notifications. L'API tente désormais de deviner l'icône à partir de l'icône enregistrée et du partenaire, et stocke l'icône brute pour une plus grande flexibilité. L'icône de l'élément de suivi est également renvoyée. [#952]
- **Suivis :** Ajout de la possibilité d'archiver les suivis (follow-up) avec une nouvelle interface utilisateur et une nouvelle API dédiée. Les suivis archivés sont désormais masqués par défaut. [#776]
- **Authentification :** Implémentation d'un nouveau flux d'authentification via FranceConnect FI, incluant la gestion des sessions, des tokens et des informations utilisateur.  Une page de test a été ajoutée pour faciliter le développement et les tests. [#917, #907, #708]
- **Gestion des adresses :** Amélioration de la gestion des adresses dans les préférences utilisateur, avec la possibilité de les ajouter, les supprimer et de les sélectionner facilement. [#789]
- **Liens profonds :** Amélioration de la gestion des liens profonds pour les suivis, permettant de naviguer directement vers un suivi spécifique. [#690]
- **Notifications expirées :** L'API exclut désormais les notifications avec une date de validité dépassée. [#674]

### Évolutions techniques
- **Performance :** Optimisation de la requête de liste des notifications en utilisant `select_related` pour réduire le nombre de requêtes à la base de données. [#952]
- **Architecture :** Utilisation de `django-tasks-db` pour la gestion des tâches asynchrones, améliorant la robustesse et la scalabilité. [#956]
- **Configuration :** Utilisation de variables d'environnement pour la configuration, notamment pour l'URL de base du proxy FranceConnect FI. [#708, #905]
- **Tests :** Suppression des timeouts inutiles dans les tests unitaires. [#789]
- **Outils :** Mise à jour de certaines dépendances (uv, webob, esbuild, svelte, etc.).
- **Code :** Suppression de code inutile et refactorisation de certains composants de l'interface utilisateur.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'API.
- **Gitignore :** Correction du fichier `.gitignore` pour ignorer correctement les répertoires de build de l'application mobile.
- **Replication :** Ajout de l'ID utilisateur dans l'anonymisation des enregistrements et des notifications lors de la réplication. [#964]
- **Gestion des logs :** Amélioration de la gestion des logs pour faciliter le débogage et le suivi des erreurs.
- **Correction d'un bug :** Correction d'un problème d'erreur d'intégrité lors de la déconnexion. [#971]
- **Correction d'un bug :** Correction d'un bug empêchant l'affichage correct des données du quotient familial après la connexion via ami-fi. [#907]
- **Accessibilité :** Correction d'un problème d'accessibilité lié aux images avec des attributs `alt` ou `aria-label` vides. [#924]
- **Suppression de code obsolète :** Suppression de code obsolète et de fichiers inutiles.
