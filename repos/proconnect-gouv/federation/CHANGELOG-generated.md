## Changelog : federation (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'importantes améliorations de sécurité, notamment sur la gestion des codes de vérification (OTP) et la robustesse des sessions MFA. Les processus d'authentification ont été affinés pour être plus fluides, tandis que l'infrastructure technique a été optimisée pour faciliter le déploiement et la maintenance.

### Évolutions fonctionnelles
- **Amélioration de la gestion des codes OTP** : mise en place de modèles d'e-mails dédiés, raccourcissement de la longueur des codes et clarification des objets d'e-mails pour une meilleure expérience utilisateur ([#1477](https://github.com/proconnect-gouv/federation/issues/1477), [#1482](https://github.com/proconnect-gouv/federation/issues/1482)).
- **Optimisation de la vérification d'e-mail** : le renvoi d'e-mail de vérification ne se fait désormais que sur demande explicite ([#1458](https://github.com/proconnect-gouv/federation/issues/1458)) et un seul jeton de vérification est autorisé par utilisateur ([#1446](https://github.com/proconnect-gouv/federation/issues/1446)).
- **Améliorations de l'interface et de la clarté** : 
    - Renommage de "Fournisseur de données" en "Serveur de ressources" pour une terminologie plus précise ([#1484](https://github.com/proconnect-gouv/federation/issues/1484)).
    - Correction d'un problème de navigation bloquant le bouton "retour" suite à des restrictions de sécurité CSP ([#1544](https://github.com/proconnect-gouv/federation/issues/1544)).
    - Correction du calcul du compte à rebours d'expiration ([#1528](https://github.com/proconnect-gouv/federation/issues/1528)).
- **Administration** : les domaines d'e-mails sont désormais bloqués par défaut lors de la création d'un fournisseur d'identité (IdP) dans l'interface d'administration ([#1476](https://github.com/proconnect-gouv/federation/issues/1476)).

### Évolutions techniques
- **Sécurité et Protocoles** : 
    - Réutilisation des sessions MFA lorsque les exigences d'authentification sont satisfaites ([#1450](https://github.com/proconnect-gouv/federation/issues/1450)).
    - Simplification des serveurs de ressources par la suppression de l'encryption et de l'URL JWKS ([#1487](https://github.com/proconnect-gouv/federation/issues/1487)).
- **Gestion des erreurs** : migration vers un système de filtres d'exceptions NestJS standardisé et nettoyage des préfixes de messages d'erreur pour plus de clarté ([#1438](https://github.com/proconnect-gouv/federation/issues/1438), [#1545](https://github.com/proconnect-gouv/federation/issues/1545)).
- **Infrastructure et CI/CD** : 
    - Optimisation des Dockerfiles (build multi-étapes) et intégration des assets/CSS dans l'image du backend ([#1452](https://github.com/proconnect-gouv/federation/issues/1452), [#1529](https://github.com/proconnect-gouv/federation/issues/1529)).
    - Résolution d'erreurs de communication avec Grist lors des tests en CI ([#1546](https://github.com/proconnect-gouv/federation/issues/1546)).
    - Amélioration de la gestion de la base de données pour les tests E2E (utilisation de `TRUNCATE` au lieu de clones) ([#1449](https://github.com/proconnect-gouv/federation/issues/1449)).
- **Base de données et Migrations** : refonte du processus de seeding et de migration pour l'environnement de développement ([#1455](https://github.com/proconnect-gouv/federation/issues/1455)) et automatisation de l'exécution des migrations via un hook de démarrage ([#1453](https://github.com/proconnect-gouv/federation/issues/1453)).
- **Refactoring** : amélioration de la lisibilité de l'algorithme de recherche d'utilisateurs ([#1478](https://github.com/proconnect-gouv/federation/issues/1478)) et restructuration de l'application `csmr-rie` en application autonome ([#1428](https://github.com/proconnect-gouv/federation/issues/1428)).

### Autres changements
- Mise à jour de la documentation du projet (README) ([#1448](https://github.com/proconnect-gouv/federation/issues/1448)).
