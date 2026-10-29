## Changelog : rdv-insertion (30 derniers jours, au 29 octobre 2026)

### Résumé
Ce mois-ci, les développements ont porté sur la fiabilisation des processus métiers (gestion des orientations, des suivis et des numéros de téléphone) et l'amélioration de la stabilité de l'API. Des efforts importants ont également été consacrés à l'optimisation de l'observabilité (réduction du bruit dans les alertes) et à l'automatisation de la revue de code pour garantir une meilleure qualité de livraison.

### Évolutions fonctionnelles
- **Gestion des orientations :** Amélioration de la détection des chevauchements et prise en compte des orientations débutant le jour même comme étant actives [#3408](https://github.com/gip-inclusion/rdv-insertion/issues/3408).
- **Suivi des dossiers :** Nouvelle fonctionnalité permettant d'enregistrer la date de clôture lors de la modification d'un suivi [#3400](https://github.com/gip-inclusion/rdv-insertion/issues/3400).
- **Gestion des contacts :** Correction de la détection des codes pays pour les numéros de téléphone mobiles des DROM [#3397](https://github.com/gip-inclusion/rdv-insertion/issues/3397).
- **Stabilité de l'API :** Correction d'un crash lors de l'invitation sans catégorie de motif [#3387](https://github.com/gip-inclusion/rdv-insertion/issues/3387) et exposition du type de catégorie de motif [#3411](https://github.com/gip-inclusion/rdv-insertion/issues/3411).

### Évolutions techniques
- **Automatisation de la revue :** Optimisation du workflow de revue de code via l'intégration de *relecteur* [#3417](https://github.com/gip-inclusion/rdv-insertion/issues/3417), [#3410](https://github.com/gip-inclusion/rdv-insertion/issues/3410) et la configuration de *CodeRabbit* [#3402](https://github.com/gip-inclusion/rdv-insertion/issues/3402), [#3405](https://github.com/gip-inclusion/rdv-insertion/issues/3405).
- **Observabilité et monitoring :** 
    - Optimisation de Sentry pour réduire le volume d'alertes non pertinentes (alertes métier, limites de débit France Travail) [#3389](https://github.com/gip-inclusion/rdv-insertion/issues/3389), [#3390](https://github.com/gip-inclusion/rdv-insertion/issues/3390), [#3383](https://github.com/gip-inclusion/rdv-insertion/issues/3383).
    - Correction de la configuration de Matomo pour une meilleure gestion des sources CSP [#3393](https://github.com/gip-inclusion/rdv-insertion/issues/3393), [#3394](https://github.com/gip-inclusion/rdv-insertion/issues/3394).
- **Performance et sécurité :** 
    - Optimisation du calcul des statistiques pour prévenir les dépassements de mémoire des conteneurs [#3382](https://github.com/gip-inclusion/rdv-insertion/issues/3382).
    - Renforcement de la sécurité via un rate-limiting des recherches par NIR plutôt que par IP [#3409](https://github.com/gip-inclusion/rdv-insertion/issues/3409).
- **Maintenance infrastructure :** Mise à jour de Ruby (4.0.9) [#3416](https://github.com/gip-inclusion/rdv-insertion/issues/3416) et correction des dépendances de base de données pour les agents [#3407](https://github.com/gip-inclusion/rdv-insertion/issues/3407).

### Autres changements
- **Documentation :** Mise à jour de la documentation du schéma de données [#3392](https://github.com/gip-inclusion/rdv-insertion/issues/3392) et création d'un fichier de conventions pour les agents [#3391](https://github.com/gip-inclusion/rdv-insertion/issues/3391).
- **Légal :** Ajout de la licence MIT [#3401](https://github.com/gip-inclusion/rdv-insertion/issues/3401).
- **Tests :** Révision des cas de tests négatifs pour les évaluations [#3403](https://github.com/gip-inclusion/rdv-insertion/issues/3403).
