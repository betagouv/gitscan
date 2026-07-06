## Changelog : aides-agri (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se sont concentrées sur l'administration du service, avec des optimisations pour l'export de données, la gestion des bases juridiques et l'ajout de la région Bourgogne-Franche-Comté. La documentation a également été largement revue et mise à jour. Des corrections de bugs et des améliorations de la performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la région Bourgogne-Franche-Comté aux régions intégrées, permettant une meilleure prise en charge des aides dans cette zone géographique. [#632](https://github.com/betagouv/aides-agri/issues/632)
- Amélioration de l'admin : les bases juridiques sont désormais réutilisables, facilitant la gestion et la cohérence des informations. [#616](https://github.com/betagouv/aides-agri/issues/616)
- Amélioration de l'admin : ajout d'un champ pour l'export CSV, offrant plus de flexibilité dans la gestion des données. [#607](https://github.com/betagouv/aides-agri/issues/607)
- Correction du lien vers le formulaire de collecte des aides, améliorant l'expérience utilisateur. [#649](https://github.com/betagouv/aides-agri/issues/649)
- Correction du tracking sur les liens externes, assurant un suivi précis des actions des utilisateurs. [#630](https://github.com/betagouv/aides-agri/issues/630)
- Les liens non-cliquables ne sont plus affichés dans la liste des résultats, améliorant la clarté de l'interface. [#629](https://github.com/betagouv/aides-agri/issues/629)
- Comptabilisation des clics vers l’extérieur via les étapes dans la fiche d’aide, pour un suivi plus précis de l'engagement des utilisateurs. [#621](https://github.com/betagouv/aides-agri/issues/621)

### Évolutions techniques
- Migration vers Python 3.14, assurant la compatibilité avec les dernières technologies et améliorant la sécurité. [#644](https://github.com/betagouv/aides-agri/issues/644)
- Tentative de diminution de l'empreinte mémoire de la page Résultats, améliorant la performance et la réactivité de l'application. [#652](https://github.com/betagouv/aides-agri/issues/652) et [#647](https://github.com/betagouv/aides-agri/issues/647)
- Mise à jour des statistiques pour juin 2026, assurant un suivi précis de l'utilisation du service. [#648](https://github.com/betagouv/aides-agri/issues/648)
- Améliorations de l'admin des retours utilisateurices, facilitant la gestion des feedbacks. [#646](https://github.com/betagouv/aides-agri/issues/646)
- Application des filtres à l'export CSV des aides dans l'admin, offrant plus de contrôle sur les données exportées. [#643](https://github.com/betagouv/aides-agri/issues/643)
- Rétablissement de la taille des champs dans l'admin, améliorant l'ergonomie de l'interface. [#645](https://github.com/betagouv/aides-agri/issues/645)

### Autres changements
- Documentation : revue complète et mise à jour de la documentation, incluant les sujets de sécurité et une remise à niveau générale. [#606](https://github.com/betagouv/aides-agri/issues/606), [#605](https://github.com/betagouv/aides-agri/issues/605), [#604](https://github.com/betagouv/aides-agri/issues/604), [#603](https://github.com/betagouv/aides-agri/issues/603), [#602](https://github.com/betagouv/aides-agri/issues/602)
- Correction d'un bug dans `aides_publish_illustrations_from_db`. [#600](https://github.com/betagouv/aides-agri/issues/600)
- Mise à jour des dépendances (certifi, coverage, faker, idna, pydantic-settings, pytest, ruff, sentry-sdk, ultimate-sitemap-parser, django, django-debug-toolbar, django-reversion).
