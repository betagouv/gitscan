## Changelog : complements-alimentaires (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des visas, notamment avec l'ajout d'une fonctionnalité d'approbation automatique et une interface utilisateur dédiée. De nombreuses mises à jour de dépendances ont également été intégrées pour assurer la sécurité et la stabilité du projet. Des améliorations ont été apportées à la composition des PDF générés, notamment la correction de l'affichage des symboles et l'ajout d'un compteur de pages.

### Évolutions fonctionnelles
- **Visa automatique :** Implémentation d'une fonctionnalité d'approbation automatique des visas, avec une interface utilisateur dédiée pour la gestion.
- **Composition PDF :** Amélioration de la composition des PDF générés, incluant la correction de l'affichage des symboles (remplacement du symbole micro par une « u ») et l'ajout d'un compteur de pages.
- **Fixtures :** Ajout de fixtures pour faciliter les tests et le développement.
- **Suppression des notebooks :** Suppression des notebooks inutiles du dépôt.

### Évolutions techniques
- **Mises à jour de dépendances :** De nombreuses dépendances ont été mises à jour vers leurs dernières versions stables, notamment :
    - Django (6.0.4 -> 6.0.5)
    - pypdf (6.10.2 -> 6.11.0)
    - lxml (6.0.2 -> 6.1.0)
    - sentry-sdk (2.49.0 -> 2.58.0)
    - pandas (3.0.0 -> 3.0.2)
    - ruff (0.15.10 -> 0.15.12)
    - chardet (7.4.2 -> 7.4.3)
    - sqlfluff (4.0.0 -> 4.1.0)
    - redis (7.3.0 -> 7.4.0)
    - botocore (1.42.47 -> 1.42.97)
    - cryptography (46.0.7 -> 47.0.0)
    - numpy (2.4.3 -> 2.4.4)
    - urllib3 (2.6.3 -> 2.7.0)
    - platformdirs (4.5.0 -> 4.9.6)
    - wcwidth (0.6.0 -> 0.7.0)
    - ipython (9.11.0 -> 9.13.0)
    - django-hijack (3.7.6 -> 3.7.8)
    - filelock (3.20.3 -> 3.29.0)
    - tinycss2 (1.4.0 -> 1.5.1)
- **Suppression de `ipdb` :** Suppression de l'outil de débogage `ipdb` et de ses dépendances.
- **Refactoring des tests :** Amélioration de la granularité des tests.
- **Mises à jour des actions GitHub :** Mise à jour des actions GitHub utilisées dans le workflow CI/CD.
- **Mises à jour des dépendances frontend :** Mises à jour de plusieurs dépendances frontend (Vue.js, Vue Router, PostCSS, TailwindCSS, etc.).

### Autres changements
- Correction de bugs mineurs et améliorations de la qualité du code.
- Documentation mise à jour.
- Suppression de fichiers inutiles.
- Amélioration de la gestion des paramètres pour l'auto-visa.
- Correction de l'affichage des polices dans les PDF.
