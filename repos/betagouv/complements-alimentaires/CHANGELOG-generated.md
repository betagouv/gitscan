## Changelog : complements-alimentaires (30 derniers jours, au 26 mai 2026)

### Résumé
Cette période a été marquée par des mises à jour de dépendances pour assurer la sécurité et la stabilité du projet. Des améliorations fonctionnelles ont été apportées concernant la gestion des informations sur les compléments alimentaires, notamment en affinant l'affichage des champs pour les plantes et en permettant l'export des contacts. Des corrections et refactorisations ont également été effectuées pour améliorer la qualité du code.

### Évolutions fonctionnelles
- Amélioration de l'affichage des champs relatifs aux plantes : les informations additionnelles pour les plantes inactives sont désormais optionnelles [#2884](https://github.com/betagouv/complements-alimentaires/pull/2884).
- Implémentation de l'export des contacts par email [#2870](https://github.com/betagouv/complements-alimentaires/pull/2870).
- Mise en place d'un système de visa automatique [#2883](https://github.com/betagouv/complements-alimentaires/pull/2883).
- Possibilité de générer un PDF de la composition d'un complément alimentaire [#2854](https://github.com/betagouv/complements-alimentaires/pull/2854).

### Évolutions techniques
- Mise à jour de nombreuses dépendances :
    - `cryptography` vers la version 48.0.0
    - `requests` vers la version 2.34.2
    - `pytz` vers la version 2026.2
    - `psycopg2` vers la version 2.9.12
    - `vue` vers la version 3.5.34
    - `vue-router` vers la version 5.0.7
    - `tailwindcss` vers la version 4.3.0
    - `numpy` vers la version 2.4.4
    - `django` vers la version 6.0.5
    - `botocore` vers la version 1.42.97
    - `redis` vers la version 7.4.0
    - `filelock` vers la version 3.29.0
    - et d'autres (voir commits pour détails).
- Suppression de l'utilisation de `ipdb` et ajout des dépendances manquantes [#2932](https://github.com/betagouv/complements-alimentaires/pull/2932).
- Refactorisation des tests unitaires pour une meilleure granularité.

### Autres changements
- Mise à jour de la documentation et des commentaires de code.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des actions GitHub pour la CI/CD.
- Amélioration de la gestion des polices d'affichage.
- Correction d'un problème de mélange de paramètres lors de l'activation du visa automatique.
