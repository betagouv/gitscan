## Changelog : aides-agri (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec la v2 du parcours agri, la consolidation des informations légales des aides et des corrections de bugs d'affichage et de fonctionnement. Des optimisations techniques ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- **Parcours agri v2 :** Déploiement de la version 2 du parcours agricole, améliorant l'expérience utilisateur pour les exploitants agricoles. [#418](https://github.com/betagouv/aides-agri/pull/418)
- **Gestion des fiches d'aide :**
    - Possibilité de créer une fiche mère à partir de plusieurs fiches filles. [#469](https://github.com/betagouv/aides-agri/pull/469)
    - Modification d'une fiche mère impacte également ses fiches filles. [#468](https://github.com/betagouv/aides-agri/pull/468)
- **Informations légales :** Déplacement des informations légales en bas de page des aides. [#466](https://github.com/betagouv/aides-agri/pull/466)
- **Base juridique des aides :** Consolidation et amélioration de la gestion de la base juridique des aides. [#495](https://github.com/betagouv/aides-agri/pull/495), [#499](https://github.com/betagouv/aides-agri/pull/499)
- **Outil d'édition des aides :** Améliorations apportées à l'outil d'édition des aides pour faciliter la gestion du contenu. [#498](https://github.com/betagouv/aides-agri/pull/498)
- **Correction d'impression PDF :** Correction d'un bug empêchant l'impression correcte des PDF. [#525](https://github.com/betagouv/aides-agri/pull/525)
- **Correction crash historique admin :** Correction d'un crash de l'historique dans l'interface d'administration. [#524](https://github.com/betagouv/aides-agri/pull/524)
- **Correction bug d'affichage couleur :** Correction d'un bug d'affichage des couleurs sur la page des résultats. [#511](https://github.com/betagouv/aides-agri/pull/511)
- **Correction alignement filtres :** Correction d'un problème d'alignement des filtres sur la page d'ensemble des aides. [#515](https://github.com/betagouv/aides-agri/pull/515)
- **Correction slug des aides :** Correction d'un bug lié au slug des aides. [#497](https://github.com/betagouv/aides-agri/pull/497)
- **Amélioration de la homepage :** Ajustements apportés à la page d'accueil. [#527](https://github.com/betagouv/aides-agri/pull/527)

### Évolutions techniques
- **Optimisation des performances :** Tentative de réduction des latences de l'application. [#523](https://github.com/betagouv/aides-agri/pull/523)
- **Workflow Github :** Optimisation du workflow Github pour une meilleure gestion des contributions. [#467](https://github.com/betagouv/aides-agri/pull/467)
- **Déploiement simplifié :** Facilitation du déploiement en cas de changement de schéma de base de données. [#501](https://github.com/betagouv/aides-agri/pull/501)
- **Mise à jour des dépendances :** Mises à jour de plusieurs dépendances (Django, Django-DSFR, Sentry, etc.) pour bénéficier des dernières corrections de sécurité et améliorations.
- **Gestion des dépendances UV :** Correction du système de cooldown des dépendances UV. [#470](https://github.com/betagouv/aides-agri/pull/470)
- **Verrouillage des dépendances UV :** Ajout de fichiers de verrouillage pour les dépendances UV. [#491](https://github.com/betagouv/aides-agri/pull/491), [#522](https://github.com/betagouv/aides-agri/pull/522)

### Autres changements
- **Documentation :** Mise à jour de la date de validité du fichier `security.txt`. [#505](https://github.com/betagouv/aides-agri/pull/505)
- **Scripts DDT(M) :** Ajout de scripts pour la création et l'association des logos des Directions Départementales des Territoires et de la Mer. [#493](https://github.com/betagouv/aides-agri/pull/493), [#507](https://github.com/betagouv/aides-agri/pull/507)
- **Statistiques :** Ajout des statistiques pour le mois de mars 2026. [#477](https://github.com/betagouv/aides-agri/pull/477)
