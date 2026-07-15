## Changelog : complements-alimentaires (30 derniers jours, au 07 juillet 2026)

### Résumé
Cette période a été marquée par une mise à jour importante des dépendances du projet, tant côté frontend (React, Vue.js, Node.js) que backend (Python, Django, Redis).  Une simplification du code a été effectuée en supprimant une librairie non utilisée. Des validations backend ont été ajoutées en préparation de la gestion de la visa obligatoire pour certains articles.

### Évolutions fonctionnelles
- Ajout de validations côté backend en préparation de la gestion de la visa obligatoire pour les articles 16 et 18. [#2996](https://github.com/betagouv/complements-alimentaires/pull/2996)

### Évolutions techniques
- Suppression de la librairie `beautifulsoup4` et de ses dépendances, simplifiant ainsi le code. [#2977](https://github.com/betagouv/complements-alimentaires/pull/2977)
- Mise à jour de nombreuses dépendances :
    - Redis (7.4.0 -> 8.0.0)
    - Django-webpack-loader (3.2.3 -> 3.2.4)
    - pikepdf (10.5.1 -> 10.9.1)
    - regex (2026.5.9 -> 2026.6.28)
    - sentry-sdk (2.60.0 -> 2.63.0)
    - tzlocal (5.3.1 -> 5.4.3)
    - uritools (6.0.1 -> 6.1.2)
    - pandas (3.0.2 -> 3.0.3)
    - pypdf (6.12.0 -> 6.13.3)
    - numpy (2.4.4 -> 2.4.6)
    - cryptography (48.0.0 -> 48.0.1)
    - bleach (6.3.0 -> 6.4.0)
- Mises à jour des dépendances frontend (React, Vue.js, PostCSS, TailwindCSS, etc.) pour bénéficier des dernières corrections et améliorations.

### Autres changements
- Mise à jour des actions GitHub utilisées pour le CI/CD.
- Corrections de tests.
- Amélioration de la configuration du projet.
