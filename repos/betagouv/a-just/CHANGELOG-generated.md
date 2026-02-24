## Changelog : a-just (30 derniers jours)

### Résumé
Ce changelog couvre les 30 derniers jours d'évolution du projet a-just. Les principales améliorations concernent le cockpit (nouvelle interface), l'extracteur de données (collecte 2026) et les tests automatisés (E2E et unitaires). Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment au niveau de l'affichage des données et de la gestion des exports.

### Évolutions fonctionnelles
- Amélioration de l'interface du cockpit avec l'ajout de données et la gestion des popins d'alerte. (#27ef49b2)
- Correction de l'affichage des ratios dans le simulateur. (#87f8484d)
- Correction de l'affichage des entrées projetées dans le simulateur. (#286ab202, #7fea3c7e)
- Correction de l'affichage des libellés. (#a6c50373, #cc5bba57)
- Restauration de la journalisation (log) manquante pour l'exécution de l'extracteur. (#53cc9d4e, #de7bfe45)
- Amélioration de la gestion des options de sélection "Attachés de Justice" pour la collecte CA. (#3f0e4ea2)
- Limitation des options du menu déroulant "Attachés de Justice" à "Siège autres" et "Parquet" pour la collecte CA. (#3f0e4ea2)
- Correction de l'affichage des valeurs dans les tableaux Excel exportés. (#de773ace, #541b5d27)

### Évolutions techniques
- Mise à jour de l'extracteur de données pour la collecte 2026 avec corrections et ajout de nouveaux fichiers Excel. (#446, #445, #444, #440, #3fc35ef0)
- Refonte de l'architecture des tests E2E avec amélioration de la configuration, de la gestion des rapports et de l'intégration continue (CI/CD). (#f81d4ac9, #9ca40100, #f37dc2fb, #8998c232, #3457b485, #f0f030b7, #9d77b7de)
- Correction de tests unitaires et d'intégration. (#449, #bb0671cb)
- Amélioration de la gestion des erreurs et des logs dans les tests E2E. (#7d34f2c0, #60a6cce6, #9a31fa0f)
- Correction de problèmes de mémoire lors de l'exécution des tests E2E sur GitHub Actions. (#48dcdca0)
- Mise à jour des images Cypress utilisées pour les tests E2E. (#29c6b59c)
- Ajout de scripts d'anonymisation de la base de données. (#425, #413, #409, #406, #405)
- Amélioration de la gestion des CORS et de l'authentification SSO. (#7370abd7)
- Suppression du rounding côté backend pour corriger les problèmes de valeurs négatives dans Excel. (#cd5c1e79)
- Ajout de MAX flooring aux formules Excel pour gérer les valeurs négatives. (#541b5d27)

### Autres changements
- Mise à jour de la documentation.
- Nettoyage du code et suppression de fichiers inutiles.
- Correction de noms de tests. (#97576513)
- Amélioration des messages de log.
- Correction de la configuration des tests.
- Mise à jour de la version du projet. (#1d19d4f2)
- Amélioration de la gestion des fichiers dans les jobs CI/CD. (#dcefee82)
- Ajout de fichiers de configuration pour les tests. (#2559ffdb)
- Correction de la gestion des chemins de fichiers dans les jobs CI/CD. (#2edbacb4)
- Ajout de fichiers package-lock.json pour le frontend. (#e08083b8, #63155ad8)
- Amélioration des messages d'erreur et des logs.
