## Changelog : seves (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions de Sèves se concentrent sur l'amélioration de l'interface utilisateur, la correction de bugs et l'optimisation des performances, notamment au niveau de la gestion des événements SV et des formulaires. Des améliorations ont également été apportées à la gestion des documents et des fichiers, ainsi qu'à la sécurité et à la robustesse de l'application.

### Évolutions fonctionnelles
- Possibilité de prévisualiser les images et les fichiers PDF. [#3bdeb05](https://github.com/betagouv/seves/commit/3bdeb05)
- Amélioration de la précision des notifications dans les Autorisations Spécifiques (SSA). [#107ac35](https://github.com/betagouv/seves/commit/107ac35)
- Ajout du numéro RASFF aux objets TIAC. [#b6469bf](https://github.com/betagouv/seves/commit/b6469bf)
- Ajout de la date de publication sur tous les objets fiche. [#51fa26d](https://github.com/betagouv/seves/commit/51fa26d)
- Date de réception maximale ajoutée dans l'interface front-end. [#16c371b](https://github.com/betagouv/seves/commit/16c371b)
- Amélioration de l'affichage de la date dans les messages. [#034ca53](https://github.com/betagouv/seves/commit/034ca53)
- Ajout d'un bouton d'annulation sur la page d'édition TIAC. [#e0be778](https://github.com/betagouv/seves/commit/e0be778)
- Affichage de la date de fin de suivi dans les exports CSV lorsque nécessaire. [#ac51a38](https://github.com/betagouv/seves/commit/ac51a38)
- La date de prélèvement est maintenant obligatoire sur le formulaire de prélèvement SV. [#e5aff4e](https://github.com/betagouv/seves/commit/e5aff4e)
- Amélioration de l'éditeur de texte enrichi pour les messages. [#359f076](https://github.com/betagouv/seves/commit/359f076) et [#6debe44](https://github.com/betagouv/seves/commit/6debe44)

### Évolutions techniques
- Mise à jour de Django vers la version 6. [#e760f3f](https://github.com/betagouv/seves/commit/e760f3f)
- Amélioration de la fiabilité de `choice_js_fill`. [#a766d63](https://github.com/betagouv/seves/commit/a766d63)
- Correction d'un test assert flaky. [#1ff40d2](https://github.com/betagouv/seves/commit/1ff40d2)
- Ajout d'un timeout sur les requêtes OIDC pour éviter les interruptions des workers en production. [#0d85baf](https://github.com/betagouv/seves/commit/0d85baf)
- Amélioration des performances de la vue de liste SSA. [#8e5af29](https://github.com/betagouv/seves/commit/8e5af29)
- Refactorisation de l'implémentation de `and_more_ellipsis_tooltip`. [#b3d398d](https://github.com/betagouv/seves/commit/b3d398d)
- Amélioration de la gestion des relations profondes dans l'historique des modèles. [#4270c9a](https://github.com/betagouv/seves/commit/4270c9a)
- S'assurer que Celery se reconnecte à Redis. [#9dab5ba](https://github.com/betagouv/seves/commit/9dab5ba)
- Suppression de l'utilisation de SSA dans l'application core. [#d5e7d58](https://github.com/betagouv/seves/commit/d5e7d58)
- Suppression des révisions ajoutées par les signaux dans SV. [#c3a59b4](https://github.com/betagouv/seves/commit/c3a59b4)

### Autres changements
- Corrections de design sur le tableau SV et le menu des domaines. [#e9b2045](https://github.com/betagouv/seves/commit/e9b2045) et [#8bda377](https://github.com/betagouv/seves/commit/8bda377)
- Amélioration de l'accessibilité de l'indicateur 'fiche zone délimitée'. [#bb0c0ad](https://github.com/betagouv/seves/commit/bb0c0ad)
- Uniformisation des liens d'annulation sur les objets fiche. [#98d3a21](https://github.com/betagouv/seves/commit/98d3a21)
- Changement de format pour les filtres année et numéro. [#f3fc1b2](https://github.com/betagouv/seves/commit/f3fc1b2)
- Suppression de l'utilisation de Clamav au profit d'une solution en ligne. [#65c5b00](https://github.com/betagouv/seves/commit/65c5b00)
- Mise à jour des dépendances : lxml, django-dsfr, django-post-office, sentry-sdk, ruff, pytest, cryptography, djhtml, redis, gunicorn, pygments, requests.
