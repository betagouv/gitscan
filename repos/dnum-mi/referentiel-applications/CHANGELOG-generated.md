## Changelog : referentiel-applications (30 derniers jours, au 13/10/2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes en enrichissant ses fonctionnalités métier (export PowerPoint, synchronisation Grist, nouveau panneau d'administration) tout en renforçant considérablement la sécurité des accès et la robustesse de l'infrastructure technique.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Exportation des fiches produits vers PowerPoint [#2833](https://github.com/dnum-mi/referentiel-applications/issues/2833).
    - Synchronisation avec Grist [#2876](https://github.com/dnum-mi/referentiel-applications/issues/2876).
    - Nouveau panneau d'administration pour la gestion des options d'hébergement [#2763](https://github.com/dnum-mi/referentiel-applications/issues/2763).
    - Gestion des applications remplacées via de nouveaux tags [#2771](https://github.com/dnum-mi/referentiel-applications/issues/2771) et [#2665](https://github.com/dnum-mi/referentiel-applications/issues/2665).
- **Améliorations de l'expérience utilisateur** :
    - Optimisation de la recherche : indexation des stacks technologiques [#2770](https://github.com/dnum-mi/referentiel-applications/issues/2770), recherche de technologies sans fin de vie [#2660](https://github.com/dnum-mi/referentiel-applications/issues/2660), et rétablissement des suggestions MAIA [#2774](https://github.com/dnum-mi/referentiel-applications/issues/2774).
    - Améliorations de l'interface : pagination Excel [#2829](https://github.com/dnum-mi/referentiel-applications/issues/2829), gestion des notifications [#2772](https://github.com/dnum-mi/referentiel-applications/issues/2772), et affichage du référent administrateur sur la page profil [#2690](https://github.com/dnum-mi/referentiel-applications/issues/2690).
    - Alertes de droits d'accès pour les utilisateurs n'ayant pas les droits de lecture complets [#2633](https://github.com/dnum-mi/referentiel-applications/issues/2633).
- **Gestion des droits et accès** :
    - Restriction de l'accès aux technologies par capacité et périmètre [#2803](https://github.com/dnum-mi/referentiel-applications/issues/2803).
    - Corrections sur la gestion des permissions et des périmètres d'administration (scoped admin) [#2865](https://github.com/dnum-mi/referentiel-applications/issues/2865), [#2827](https://github.com/dnum-mi/referentiel-applications/issues/2827), et [#2737](https://github.com/dnum-mi/referentiel-applications/issues/2737).

### Évolutions techniques
- **Sécurité** :
    - Renforcement de l'authentification et durcissement des accès à l'application [#2802](https://github.com/dnum-mi/referentiel-applications/issues/2802), [#2630](https://github.com/dnum-mi/referentiel-applications/issues/2630).
    - Correction de vulnérabilités et mise à jour des dépendances de développement [#2862](https://github.com/dnum-mi/referentiel-applications/issues/2862), [#2898](https://github.com/dnum-mi/referentiel-applications/issues/2898).
    - Prévention de l'escalade de privilèges via les jetons de service délégués [#2687](https://github.com/dnum-mi/referentiel-applications/issues/2687).
- **Architecture et API** :
    - Mise en place d'un filtre d'exception global et d'un contrat d'erreur normalisé pour l'API [#2738](https://github.com/dnum-mi/referentiel-applications/issues/2738).
    - Refactorisation du frontend (découpage des formulaires d'application [#2766](https://github.com/dnum-mi/referentiel-applications/issues/2766)) et du backend (nettoyage des dépendances et typage des services [#2762](https://github.com/dnum-mi/referentiel-applications/issues/2762)).
    - Unification des modales de recherche asynchrone et de relation [#2664](https://github.com/dnum-mi/referentiel-applications/issues/2664).
- **Qualité et CI/CD** :
    - Amélioration des portes de qualité (quality gates) et de la couverture de tests frontend [#2667](https://github.com/dnum-mi/referentiel-applications/issues/2667).
    - Amélioration de la fiabilité des tests QA via l'utilisation de fixtures reproductibles [#2773](https://github.com/dnum-mi/referentiel-applications/issues/2773), [#2661](https://github.com/dnum-mi/referentiel-applications/issues/2661).

### Autres changements
- Mise à jour de la documentation utilisateur [#2764](https://github.com/dnum-mi/referentiel-applications/issues/2764) et clarification des processus d'authentification [#2659](https://github.com/dnum-mi/referentiel-applications/issues/2659).
