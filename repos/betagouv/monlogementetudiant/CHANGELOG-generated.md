## Changelog : monlogementetudiant (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience utilisateur grâce à une refonte de l'interface et l'ajout de nouveaux espaces (espace étudiant, mode gestionnaire). Parallèlement, des travaux importants ont été menés sur la fiabilité des données (géocodage et adresses) et sur l'automatisation de la maintenance des données (archivage et purges automatiques).

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Création d'un espace dédié pour les étudiants.
    - Mise en place d'un mode de contact pour les gestionnaires.
    - Ajout de la gestion des préférences de notifications sur la page des favoris.
    - Amélioration de l'administration avec l'affichage de la part d'étudiants boursiers.
- **Interface et Expérience Utilisateur (UI/UX)** :
    - Refonte visuelle utilisant les composants du Design System (DSFR) : passage aux boutons radio, menus latéraux, et utilisation d'alertes plutôt que de "toasters".
    - Amélioration de la navigation et de l'affichage (menus, icônes de simulation, grille d'images).
    - Optimisation des formulaires (pré-remplissage du numéro de téléphone, suppression de certains champs obligatoires).
- **Corrections** :
    - Correction de la mise à jour des informations utilisateurs [#372](https://github.com/betagouv/monlogementetudiant/pull/372).
    - Correction des typologies dans l'administration [#369](https://github.com/betagouv/monlogementetudiant/pull/369).
    - Correction de noms d'établissements (fac habitat).

### Évolutions techniques
- **Gestion et qualité des données** :
    - Fiabilisation du géocodage : amélioration de la validation des adresses (gestion des CEDEX, validation via le BAN) et nouveau système de rapport pour identifier les adresses incohérentes.
    - Automatisation du cycle de vie des données : mise en place de politiques de rétention (purges mensuelles, archivage automatique sur S3 des données supprimées) et de sauvegardes quotidiennes/mensuelles de la base de données.
- **Performance et Infrastructure** :
    - Optimisation des performances via la mise en cache des images.
    - Optimisation des ressources Scalingo en fusionnant certaines tâches de détection d'alertes pour respecter les limites de jobs.
    - Résolution de fuites de mémoire sur les processus de fermeture de base de données [#365](https://github.com/betagouv/monlogementetudiant/pull/365).
    - Optimisation des index de la base de données.

### Autres changements
- **Documentation** : Mise à jour de la politique de confidentialité, documentation de la commande de backfill de géocodage dans le README et ajout de notes sur les procédures de restauration d'archives S3.
- **Maintenance** : Nettoyage du code (linting, suppression de `console.log`) et mise à jour des tests.
