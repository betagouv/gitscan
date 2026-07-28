## Changelog : apistration (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de la sécurité, notamment concernant la gestion des tokens éditeur et la protection contre les attaques. Des améliorations significatives ont également été apportées à l'expérience utilisateur pour les éditeurs, avec de nouvelles fonctionnalités de gestion des tokens et une meilleure documentation. Enfin, des corrections et des améliorations ont été apportées à l'accessibilité et à la documentation générale.

### Évolutions fonctionnelles
- **Gestion des tokens éditeur :** Les éditeurs peuvent désormais gérer leurs propres tokens d'API, incluant la création, la révocation, la prolongation et la modification des IPs autorisées. [#286](https://github.com/datagouv/apistration/pull/286)
- **Délégation d'accès :** Amélioration de la gestion de la délégation d'accès pour les éditeurs, avec une meilleure documentation et une intégration plus fluide. [#287](https://github.com/datagouv/apistration/pull/287)
- **API Particulier :** Ajout du numéro INE dans la réponse de l'API CNOUS v5. [#285](https://github.com/datagouv/apistration/pull/285)
- **API DGFIP TVA :** Clarification du titre de l'endpoint DGFIP TVA pour mieux indiquer son champ d'application français intra-communautaire. [#295](https://github.com/datagouv/apistration/pull/295)
- **Simplifions :** Intégration de Simplifions sur les sites API Particulier et API Entreprise, avec de nouvelles cartes et une refonte de la FAQ. [#235](https://github.com/datagouv/apistration/pull/235)
- **Hyperping :** Ajout d'une skill Hyperping pour gérer les incidents sur la page de statut. [#255](https://github.com/datagouv/apistration/pull/255)

### Évolutions techniques
- **Sécurité :**
    - Correction d'une vulnérabilité XSS potentielle dans les liens DataPass. [#240](https://github.com/datagouv/apistration/pull/240)
    - Protection contre les attaques de type tabnapping sur les liens DataPass. [#240](https://github.com/datagouv/apistration/pull/240)
    - Correction d'un problème de réutilisation de blacklist pour les tokens régénérés. [#248](https://github.com/datagouv/apistration/pull/248)
- **Refactoring :** Refactorisation du code pour améliorer la maintenabilité et la lisibilité, notamment dans la gestion de Simplifions. [#225](https://github.com/datagouv/apistration/pull/225)
- **Tests :** Amélioration de la couverture des tests, notamment pour l'API DGFIP TVA. [#236](https://github.com/datagouv/apistration/pull/236)
- **Dépendances :** Mise à jour de plusieurs dépendances, incluant Ruby, Rails, et les actions GitHub.
- **CI/CD :** Amélioration du workflow de déploiement pour l'environnement de staging. [#273](https://github.com/datagouv/apistration/pull/273)

### Autres changements
- **Documentation :** Amélioration de la documentation pour les API et les fonctionnalités, incluant la documentation de l'API Editor et des nouvelles fonctionnalités de gestion des tokens.
- **Accessibilité :** Nombreuses corrections pour améliorer l'accessibilité du site web, conformément aux normes RGAA. [#241](https://github.com/datagouv/apistration/pull/241)
- **Corrections de bugs :** Correction de divers bugs mineurs et améliorations de la stabilité.
- **Mises à jour de mocks :** Ajout et mise à jour des mocks pour les API CNOUS et ARS.
- **Nettoyage de code :** Suppression de code inutile et amélioration de la qualité du code.
