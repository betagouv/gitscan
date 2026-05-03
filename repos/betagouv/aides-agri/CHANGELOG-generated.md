## Changelog : aides-agri (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la refonte du parcours utilisateur pour les aides agricoles (v2), l'amélioration de l'outil d'administration des aides, et la consolidation de la gestion des bases juridiques. De nombreuses mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- **Parcours utilisateur v2 :** Déploiement de la nouvelle version du parcours agri, améliorant l'expérience pour les exploitants agricoles. [#418](https://github.com/betagouv/aides-agri/pull/418)
- **Outil d'édition des aides :** Améliorations apportées à l'outil d'édition des aides pour faciliter la gestion des informations. [#498](https://github.com/betagouv/aides-agri/pull/498)
- **Gestion des bases juridiques :** Consolidation de la notion de base juridique des aides, avec des améliorations continues. [#495](https://github.com/betagouv/aides-agri/pull/495), [#499](https://github.com/betagouv/aides-agri/pull/499)
- **Fiches d'aide :** Possibilité de créer une fiche mère à partir de plusieurs fiches filles, et de modifier une fiche mère pour impacter ses fiches filles. [#468](https://github.com/betagouv/aides-agri/pull/468), [#469](https://github.com/betagouv/aides-agri/pull/469)
- **Affichage des aides :** Correction d'un bug d'affichage de couleur sur la page de résultats et amélioration de l'alignement des filtres sur la page d'ensemble des aides. [#511](https://github.com/betagouv/aides-agri/pull/511), [#515](https://github.com/betagouv/aides-agri/pull/515)
- **Informations légales :** Déplacement de l'information légale en bas de la page Aide. [#466](https://github.com/betagouv/aides-agri/pull/466)

### Évolutions techniques
- **Déploiement :** Facilitation du déploiement en cas de changement de schéma de BDD. [#501](https://github.com/betagouv/aides-agri/pull/501)
- **Workflow Github :** Optimisation du workflow Github pour une meilleure efficacité. [#467](https://github.com/betagouv/aides-agri/pull/467)
- **Mises à jour de dépendances :** Mises à jour de nombreuses dépendances (Django, Sentry, Ruff, etc.) pour améliorer la sécurité et la stabilité. (Voir commits individuels pour détails)
- **Lock des dépendances :** Ajout de fichiers de lock pour les dépendances (uv.lock) afin d'assurer la reproductibilité des environnements. [#491](https://github.com/betagouv/aides-agri/pull/491), [#512](https://github.com/betagouv/aides-agri/pull/512)

### Autres changements
- **Documentation :** Mise à jour de la date de validité du fichier security.txt. [#505](https://github.com/betagouv/aides-agri/pull/505)
- **Statistiques :** Ajout des statistiques pour le mois de mars 2026. [#477](https://github.com/betagouv/aides-agri/pull/477)
- **Scripts :** Ajout de scripts pour la gestion des services déconcentrés et des logos des DDT(M). [#493](https://github.com/betagouv/aides-agri/pull/493), [#507](https://github.com/betagouv/aides-agri/pull/507)
- **Correction du slug :** Correction d'un bug sur le slug des aides. [#497](https://github.com/betagouv/aides-agri/pull/497)
- **Cooldow des dépendances UV :** Correction du système de cooldown des dépendances UV. [#470](https://github.com/betagouv/aides-agri/pull/470)
