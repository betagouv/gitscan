## Changelog : aides-agri (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans l'interface d'administration, notamment avec l'ajout de fonctionnalités d'export CSV et la réutilisation des bases juridiques. La documentation a également été largement revue et mise à jour. Des corrections de bugs ont été apportées pour améliorer le suivi des liens externes et l'affichage des résultats de recherche. Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Ajout de la région Bourgogne-Franche-Comté aux régions intégrées dans le système. [#632](https://github.com/betagouv/aides-agri/issues/632)
- Amélioration de l'admin : les bases juridiques sont désormais réutilisables, facilitant la gestion des aides. [#616](https://github.com/betagouv/aides-agri/issues/616)
- Ajout d'un champ pour l'export CSV dans l'admin, améliorant la capacité à extraire des données. [#607](https://github.com/betagouv/aides-agri/issues/607)
- Amélioration des exports CSV depuis l'admin. [#599](https://github.com/betagouv/aides-agri/issues/599)
- Correction du tracking des clics sur les liens externes, permettant un suivi plus précis de l'activité des utilisateurs. [#630](https://github.com/betagouv/aides-agri/issues/630)
- Correction de l'affichage des liens non-cliquables dans la liste des résultats de recherche. [#629](https://github.com/betagouv/aides-agri/issues/629)
- Amélioration de la lisibilité de la page de statistiques. [#585](https://github.com/betagouv/aides-agri/issues/585)

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Django, pytest, ruff, sentry-sdk, faker, idna, certifi, etc. (voir les commits individuels pour les détails).
- Documentation d'infrastructure : ajout des variables d'environnement pour faciliter le déploiement et la configuration. [#633](https://github.com/betagouv/aides-agri/issues/633)
- Documentation : revue complète et mise à jour de la documentation, incluant l'architecture technique et les sujets de sécurité. [#605](https://github.com/betagouv/aides-agri/issues/605), [#604](https://github.com/betagouv/aides-agri/issues/604), [#603](https://github.com/betagouv/aides-agri/issues/603), [#602](https://github.com/betagouv/aides-agri/issues/602)
- Mise à jour des dépendances via `uv lock` pour assurer la reproductibilité des environnements. [#636](https://github.com/betagouv/aides-agri/issues/636), [#628](https://github.com/betagouv/aides-agri/issues/628), [#598](https://github.com/betagouv/aides-agri/issues/598), [#583](https://github.com/betagouv/aides-agri/issues/583), [#588](https://github.com/betagouv/aides-agri/issues/588)

### Autres changements
- Correction d'un bug dans `aides_publish_illustrations_from_db`. [#600](https://github.com/betagouv/aides-agri/issues/600)
- Correction d'une typo dans la documentation. [#606](https://github.com/betagouv/aides-agri/issues/606)
