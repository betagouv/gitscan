## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 01/09/2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une modernisation structurelle majeure, marquée par la migration vers Rails 8.1 et une refonte profonde de la gestion des types de champs. Ces évolutions techniques renforcent la stabilité et les performances du système. Pour les utilisateurs, les changements se traduisent par une interface d'administration plus ergonomique, une meilleure précision des rapports de révision et une gestion plus fiable des données lors de la fusion de comptes.

### Évolutions fonctionnelles
- **Administration et Édition** : 
    - Amélioration de l'interface d'édition avec l'ajout d'un bouton "paragraphe" dans les éditeurs d'attestations et d'emails.
    - Optimisation de la visibilité des tableaux de procédures pour éviter les problèmes d'affichage avec les libellés longs [#13769](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13769).
    - Harmonisation des infobulles dans l'éditeur d'attestation.
- **Gestion des dossiers et formulaires** :
    - Amélioration de la clarté et de la précision des rapports de révision (wording et détails des changements effectués).
    - Corrections sur le comportement des champs complexes (champs de type "répétition", listes déroulantes et pré-remplissage).
    - Amélioration de la gestion des PDF de dossiers vides via un système de mise en cache.
- **Cartographie** : Corrections sur l'affichage et l'exclusion mutuelle des couches de données (cadastre et RPG).
- **API et Intégrations** : 
    - Nouvelles capacités d'affectation de dossiers et exposition de l'historique des affectations via l'API v2.
- **Fusion de comptes** : Amélioration de la continuité de service lors de la fusion de comptes, garantissant le transfert des notifications, des rendez-vous, des suivis et des paramètres de procédure.

### Évolutions techniques
- **Architecture et Framework** :
    - Migration majeure de l'application vers **Rails 8.1** [#13612](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13612).
    - Refonte complète de la gestion des types de champs via l'implémentation du polymorphisme (STI - Single Table Inheritance) pour une architecture plus robuste [#13662](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13662).
    - Migration massive des templates de la technologie HAML vers ERB pour une meilleure maintenance.
- **Performance et GraphQL** :
    - Optimisations des requêtes GraphQL pour réduire les problèmes de performance (N+1) sur les adresses et les zones géographiques.
    - Segmentation du trafic GraphQL pour une meilleure observabilité et monitoring.
    - Exposition publique de nouveaux descripteurs de démarches et du nombre de dossiers.
- **Sécurité et Robustesse** :
    - Renforcement de la sécurité lors de l'exportation de fichiers ZIP (protection contre les traversées de chemin/path traversal) [#13674](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13674).
    - Durcissement du traitement des images (libvips) et des décodeurs.
    - Amélioration du filtrage des erreurs Sentry (notamment pour les scripts injectés par des navigateurs mobiles).
- **Maintenance et Nettoyage** :
    - Suppression de la dépendance à `delayed_job` [#13682](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13682).
    - Nettoyage important du code : suppression de nombreuses fonctions obsolètes, de colonnes de base de données inutilisées et de flags de fonctionnalités (feature flags) périmés.
    - Refonte du système de modèles d'emails vers une structure basée sur une table dédiée.

### Autres changements
- **Internationalisation (i18n)** : Travail important d'extraction des chaînes de caractères codées en dur vers les fichiers de traduction pour faciliter la maintenance et la localisation.
- **Documentation** : Mise à jour de la documentation concernant les dépendances système requises (libvips, zip).
