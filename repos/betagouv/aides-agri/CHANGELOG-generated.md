## Changelog : aides-agri (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la documentation, la correction de bugs et l'optimisation de l'administration du site. De nouvelles régions ont été intégrées et des améliorations ont été apportées aux exports CSV et au suivi des liens externes. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de la région Bourgogne-Franche-Comté aux régions intégrées. [#632](https://github.com/betagouv/aides-agri/issues/632)
- Amélioration de la lisibilité de la page de statistiques. [#585](https://github.com/betagouv/aides-agri/issues/585)
- Correction du suivi des clics sur les liens externes, permettant de mieux comptabiliser les actions des utilisateurs. [#630](https://github.com/betagouv/aides-agri/issues/630)
- Amélioration de l'interface d'administration pour les exports CSV, avec l'ajout d'un champ supplémentaire. [#607](https://github.com/betagouv/aides-agri/issues/607) et [#599](https://github.com/betagouv/aides-agri/issues/599)
- Les bases juridiques sont désormais réutilisables dans l'interface d'administration, facilitant la gestion des aides. [#616](https://github.com/betagouv/aides-agri/issues/616)
- Correction d'erreurs sur les notifications d'administration des aides. [#576](https://github.com/betagouv/aides-agri/issues/576)
- Affichage amélioré des liens non cliquables dans la liste des résultats. [#629](https://github.com/betagouv/aides-agri/issues/629)

### Évolutions techniques
- Mise à jour de plusieurs dépendances (Django, pytest, faker, ruff, idna, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance. (Voir les PRs [#625](https://github.com/betagouv/aides-agri/pull/625), [#624](https://github.com/betagouv/aides-agri/pull/624), [#622](https://github.com/betagouv/aides-agri/pull/622), [#623](https://github.com/betagouv/aides-agri/pull/623), [#595](https://github.com/betagouv/aides-agri/pull/595), [#587](https://github.com/betagouv/aides-agri/pull/587), [#586](https://github.com/betagouv/aides-agri/pull/586), etc.)
- Documentation de l'infrastructure : ajout des variables d'environnement. [#633](https://github.com/betagouv/aides-agri/issues/633)
- Mise à jour de la documentation technique et des ADR (Architecture Decision Records). [#594](https://github.com/betagouv/aides-agri/issues/594)
- Tentative d'amélioration des performances en dynamisant le nombre maximal de requêtes gérées par Gunicorn. [#578](https://github.com/betagouv/aides-agri/issues/578)

### Autres changements
- Correction d'une faute de frappe dans la documentation. [#606](https://github.com/betagouv/aides-agri/issues/606)
- Finalisation de la documentation (version 1). [#605](https://github.com/betagouv/aides-agri/issues/605)
- Documentation sur les sujets de sécurité du service. [#604](https://github.com/betagouv/aides-agri/issues/604)
- Correction de quelques erreurs mineures dans la documentation. [#603](https://github.com/betagouv/aides-agri/issues/603)
- Suite et fin de la mise à niveau de la documentation. [#602](https://github.com/betagouv/aides-agri/issues/602)
- Correction d'un problème avec `aides_publish_illustrations_from_db`. [#600](https://github.com/betagouv/aides-agri/issues/600)
