## Changelog : aides-agri (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'administration du service, notamment avec la réutilisation des bases juridiques et l'amélioration des exports CSV. La documentation a également été largement revue et mise à jour, incluant un dossier d'architecture technique. Des corrections de bugs et des optimisations de performance ont été apportées pour améliorer la stabilité et la réactivité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de l'admin : les bases juridiques sont désormais réutilisables, facilitant la gestion des aides. [#616](https://github.com/betagouv/aides-agri/issues/616)
- Amélioration des exports CSV depuis l'admin, avec l'ajout d'un champ. [#599](https://github.com/betagouv/aides-agri/issues/599) et [#607](https://github.com/betagouv/aides-agri/issues/607)
- Comptabilisation des clics vers l’extérieur via les étapes dans la fiche d’aide, permettant un meilleur suivi de l'engagement des utilisateurs. [#621](https://github.com/betagouv/aides-agri/issues/621)
- Correction de bugs sur les notifications admin des aides. [#576](https://github.com/betagouv/aides-agri/issues/576)
- La page de statistiques est plus lisible. [#585](https://github.com/betagouv/aides-agri/issues/585)

### Évolutions techniques
- Mise à jour de la documentation, incluant un dossier d'architecture technique et des ADR (Architecture Decision Records). [#594](https://github.com/betagouv/aides-agri/issues/594), [#605](https://github.com/betagouv/aides-agri/issues/605), [#604](https://github.com/betagouv/aides-agri/issues/604), [#603](https://github.com/betagouv/aides-agri/issues/603), [#602](https://github.com/betagouv/aides-agri/issues/602)
- Tentative de résolution des latences en dynamisant le `max-requests` de Gunicorn. [#578](https://github.com/betagouv/aides-agri/issues/578)
- Mises à jour de plusieurs dépendances : Django, Faker, Ruff, idna, sentry-sdk, certifi, types-pyyaml, django-formtools, requests, etc. (voir les commits pour plus de détails).
- Mise à jour de la librairie de chart DSFR. [#589](https://github.com/betagouv/aides-agri/issues/589)

### Autres changements
- Correction d'une typo dans la documentation. [#606](https://github.com/betagouv/aides-agri/issues/606)
- Exécution régulière de `uv lock` pour garantir la cohérence des dépendances. [#598](https://github.com/betagouv/aides-agri/issues/598), [#588](https://github.com/betagouv/aides-agri/issues/588), [#583](https://github.com/betagouv/aides-agri/issues/583), [#577](https://github.com/betagouv/aides-agri/issues/577)
- Correction d'un problème avec `aides_publish_illustrations_from_db`. [#600](https://github.com/betagouv/aides-agri/issues/600)
