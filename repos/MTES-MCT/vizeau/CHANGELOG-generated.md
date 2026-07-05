## Changelog : vizeau (30 derniers jours, au 02 Juillet 2026)

### Résumé
Ce mois-ci, l'application Vizeau a bénéficié d'améliorations significatives concernant la gestion des projets, notamment l'ajout de nouvelles étapes, la gestion des documents associés et une interface utilisateur améliorée. Des optimisations techniques ont également été apportées pour améliorer la performance et la maintenabilité du code. L'intégration de Matomo permet désormais un suivi plus précis de l'utilisation de l'application.

### Évolutions fonctionnelles
- **Gestion des projets :**
    - Ajout de la création et de l'édition d'étapes de projet [#457](https://github.com/MTES-MCT/vizeau/pull/457), [#451](https://github.com/MTES-MCT/vizeau/pull/451), [#447](https://github.com/MTES-MCT/vizeau/pull/447).
    - Possibilité d'associer des documents à chaque étape de projet [#456](https://github.com/MTES-MCT/vizeau/pull/456), [#440](https://github.com/MTES-MCT/vizeau/pull/440).
    - Refonte du formulaire de création de projet avec des composants dédiés [#436](https://github.com/MTES-MCT/vizeau/pull/436).
    - Ajout d'une page "Mes territoires" pour faciliter la gestion des territoires [#445](https://github.com/MTES-MCT/vizeau/pull/445).
    - Ajout d'un bouton de navigation vers la sélection de parcelles [#450](https://github.com/MTES-MCT/vizeau/pull/450).
- **Améliorations générales :**
    - Intégration de Matomo pour le suivi analytique [#459](https://github.com/MTES-MCT/vizeau/pull/459).
    - Correction du tri des données [#453](https://github.com/MTES-MCT/vizeau/pull/453).
    - Amélioration de la gestion des liens profonds vers les parcelles.
    - Correction de l'affichage des titres tronqués [#455](https://github.com/MTES-MCT/vizeau/pull/455).
- **Exploitations agricoles :**
    - Possibilité d'assigner un territoire à une exploitation [#440](https://github.com/MTES-MCT/vizeau/pull/440).

### Évolutions techniques
- **Performance :**
    - Optimisation de la requête de récupération des AAC et utilisation d'un mode debug pour DuckDB [#460](https://github.com/MTES-MCT/vizeau/pull/460).
    - Optimisation de la mémoire en effectuant le tri des données sur disque [#458](https://github.com/MTES-MCT/vizeau/pull/458).
- **Infrastructure & Code :**
    - Raccourcissement des imports relatifs des types [#442](https://github.com/MTES-MCT/vizeau/pull/442).
    - Refactorisation des filtres [#435](https://github.com/MTES-MCT/vizeau/pull/435).
    - Mise à jour de la documentation de migration en production [#433](https://github.com/MTES-MCT/vizeau/pull/433).
    - Ajout d'un fichier `.env.sample` et mise à jour du `.gitignore` [#461](https://github.com/MTES-MCT/vizeau/pull/461).
- **Tests :**
    - Mise à jour des tests et corrections diverses.

### Autres changements
- Génération de scripts pour les fiches AAC et les analyses d'eau [#460](https://github.com/MTES-MCT/vizeau/pull/460), [#458](https://github.com/MTES-MCT/vizeau/pull/458).
- Ajout de la documentation pour la commande de réinitialisation du mot de passe [#434](https://github.com/MTES-MCT/vizeau/pull/434).
- Corrections de typos et amélioration de la documentation générale.
- Correction de bugs et améliorations diverses suite aux retours de Copilot.
