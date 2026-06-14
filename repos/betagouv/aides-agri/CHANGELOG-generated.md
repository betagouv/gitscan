## Changelog : aides-agri (30 derniers jours, au 13 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la documentation du projet, des corrections de bugs et des mises à jour de dépendances. Des améliorations ont été apportées à l'export CSV depuis l'interface d'administration et à la lisibilité de la page de statistiques. Des efforts ont également été faits pour améliorer les performances et la sécurité du service.

### Évolutions fonctionnelles
- Amélioration des exports CSV depuis l'administration, avec l'ajout d'un champ pour faciliter l'export des données. [#599](https://github.com/betagouv/aides-agri/issues/599)
- La page de statistiques est plus lisible. [#585](https://github.com/betagouv/aides-agri/issues/585)
- Correction d'un bug empêchant l'affichage du commentaire du champ "base juridique" sur la fiche d'aide. [#569](https://github.com/betagouv/aides-agri/issues/569)
- Correction de deux erreurs concernant les notifications admin des aides. [#576](https://github.com/betagouv/aides-agri/issues/576)
- Ajout de l'Occitanie à la liste statique des régions couvertes. [#561](https://github.com/betagouv/aides-agri/issues/561)
- Ajout d'un nouvel icône pour le thème Transmission. [#573](https://github.com/betagouv/aides-agri/issues/573)

### Évolutions techniques
- Mise à jour de la documentation technique, incluant le dossier d'architecture et les ADR (Architecture Decision Records). [#594](https://github.com/betagouv/aides-agri/issues/594)
- Tentative d'amélioration des performances en dynamisant le paramètre `max-requests` de Gunicorn. [#578](https://github.com/betagouv/aides-agri/issues/578)
- Mises à jour de plusieurs dépendances : Django, Ruff, idna, faker, psycopg, coverage, sentry-sdk, requests, django-reversion, pymdown-extensions, certifi, types-pyyaml, django-formtools, django-admin-extra-buttons. (Voir les PRs correspondants pour plus de détails)
- Utilisation de `uv lock` pour verrouiller les dépendances. [#598](https://github.com/betagouv/aides-agri/issues/598), [#588](https://github.com/betagouv/aides-agri/issues/588), [#583](https://github.com/betagouv/aides-agri/issues/583), [#562](https://github.com/betagouv/aides-agri/issues/562)

### Autres changements
- Correction d'une typo dans la documentation. [#606](https://github.com/betagouv/aides-agri/issues/606)
- Finalisation de la documentation (version 1). [#605](https://github.com/betagouv/aides-agri/issues/605)
- Ajout de documentation sur les sujets de sécurité du service. [#604](https://github.com/betagouv/aides-agri/issues/604)
- Correction de quelques fautes mineures dans la documentation. [#603](https://github.com/betagouv/aides-agri/issues/603)
- Suite et fin de la remise à niveau de la documentation. [#602](https://github.com/betagouv/aides-agri/issues/602)
- Correction d'un problème avec `aides_publish_illustrations_from_db`. [#600](https://github.com/betagouv/aides-agri/issues/600)
