## Changelog : docs (30 derniers jours, au 7 mai 2026)

### Résumé
Ce changelog couvre les 30 derniers jours d'évolution du projet Docs. Les améliorations se concentrent sur la stabilité et la performance, notamment avec la migration vers de nouveaux outils de construction et de gestion des dépendances (uv et uv_build). Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, en particulier concernant la collaboration en temps réel, la gestion des liens internes et la gestion des erreurs. Enfin, la sécurité a été renforcée avec des mises à jour de dépendances.

### Évolutions fonctionnelles
- Ajout d'un lien vers la documentation dans le menu d'aide. [#2222](https://github.com/suitenumerique/docs/issues/2222)
- Amélioration de l'expérience utilisateur des liens internes (interlinking) avec une interface plus claire et des corrections de bugs. [#2213](https://github.com/suitenumerique/docs/issues/2213)
- Ajout de la possibilité d'utiliser un nouveau service d'IA (Mistral) pour certaines fonctionnalités. [#2193](https://github.com/suitenumerique/docs/issues/2193)
- Amélioration de la gestion des erreurs 5xx avec une structure d'alerte plus accessible. [#2128](https://github.com/suitenumerique/docs/issues/2128)
- Ajout du support hors ligne pour le contenu.
- Amélioration de la gestion des membres sur les petits écrans. [#2226](https://github.com/suitenumerique/docs/issues/2226)

### Évolutions techniques
- Migration de l'outil de construction de Python `setuptools` vers `uv_build` et de la gestion des dépendances `pip` vers `uv`. [#2276](https://github.com/suitenumerique/docs/issues/2276)
- Mise à jour de plusieurs dépendances, incluant `axios`, `lxml`, `uuid` et les dépendances Python, pour corriger des failles de sécurité et bénéficier des dernières améliorations.
- Refactorisation du code backend pour améliorer la performance et la maintenabilité, notamment en séparant le module `core/utils.py`.
- Implémentation d'en-têtes `etag` et `last_modified` pour optimiser la récupération du contenu.
- Utilisation de `uvicorn` pour exécuter l'application Django en environnement de développement.
- Amélioration de la gestion des requêtes asynchrones et de la concurrence pour éviter les blocages lors de la création de documents.
- Mise à jour de Docspec vers la version 3.0.x et adaptation de l'API du convertisseur. [#2220](https://github.com/suitenumerique/docs/issues/2220)
- Refactorisation des tests E2E pour une meilleure organisation et fiabilité.

### Autres changements
- Correction de fautes de frappe dans le fichier `contributing.md`.
- Mise à jour des chaînes de traduction.
- Ajout d'un favicon par défaut.
- Amélioration de la gestion des erreurs et des redirections après authentification.
- Suppression de points de terminaison obsolètes.
- Ajout d'une configuration pour l'URI de la requête d'authentification forward.
- Amélioration de la gestion des tests et de l'intégration continue.
- Correction de bugs mineurs et améliorations de la qualité du code.
