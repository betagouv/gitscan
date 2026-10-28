## Changelog : referentiel-applications (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'accessibilité (RGAA) pour les utilisateurs de lecteurs d'écran et le renforcement de la sécurité des données (protection des jetons et des accès). Le catalogue gagne également en puissance avec de nouvelles capacités d'exportation (Excel, PowerPoint) et une meilleure gestion des fonctionnalités en phase bêta.

### Évolutions fonctionnelles
- **Exportation et données** :
    - Ajout de l'export des fiches produits au format PowerPoint [#2833](https://github.com/dnum-mi/referentiel-applications/issues/2833).
    - Amélioration des exports Excel avec l'inclusion du statut actuel [#3082](https://github.com/dnum-mi/referentiel-applications/issues/3082) et correction de la pagination [#2829](https://github.com/dnum-mi/referentiel-applications/issues/2829).
    - Mise en place de la synchronisation avec Grist [#2876](https://github.com/dnum-mi/referentiel-applications/issues/2876) et ajout de colonnes dédiées [#2901](https://github.com/dnum-mi/referentiel-applications/issues/2901).
- **Accessibilité (RGAA)** :
    - Amélioration de l'annonce des éléments pour les lecteurs d'écran (notifications [#3045](https://github.com/dnum-mi/referentiel-applications/issues/3045), chargement de l'application [#3037](https://github.com/dnum-mi/referentiel-applications/issues/3037)) et des liens externes [#3081](https://github.com/dnum-mi/referentiel-applications/issues/3081).
    - Optimisation de la gestion du focus pour les tableaux [#3007](https://github.com/dnum-mi/referentiel-applications/issues/3007).
- **Nouvelles fonctionnalités** :
    - Introduction d'un système de gestion des fonctionnalités bêta [#3034](https://github.com/dnum-mi/referentiel-applications/issues/3034) et limitation des exports HTML à cette capacité [#3042](https://github.com/dnum-mi/referentiel-applications/issues/3042).
    - Ajout d'un panneau d'administration pour la gestion des options d'hébergement [#2763](https://github.com/dnum-mi/referentiel-applications/issues/2763).
    - Ajout de tags de remplacement pour les applications non commissionnées [#2771](https://github.com/dnum-mi/referentiel-applications/issues/2771).
- **Recherche et filtrage** :
    - Amélioration de la recherche d'applications par source de données [#3055](https://github.com/dnum-mi/referentiel-applications/issues/3055) et par piles technologiques [#2770](https://github.com/dnum-mi/referentiel-applications/issues/2770).
    - Possibilité de filtrer les technologies par fin de vie (End of Life) [#2921](https://github.com/dnum-mi/referentiel-applications/issues/2921).

### Évolutions techniques
- **Sécurité** :
    - Renforcement de la validation des revendications JWT [#3039](https://github.com/dnum-mi/referentiel-applications/issues/3039) et durcissement de l'accès applicatif [#2802](https://github.com/dnum-mi/referentiel-applications/issues/2802).
    - Masquage des jetons API dans les logs HTTP [#3018](https://github.com/dnum-mi/referentiel-applications/issues/3018).
    - Mise à jour massive des dépendances pour corriger des vulnérabilités (pnpm, outils de build, dépendances verrouillées) [#3080](https://github.com/dnum-mi/referentiel-applications/issues/3080), [#2898](https://github.com/dnum-mi/referentiel-applications/issues/2898), [#2862](https://github.com/dnum-mi/referentiel-applications/issues/2862).
    - Limitation des capacités d'impersonation pour les administrateurs à un périmètre restreint [#3029](https://github.com/dnum-mi/referentiel-applications/issues/3029).
- **Architecture et Refactoring** :
    - Découpage du formulaire de création d'application en plusieurs étapes pour une meilleure gestion [#2766](https://github.com/dnum-mi/referentiel-applications/issues/2766).
    - Nettoyage des services de base du backend et des dépendances [#2762](https://github.com/dnum-mi/referentiel-applications/issues/2762).
    - Optimisation de la traversée des graphes de relations par distance la plus courte [#3030](https://github.com/dnum-mi/referentiel-applications/issues/3030).
- **CI/CD et Observabilité** :
    - Automatisation de la publication des images Docker lors de la création de releases [#3079](https://github.com/dnum-mi/referentiel-applications/issues/3079).
    - Amélioration de la traçabilité avec l'ajout de logs pour les appels API (Loki) [#3028](https://github.com/dnum-mi/referentiel-applications/issues/3028).

### Autres changements
- **Documentation** :
    - Mise à jour du guide utilisateur [#2764](https://github.com/dnum-mi/referentiel-applications/issues/2764).
    - Documentation des processus de détection et de revue humaine pour la corrélation [#2922](https://github.com/dnum-mi/referentiel-applications/issues/2922).
    - Mise à jour de la documentation Grafana [#3035](https://github.com/dnum-mi/referentiel-applications/issues/3035).
