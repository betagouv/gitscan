## Changelog : referentiel-applications (30 derniers jours, au 04/11/2026)

### Résumé
Ce mois a été marqué par le lancement de plusieurs fonctionnalités en version bêta (GristSync, exports HTML) et un effort important sur l'accessibilité (conformité RGAA). L'outil est devenu plus complet grâce à un système de notifications enrichi (résumés quotidiens, rappels) et des capacités d'exportation (Excel, PowerPoint) plus robustes et diversifiées.

### Évolutions fonctionnelles
- **Notifications** : Ajout de filtres par type d'événement [#3188], de rappels d'expiration de jetons [#3177], de la gestion des notifications lues [#2772] et mise en place d'un résumé quotidien par email [#3098].
- **Exports** : Amélioration de la fiabilité et de la performance des exports Excel [#3171, #3150, #3128, #3092, #2829], ajout de l'export des cartes produits vers PowerPoint [#2833] et mise à disposition des exports HTML en version bêta [#3042].
- **Accessibilité (RGAA)** : Améliorations globales des parcours utilisateurs [#2875], gestion de l'annonce des chargements pour les lecteurs d'écran [#3037], et optimisation de la navigation et des focus pour les tableaux et les liens [#3007, #3081, #2831, #2863].
- **Gestion des données et interface** : Introduction de la synchronisation Grist (en bêta) [#3190, #2876], gestion des logos lors des mises à jour [#3086], et mise à jour de la terminologie (passage de "fins de vie" à "technologies") [#3099].
- **Recherche et filtres** : Renommage des filtres personnels [#3104], correction de la recherche globale pour respecter les permissions [#3176] et restauration de la recherche par source de données [#3055].
- **Conformité** : Ajout de la cible de révision pour l'EcoIndex dans le modèle de conformité [#3172].

### Évolutions techniques
- **Sécurité** : Correction de plusieurs vulnérabilités sur les dépendances et les images Docker [#3088, #3102, #3080, #2898, #2862, #2802], renforcement de l'authentification JWT [#3039] et masquage des jetons API dans les logs HTTP [#3018].
- **Architecture et Concurrence** : Implémentation d'un service de verrouillage pour gérer les synchronisations concurrentes (GristSyncLock) [#3087] et optimisation de la gestion des graphes de relations [#3030, #3044].
- **CI/CD et Tests** : Amélioration de la publication des images lors des releases [#3079] et renforcement de la couverture de tests (permissions d'export, processus de corrélation) [#3106, #2773].

### Autres changements
- **Documentation** : Migration des décisions d'architecture vers la documentation officielle [#3089] et documentation des processus de détection et de revue humaine pour la corrélation [#2922].
