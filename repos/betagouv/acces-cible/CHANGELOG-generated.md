## Changelog : acces-cible (30 derniers jours, au 28 octobre 2026)

### Résumé
Cette période est marquée par une amélioration significative de la précision des audits, notamment grâce à une meilleure détection des mentions d'accessibilité et une analyse plus fine des dates de conformité. L'expérience utilisateur est également enrichie par de nouveaux filtres de recherche, une meilleure visibilité sur la fraîcheur des données et une structure d'export CSV optimisée.

### Évolutions fonctionnelles
- **Précision des audits et détection :**
    - Amélioration de la détection des mentions d'accessibilité grâce à des règles de recherche plus flexibles ([#790](https://github.com/betagouv/acces-cible/issues/790), [#774](https://github.com/betagouv/acces-cible/issues/774)).
    - Optimisation de l'analyse des dates pour les plans et les schémas ([#759](https://github.com/betagouv/acces-cible/issues/759), [#800](https://github.com/betagouv/acces-cible/issues/800)).
    - Amélioration de l'extraction de contenu (Shadow DOM) et de la détection du taux de conformité ([#785](https://github.com/betagouv/acces-cible/issues/785), [#789](https://github.com/betagouv/acces-cible/issues/789)).
    - Normalisation des URLs incluant désormais le préfixe "www" ([#795](https://github.com/betagouv/acces-cible/issues/795)).
    - Ajout d'un avertissement en cas d'URLs en double ignorées ([#801](https://github.com/betagouv/acces-cible/issues/801)).
- **Interface et expérience utilisateur :**
    - Ajout d'un filtre pour afficher le "dernier audit par site" ([#777](https://github.com/betagouv/acces-cible/issues/777)).
    - Affichage de la date de mise à jour des audits dans les vues dédiées ([#799](https://github.com/betagouv/acces-cible/issues/799)).
    - Refonte de la structure des exports CSV ([#796](https://github.com/betagouv/acces-cible/issues/796)).
    - Modification du design des alertes de redirection ([#762](https://github.com/betagouv/acces-cible/issues/762)).

### Évolutions techniques
- **Infrastructure et environnement :**
    - Mise à jour de la version de Ruby vers 4.0.7 ([#791](https://github.com/betagouv/acces-cible/issues/791)).
    - Renforcement de la sécurité de l'environnement de staging (gestion des identifiants ProConnect et blocage de l'indexation par les moteurs de recherche) ([#771](https://github.com/betagouv/acces-cible/issues/771), [#763](https://github.com/betagouv/acces-cible/issues/763)).
- **Optimisations :**
    - Résolution de problèmes de chargement pour les applications monopages (SPA) liés au CSS et à l'API Google ([#794](https://github.com/betagouv/acces-cible/issues/794)).

### Autres changements
- Mise à jour des traductions ([#769](https://github.com/betagouv/acces-cible/issues/769)).
