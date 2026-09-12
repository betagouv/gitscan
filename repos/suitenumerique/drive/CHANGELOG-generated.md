## Changelog : drive (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec la refonte complète du système de gestion des restrictions d'accès, permettant un contrôle beaucoup plus fin sur la visibilité et la protection des dossiers. La robustesse de la plateforme a également été renforcée par l'introduction de tests de charge (load testing), de nouvelles mesures de sécurité pour l'édition de documents (WOPI) et une optimisation des processus d'administration et de détection de malwares.

### Évolutions fonctionnelles
- **Gestion des restrictions et permissions** : 
    - Mise en place d'un système permettant d'activer ou désactiver des restrictions sur des dossiers (notamment via leur déplacement dans l'arborescence).
    - Les éléments faisant l'objet d'une restriction sont désormais exclus des résultats de recherche, des exports et de l'indexation.
    - Amélioration de la visibilité des états de restriction via l'API des éléments.
- **Administration** : Ajout de la possibilité d'abandonner manuellement des analyses de logiciels malveillants en cours.
- **Expérience utilisateur et corrections** :
    - Correction du rafraîchissement de la vue "Récents" après une modification d'élément.
    - Amélioration de l'affichage et du rendu des documents PDF.
    - Sécurisation de la suppression : un créateur ne peut plus supprimer un élément si ses droits d'accès ont été révoqués.

### Évolutions techniques
- **Refonte du moteur de permissions** : Migration de la logique de calcul des droits et de la résolution des rôles vers un composant backend dédié pour améliorer la modularité et la maintenance.
- **Tests et performance** :
    - Introduction de scénarios de tests de charge avec JMeter (sessions utilisateurs standards et scénarios de lecture intensive).
    - Amélioration de l'environnement de tests de bout en bout (E2E).
    - Intégration du monitoring de performance via Sentry.
- **Sécurité et protocoles** : Renforcement de la sécurité des requêtes WOPI par l'ajout de la validation des signatures et de la gestion des clés de preuve (proof keys).
- **Infrastructure et DevOps** :
    - Automatisation de la réconciliation des commandes de détection de malwares via Helm.
    - Optimisation des scripts de base de données (psql) et des règles de compilation (Makefile).
    - Nettoyage des variables d'environnement inutilisées.
- **Frontend** : Migration vers le nouveau package de composants d'interface `@gouvfr-lasuite/ui-components`.

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant les paramètres du backend de permissions et ajout du badge DPG dans le README.
- **Maintenance** : Nettoyage de fichiers de configuration et mise à jour du journal des modifications (changelog).
