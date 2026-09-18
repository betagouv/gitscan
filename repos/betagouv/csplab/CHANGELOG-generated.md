## Changelog : csplab (30 derniers jours, au 17 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes majeures dans la gestion des organisations et des équipes de recrutement. L'accent a été mis sur la robustesse de l'infrastructure avec l'intégration du stockage S3 et de la gestion des secrets Scaleway, ainsi que sur une refonte architecturale (ADR-009) visant à simplifier le code. Les fonctionnalités de gestion des membres et des processus de recrutement ont été considérablement enrichies pour offrir un contrôle plus fin aux utilisateurs.

### Évolutions fonctionnelles
- **Gestion des recrutements et des équipes** : 
    - Possibilité d'ajouter, modifier ou révoquer des membres au sein d'une équipe de recrutement, avec une gestion précise des rôles [#1445](https://github.com/betagouv/csplab/issues/1445), [#1416](https://github.com/betagouv/csplab/issues/1416), [#1412](https://github.com/betagouv/csplab/issues/1412), [#1409](https://github.com/betagouv/csplab/issues/1409).
    - Gestion des motifs de refus pour les candidatures [#1432](https://github.com/betagouv/csplab/issues/1432), [#1431](https://github.com/betagouv/csplab/issues/1431).
    - Assignation de responsables sur plusieurs recrutements d'un organisme simultanément [#1452](https://github.com/betagouv/csplab/issues/1452).
- **Gestion des organismes** : 
    - Nouvelles capacités de création, modification, consultation détaillée et suppression d'organismes [#1386](https://github.com/betagouv/csplab/issues/1386), [#1291](https://github.com/betagouv/csplab/issues/1291), [#1290](https://github.com/betagouv/csplab/issues/1290), [#1283](https://github.com/betagouv/csplab/issues/1283), [#1208](https://github.com/betagouv/csplab/issues/1208).
    - Gestion des membres rattachés aux organismes (ajout, modification et révocation de rôles) [#1273](https://github.com/betagouv/csplab/issues/1273), [#1269](https://github.com/betagouv/csplab/issues/1269), [#1264](https://github.com/betagouv/csplab/issues/1264), [#1223](https://github.com/betagouv/csplab/issues/1223).
- **Identité et Expérience Utilisateur** : 
    - Amélioration de l'identité avec la récupération automatique du nom et du prénom via ProConnect [#1451](https://github.com/betagouv/csplab/issues/1451) et la normalisation des emails en minuscules pour éviter les erreurs de recherche [#1471](https://github.com/betagouv/csplab/issues/1471).
    - Redirection automatique vers la page de connexion après une déconnexion [#1384](https://github.com/betagouv/csplab/issues/1384).
- **Ingestion de données** : 
    - Enrichissement du pipeline d'ingestion avec l'import des organismes de la DILA [#1262](https://github.com/betagouv/csplab/issues/1262) et des établissements FINESS [#1190](https://github.com/betagouv/csplab/issues/1190).
    - Amélioration du mapping et du transcodage des données issues de TalentSoft [#1411](https://github.com/betagouv/csplab/issues/1411), [#1403](https://github.com/betagouv/csplab/issues/1403).

### Évolutions techniques
- **Infrastructure et Stockage** : 
    - Mise en place du stockage S3 pour la gestion des documents des candidats [#1473](https://github.com/betagouv/csplab/issues/1473), [#1472](https://github.com/betagouv/csplab/issues/1472).
    - Intégration de la gestion des secrets via Scaleway Secret Manager pour les différents composants (web, ingestion, ocr) [#1302](https://github.com/betagouv/csplab/issues/1302), [#1301](https://github.com/betagouv/csplab/issues/1301), [#1280](https://github.com/betagouv/csplab/issues/1280).
- **Architecture (ADR-009)** : 
    - Refonte majeure pour revenir à un usage plus idiomatique de Django, simplifiant la structure globale du projet [#1305](https://github.com/betagouv/csplab/issues/1305).
    - Généralisation de l'utilisation de "factories" pour la génération de données de test sur l'ensemble des contextes (identitée, recrutement, ingestion, etc.) [#1362](https://github.com/betagouv/csplab/issues/1362), [#1363](https://github.com/betagouv/csplab/issues/1363), [#1364](https://github.com/betagouv/csplab/issues/1364), [#1365](https://github.com/betagouv/csplab/issues/1365), [#1371](https://github.com/betagouv/csplab/issues/1371), [#1400](https://github.com/betagouv/csplab/issues/1400).
- **Qualité et Tests** : 
    - Renforcement de la stratégie de tests avec l'introduction de `testing-library` pour le frontend [#1481](https://github.com/betagouv/csplab/issues/1481) et l'optimisation des tests backend via `pytest-xdist` avec des bases Redis dédiées [#1448](https://github.com/betagouv/csplab/issues/1448).
- **Outils et CI/CD** : 
    - Migration vers les *Conventional Commits* pour automatiser la génération du changelog et des releases [#1415](https://github.com/betagouv/csplab/issues/1415), [#1444](https://github.com/betagouv/csplab/issues/1444).
    - Adoption de `mise` pour la gestion unifiée des outils de développement et des tâches de workflow [#1332](https://github.com/betagouv/csplab/issues/1332), [#1276](https://github.com/betagouv/csplab/issues/1276).

### Autres changements
- **Documentation** : Mise à jour de la documentation technique concernant la gestion des secrets Scaleway [#1410](https://github.com/betagouv/csplab/issues/1410) et la documentation du rate limiting dans l'API OpenAPI [#1345](https://github.com/betagouv/csplab/issues/1345).
- **Nettoyage** : Refactorisation de divers enums et renommage de méthodes pour améliorer la cohérence du code [#1428](https://github.com/betagouv/csplab/issues/1428), [#1314](https://github.com/betagouv/csplab/issues/1314).
