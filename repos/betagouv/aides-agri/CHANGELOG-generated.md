## Changelog : aides-agri (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'administration du service, notamment l'export de données, la gestion des bases juridiques et l'ajout de la région Bourgogne-Franche-Comté. La documentation a également été mise à jour et complétée, notamment avec un dossier d'architecture technique. Des corrections de bugs et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité du service.

### Évolutions fonctionnelles
- Ajout de la région Bourgogne-Franche-Comté aux régions intégrées dans le service. [#632](https://github.com/betagouv/aides-agri/issues/632)
- Correction du lien vers le formulaire de collecte des aides. [#649](https://github.com/betagouv/aides-agri/issues/649)
- Correction du tracking des clics sur les liens externes dans les fiches d'aide. [#630](https://github.com/betagouv/aides-agri/issues/630)
- Amélioration de l'affichage des liens non cliquables dans la liste des résultats. [#629](https://github.com/betagouv/aides-agri/issues/629)
- Amélioration de l'administration des retours utilisateurs. [#646](https://github.com/betagouv/aides-agri/issues/646)
- Possibilité d'appliquer des filtres lors de l'export CSV des aides depuis l'administration. [#643](https://github.com/betagouv/aides-agri/issues/643)

### Évolutions techniques
- Migration vers Python 3.14. [#644](https://github.com/betagouv/aides-agri/issues/644)
- Amélioration de l'admin : les bases juridiques sont désormais réutilisables. [#616](https://github.com/betagouv/aides-agri/issues/616)
- Optimisation de l'empreinte mémoire de la page des résultats. [#652](https://github.com/betagouv/aides-agri/issues/652) et [#647](https://github.com/betagouv/aides-agri/issues/647)
- Mise à jour de la documentation d'infrastructure avec l'ajout des variables d'environnement. [#633](https://github.com/betagouv/aides-agri/issues/633)
- Publication d'un dossier d'architecture technique et des ADR (Architecture Decision Records) à jour. [#594](https://github.com/betagouv/aides-agri/issues/594)
- Diverses mises à jour de dépendances (voir section "Autres changements").

### Autres changements
- Mise à jour des statistiques pour juin 2026. [#648](https://github.com/betagouv/aides-agri/issues/648)
- Amélioration des exports CSV depuis l'administration. [#599](https://github.com/betagouv/aides-agri/issues/599)
- Correction d'une typo dans la documentation. [#606](https://github.com/betagouv/aides-agri/issues/606)
- Complétion de la documentation (plusieurs commits : [#605](https://github.com/betagouv/aides-agri/issues/605), [#604](https://github.com/betagouv/aides-agri/issues/604), [#603](https://github.com/betagouv/aides-agri/issues/603), [#602](https://github.com/betagouv/aides-agri/issues/602)).
- Mises à jour régulières des dépendances via Dependabot (ex: `@sentry/browser`, `pytest`, `ruff`, `django`, `faker`, `idna`, `coverage`, `sentry-sdk`, `docling`, `@gouvfr/dsfr-chart`).
