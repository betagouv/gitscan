## Changelog : referentiel-applications (30 derniers jours, au 15 octobre 2026)

### Résumé
Cette période a été marquée par un renforcement significatif de la sécurité et de l'accessibilité numérique (RGAA). Le projet a également gagné en puissance pour le pilotage grâce à de nouvelles capacités d'exportation de données (PowerPoint, stacks technologiques) et une meilleure synchronisation avec des outils externes comme Grist.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités**
    - Exportation des fiches produits vers PowerPoint ([#2833](https://github.com/dnum-mi/referentiel-applications/issues/2833)).
    - Exportation des stacks technologiques et filtrage par fin de vie ([#2921](https://github.com/dnum-mi/referentiel-applications/issues/2921)).
    - Mise en place d'un panneau d'administration pour la gestion des options d'hébergement ([#2763](https://github.com/dnum-mi/referentiel-applications/issues/2763)).
    - Intégration de la synchronisation avec Grist ([#2876](https://github.com/dnum-mi/referentiel-applications/issues/2876)) et ajout de colonnes dédiées ([#2901](https://github.com/dnum-mi/referentiel-applications/issues/2901)).
    - Gestion du cycle de vie des applications via de nouveaux tags de remplacement ([#2771](https://github.com/dnum-mi/referentiel-applications/issues/2771), [#2665](https://github.com/dnum-mi/referentiel-applications/issues/2665)).
- **Améliorations et corrections**
    - **Accessibilité** : Amélioration globale de la conformité RGAA sur les flux applicatifs et la stabilité du focus ([#2875](https://github.com/dnum-mi/referentiel-applications/issues/2875), [#2831](https://github.com/dnum-mi/referentiel-applications/issues/2831), [#2863](https://github.com/dnum-mi/referentiel-applications/issues/2863)).
    - **Gestion des droits** : Renforcement des contrôles d'accès (restrictions par capacité, protection contre la suppression de types utilisés, gestion des rôles admin) ([#2803](https://github.com/dnum-mi/referentiel-applications/issues/2803), [#2923](https://github.com/dnum-mi/referentiel-applications/issues/2923), [#2827](https://github.com/dnum-mi/referentiel-applications/issues/2827), [#2737](https://github.com/dnum-mi/referentiel-applications/issues/2737)).
    - **Recherche et interface** : Optimisation de la recherche par stack technologique ([#2770](https://github.com/dnum-mi/referentiel-applications/issues/2770)), amélioration des suggestions MAIA ([#2774](https://github.com/dnum-mi/referentiel-applications/issues/2774)) et correction de la pagination Excel ([#2829](https://github.com/dnum-mi/referentiel-applications/issues/2829)).
    - **Notifications** : Correction du filtrage et des actions de lecture des notifications ([#2772](https://github.com/dnum-mi/referentiel-applications/issues/2772)).

### Évolutions techniques
- **Sécurité**
    - Durcissement de l'accès applicatif et mise à jour des dépendances pour éliminer les vulnérabilités ([#2802](https://github.com/dnum-mi/referentiel-applications/issues/2802), [#2862](https://github.com/dnum-mi/referentiel-applications/issues/2862), [#2898](https://github.com/dnum-mi/referentiel-applications/issues/2898)).
    - Prévention de l'escalade de privilèges via les jetons de service délégués ([#2687](https://github.com/dnum-mi/referentiel-applications/issues/2687)).
- **Architecture et API**
    - Implémentation d'un filtre d'exception global et d'un contrat d'erreur normalisé pour l'API ([#2738](https://github.com/dnum-mi/referentiel-applications/issues/2738)).
    - Refactorisation du frontend (découpage des formulaires [#2766](https://github.com/dnum-mi/referentiel-applications/issues/2766)) et du backend (nettoyage des services et dépendances [#2762](https://github.com/dnum-mi/referentiel-applications/issues/2762)).
    - Unification des modales de recherche asynchrone et de relation ([#2664](https://github.com/dnum-mi/referentiel-applications/issues/2664)).
    - Amélioration de la validation des données entrantes (PATCH) ([#2799](https://github.com/dnum-mi/referentiel-applications/issues/2799)).
- **Qualité et CI/CD**
    - Renforcement des portes de qualité (quality gates) et de la couverture de tests frontend ([#2667](https://github.com/dnum-mi/referentiel-applications/issues/2667)).
    - Ajout de fixtures de QA pour les tests de corrélation ([#2773](https://github.com/dnum-mi/referentiel-applications/issues/2773)).

### Autres changements
- **Documentation**
    - Mise à jour du guide utilisateur et de la documentation sur la détection de corrélation ([#2764](https://github.com/dnum-mi/referentiel-applications/issues/2764), [#2922](https://github.com/dnum-mi/referentiel-applications/issues/2922)).
    - Clarification des processus d'authentification ([#2659](https://github.com/dnum-mi/referentiel-applications/issues/2659)).
