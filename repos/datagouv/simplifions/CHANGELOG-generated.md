## Changelog : simplifions (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la mise en place de l'environnement de production et la configuration initiale de l'application Simplifions.  L'application adopte désormais l'apparence visuelle de production, avec le favicon et la page d'accueil correspondants. Des améliorations ont également été apportées à la configuration et au processus d'intégration continue.

### Évolutions fonctionnelles
- L'application utilise désormais le favicon et le logo de production.
- La page d'accueil est maintenant configurée pour ressembler à la version de production ([https://simplifions.data.gouv.fr](https://simplifions.data.gouv.fr)).
- La page "à propos" est maintenant un miroir de la version de production.

### Évolutions techniques
- Suppression de `solid_queue` et `solid_cable` car ils ne sont pas utilisés dans l'application actuelle.
- Ajout des identifiants pour les différents environnements (production, staging, sandbox).
- Reconnaissance des environnements staging et sandbox dans les configurations Solid.
- Mise à jour des actions GitHub utilisées pour le CI/CD :
    - `actions/checkout` vers la version 7 [#1](https://github.com/datagouv/simplifions/pull/1)
    - `actions/upload-artifact` vers la version 7 [#1](https://github.com/datagouv/simplifions/pull/1)
    - `actions/cache` vers la version 6 [#3](https://github.com/datagouv/simplifions/pull/3)
- Mise à jour des dépendances :
    - `image_processing` vers la version 2.0.2 [#2](https://github.com/datagouv/simplifions/pull/2)
    - `solid_queue` vers la version 1.5.1 [#5](https://github.com/datagouv/simplifions/pull/5)
- Adoption des conventions RSpec et RuboCop du projet relais.
- Initialisation de l'application Rails Simplifions en mode standalone.
- Ajout d'un schéma vide pour permettre le bon fonctionnement de `db:test:prepare` dans le CI.
- Possibilité de déclencher le CI manuellement.
- Utilisation de DSFR 1.15.1 servi depuis les assets du projet.

### Autres changements
- Suppression de `image_processing` en attendant l'utilisation effective des variantes d'images.
