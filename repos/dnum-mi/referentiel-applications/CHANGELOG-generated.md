## Changelog : referentiel-applications (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a été marqué par un effort important sur l'accessibilité numérique (RGAA) et le renforcement de la sécurité de l'application. De nouvelles capacités d'exportation (PowerPoint, stacks technologiques) et de synchronisation de données (Grist) ont été déployées, ainsi qu'un nouveau système de gestion des fonctionnalités bêta pour permettre un déploiement progressif des nouveautés.

### Évolutions fonctionnelles
- **Accessibilité (RGAA) :** Améliorations significatives de l'expérience utilisateur pour les lecteurs d'écran, gestion du focus dans les tableaux et stabilisation des parcours utilisateurs [#3037](https://github.com/dnum-mi/referentiel-applications/issues/3037), [#3007](https://github.com/dnum-mi/referentiel-applications/issues/3007), [#2875](https://github.com/dnum-mi/referentiel-applications/issues/2875), [#2831](https://github.com/dnum-mi/referentiel-applications/issues/2831), [#2863](https://github.com/dnum-mi/referentiel-applications/issues/2863).
- **Nouvelles fonctionnalités d'export et de synchronisation :** 
    - Exportation des fiches produits vers PowerPoint [#2833](https://github.com/dnum-mi/referentiel-applications/issues/2833).
    - Exportation des stacks technologiques avec filtrage par fin de vie [#2921](https://github.com/dnum-mi/referentiel-applications/issues/2921).
    - Mise en place de la synchronisation avec Grist et ajout de colonnes dédiées [#2876](https://github.com/dnum-mi/referentiel-applications/issues/2876), [#2901](https://github.com/dnum-mi/referentiel-applications/issues/2901).
- **Administration et gestion :**
    - Création d'un panneau d'administration pour la gestion des options d'hébergement [#2763](https://github.com/dnum-mi/referentiel-applications/issues/2763).
    - Introduction d'un système de "capacités" pour activer/désactiver les fonctionnalités bêta [#3034](https://github.com/dnum-mi/referentiel-applications/issues/3034), [#3042](https://github.com/dnum-mi/referentiel-applications/issues/3042).
    - Ajout de tags de remplacement pour les applications non commissionnées [#2771](https://github.com/dnum-mi/referentiel-applications/issues/2771).
- **Gestion des droits et données :** 
    - Renforcement des permissions pour les administrateurs à périmètre restreint (scoped admin) [#3029](https://github.com/dnum-mi/referentiel-applications/issues/3029), [#2737](https://github.com/dnum-mi/referentiel-applications/issues/2737), [#2827](https://github.com/dnum-mi/referentiel-applications/issues/2827).
    - Restriction de l'accès aux technologies selon le périmètre et la capacité [#2803](https://github.com/dnum-mi/referentiel-applications/issues/2803).
    - Amélioration de la recherche (indexation des stacks) et de la gestion des notifications [#2770](https://github.com/dnum-mi/referentiel-applications/issues/2770), [#2772](https://github.com/dnum-mi/referentiel-applications/issues/2772).
    - Protection contre la suppression de types d'acteurs utilisés [#2923](https://github.com/dnum-mi/referentiel-applications/issues/2923).

### Évolutions techniques
- **Sécurité :** 
    - Durcissement de la validation des claims JWT [#3039](https://github.com/dnum-mi/referentiel-applications/issues/3039).
    - Masquage des jetons API dans les logs HTTP pour éviter les fuites de données [#3018](https://github.com/dnum-mi/referentiel-applications/issues/3018).
    - Nettoyage et mise à jour des dépendances pour éliminer les vulnérabilités [#2862](https://github.com/dnum-mi/referentiel-applications/issues/2862), [#2898](https://github.com/dnum-mi/referentiel-applications/issues/2898), [#2802](https://github.com/dnum-mi/referentiel-applications/issues/2802).
- **Architecture et API :**
    - Implémentation d'un filtre d'exception global et d'un contrat d'erreur normalisé pour l'API [#2738](https://github.com/dnum-mi/referentiel-applications/issues/2738).
    - Refactorisation du backend (services de base) et du frontend (découpage des étapes de formulaires) [#2762](https://github.com/dnum-mi/referentiel-applications/issues/2762), [#2766](https://github.com/dnum-mi/referentiel-applications/issues/2766).
    - Amélioration de la validation des corps de requêtes PATCH [#2799](https://github.com/dnum-mi/referentiel-applications/issues/2799).
- **Observabilité :** Ajout de logs spécifiques pour les appels API (tokens et MAIA) destinés à Loki [#3028](https://github.com/dnum-mi/referentiel-applications/issues/3028).

### Autres changements
- **Documentation :** Mise à jour du guide utilisateur, de la documentation sur la détection de corrélation et de la documentation Grafana [#2764](https://github.com/dnum-mi/referentiel-applications/issues/2764), [#2922](https://github.com/dnum-mi/referentiel-applications/issues/2922), [#3035](https://github.com/dnum-mi/referentiel-applications/issues/3035).
